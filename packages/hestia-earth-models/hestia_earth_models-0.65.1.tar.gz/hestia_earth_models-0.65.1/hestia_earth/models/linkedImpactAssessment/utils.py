from functools import reduce
from hestia_earth.utils.tools import non_empty_list, flatten, list_sum

from hestia_earth.models.log import log_as_table, logRequirements, logShouldRun
from hestia_earth.models.utils import sum_values, _include
from hestia_earth.models.utils.indicator import _new_indicator
from hestia_earth.models.utils.impact_assessment import get_product, convert_value_from_cycle
from hestia_earth.models.utils.input import load_impacts
from . import MODEL


def _indicator(term_id: str, value: float):
    indicator = _new_indicator(term_id, MODEL)
    indicator['value'] = value
    return indicator


def _run_indicators(product: dict, term_id: str):
    def run(values: list):
        indicator = values[0].get('indicator')
        values_from_cycle = non_empty_list([
            list_sum(value.get('input').get('value')) * value.get('indicator').get('value')
            for value in values
        ])
        value = convert_value_from_cycle(product, sum_values(values_from_cycle), model=MODEL, term_id=term_id)
        return (
            _indicator(term_id, value) | _include(indicator, ['landCover', 'previousLandCover'])
        ) if value is not None else None
    return run


def _group_indicator(group: dict, value: dict):
    group_key = ';'.join(non_empty_list([
        value.get('indicator').get('landCover', {}).get('@id'),
        value.get('indicator').get('previousLandCover', {}).get('@id')
    ]))
    group[group_key] = group.get(group_key, []) + [value]
    return group


def _run_inputs_production(impact_assessment: dict, product: dict, term_id: str):
    cycle = impact_assessment.get('cycle', {})

    # group all indicators per `landCover` and `previousLandCover`
    all_indicators = flatten([
        {
            'indicator': indicator,
            'input': input
        }
        for input in load_impacts(cycle.get('inputs', []))
        for indicator in (
            input.get('impactAssessment', {}).get('emissionsResourceUse', []) +
            input.get('impactAssessment', {}).get('impacts', [])
        )
        if indicator.get('term', {}).get('@id') in [
            term_id,
            term_id.replace('InputsProduction', 'DuringCycle')
        ]
    ])
    valid_indicators = [
        value
        for value in all_indicators
        if all([
            value.get('indicator').get('value', -1) > 0,
            list_sum(value.get('input').get('value', [-1]), 0) > 0
        ])
    ]
    grouped_indicators = reduce(_group_indicator, valid_indicators, {})
    has_indicators = bool(valid_indicators)

    logRequirements(impact_assessment, model=MODEL, term=term_id,
                    indicators=log_as_table([
                        {
                            'indicator-id': value.get('indicator').get('term', {}).get('@id'),
                            'indicator-value': value.get('indicator').get('value'),
                            'input-id': value.get('input').get('term', {}).get('@id'),
                            'input-value': list_sum(value.get('input').get('value')),
                        }
                        for value in all_indicators
                    ]))

    should_run = all([has_indicators])
    logShouldRun(impact_assessment, MODEL, term_id, should_run)

    return non_empty_list(flatten(map(_run_indicators(product, term_id), grouped_indicators.values())))


def _should_run_inputs_production(impact_assessment: dict, term_id: str):
    product = get_product(impact_assessment) or {}
    product_id = product.get('term', {}).get('@id')

    product_value = list_sum(product.get('value', []), default=None)
    economic_value = product.get('economicValueShare')

    logRequirements(impact_assessment, model=MODEL, term=term_id,
                    product_id=product_id,
                    product_value=product_value,
                    product_economicValueShare=economic_value)

    should_run = all([product, product_value, economic_value])
    logShouldRun(impact_assessment, MODEL, term_id, should_run)
    return should_run, product


def run_inputs_production(impact_assessment: dict, term_id: str):
    should_run, product = _should_run_inputs_production(impact_assessment, term_id)
    return _run_inputs_production(impact_assessment, product, term_id) if should_run else []
