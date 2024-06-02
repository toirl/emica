from emica.core.metrics import Metric


class SCIOperation:
    def process(self, metric: Metric) -> Metric:
        if metric.energy is None:
            raise ValueError("energy must be set")
        if metric.grid_carbon_intesity is None:
            raise ValueError("grid_carbon_intesity must be set")
        metric.carbon_operational = metric.energy * metric.grid_carbon_intesity
        return metric
