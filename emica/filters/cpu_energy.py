from emica.core.metrics import Metric


class CPU2Energy:
    def process(self, metric: Metric) -> Metric:
        if metric.cpu_thermal_design_power is None:
            raise ValueError("cpu_thermal_design_power must be set")
        if metric.cpu_utilization is None:
            raise ValueError("cpu_utilization must be set")
        metric.cpu_energy = metric.cpu_thermal_design_power / 100 * metric.cpu_utilization
        return metric
