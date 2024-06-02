from emica.core.metrics import Metrics


class Memory2Energy:
    def process(self, metrics: Metrics) -> Metrics:
        for metric in metrics.data:
            if metric.memory_capacity is None:
                raise ValueError("memory_capacity must be set")
            if metric.memory_utilization is None:
                raise ValueError("memory_utilization must be set")
            used_mem = metric.memory_capacity / 100 * metric.memory_utilization
            metric.memory_energy = used_mem * metric.memory_energy_per_gb
        return metrics
