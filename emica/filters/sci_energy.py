from emica.core.metrics import Metrics


class SCIEnergy:
    def process(self, metrics: Metrics) -> Metrics:
        for metric in metrics.data:
            metric.energy = 0
            if metric.cpu_energy is not None:
                metric.energy += metric.cpu_energy
            if metric.memory_energy is not None:
                metric.energy += metric.memory_energy
            if metric.energy == 0:
                raise ValueError("Either cpu_energy or memory_energy must be set")
        return metrics
