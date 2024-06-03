from datetime import timedelta
from typing import List

from emica.core.metrics import Instances, Metrics
from emica.logger import get_logger

from .filter import Filter

log = get_logger()


def apply_defaults(metrics: Metrics, defaults: dict) -> Metrics:  # pragma: no cover
    for key in defaults:
        for metric in metrics.data:
            if getattr(metric, key) is None:
                setattr(metric, key, defaults[key])
    return metrics


class Pipeline:
    def __init__(self):
        self.filters: List[Filter] = []

    def add_filter(self, filter: Filter):
        self.filters.append(filter)

    def process(self, instances: Instances) -> Instances:
        for instance in instances:
            log.info("Processing Instance", instance=instance)
            metrics = instances[instance]
            defaults = {
                "cpu_thermal_design_power": 20,
                "device_expected_lifespan": 94608000,
                "device_emission_embodied": 147000,
                "grid_carbon_intensity": 500,
                "functional_unit": "duration",
                "functional_unit_time": timedelta(minutes=1),
            }
            metrics = apply_defaults(metrics, defaults)
            for filter in self.filters:
                log.info("Apply filter", filter=filter.__class__.__name__)
                for metric in metrics:
                    try:
                        metric = filter.process(metric)
                    except ValueError as e:  # pragma: no cover
                        log.warning("Ignoring metric", date=metric.timestamp.isoformat(), error=str(e))
                        continue
        return instances
