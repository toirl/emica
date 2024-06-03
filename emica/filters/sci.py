from datetime import timedelta

from emica.core.metrics import Metric


class SCI:
    def __init__(self, functional_unit: str, functional_unit_time: timedelta):
        self._functional_unit = functional_unit
        self._functional_unit_time = functional_unit_time

    def process(self, metric: Metric) -> Metric:
        carbon = 0
        if metric.carbon_operational is not None:
            carbon += metric.carbon_operational
        if metric.carbon_embodied is not None:
            carbon += metric.carbon_embodied
        if carbon == 0:
            raise ValueError("Either carbon_embodied or carbon_operational must be set")
        if metric.functional_unit is None:
            metric.functional_unit = self._functional_unit
        if metric.functional_unit_time is None:
            metric.functional_unit_time = self._functional_unit_time

        metric.carbon = carbon / getattr(metric, metric.functional_unit)
        metric.sci = (
            metric.carbon / getattr(metric, metric.functional_unit) * metric.functional_unit_time.total_seconds()
        )
        return metric
