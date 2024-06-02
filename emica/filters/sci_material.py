from emica.core.metrics import Metrics


class SCIMaterial:
    def process(self, metrics: Metrics) -> Metrics:
        for metric in metrics.data:
            if metric.device_expected_lifespan is None:
                raise ValueError("device_expected_lifespan must be set")
            if metric.device_emission_embodied is None:
                raise ValueError("device_emission_embodied must be set")
            time_share = metric.duration / metric.device_expected_lifespan
            resource_share = metric.ressources_used / metric.ressources_total
            metric.carbon_embodied = metric.device_emission_embodied * time_share * resource_share
        return metrics
