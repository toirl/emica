from emica.core.metrics import Metric


class SCI:
    def process(self, metric: Metric) -> Metric:
        carbon = 0
        if metric.carbon_operational is not None:
            carbon += metric.carbon_operational
        if metric.carbon_embodied is not None:
            carbon += metric.carbon_embodied
        if carbon == 0:
            raise ValueError("Either carbon_embodied or carbon_operational must be set")
        if metric.funtional_unit is None:
            raise ValueError("functional_unit must be set")
        if metric.funtional_unit_time is None:
            raise ValueError("functional_unit_time must be set")

        carbon = carbon * metric.funtional_unit_time.total_seconds()
        metric.carbon = carbon
        metric.sci = metric.carbon / getattr(metric, metric.funtional_unit)
        return metric
