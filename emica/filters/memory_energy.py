from emica.core.metrics import Metric


class Memory2Energy:
    def process(self, metric: Metric) -> Metric:
        if metric.memory_capacity is None:
            raise ValueError("memory_capacity must be set")
        if metric.memory_utilization is None:
            raise ValueError("memory_utilization must be set")
        used_mem = metric.memory_utilization / 100 * metric.memory_capacity
        metric.memory_energy = used_mem * metric.memory_energy_per_gb
        return metric
