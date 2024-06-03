from typing import List, Optional

from emica.core.metrics import Metrics
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
    def __init__(self, defaults: Optional[dict] = None):
        self.filters: List[Filter] = []
        if defaults is None:
            self.defaults = {}
        else:  # pragma: no cover
            self.defaults = defaults

    def set_defaults(self, defaults: dict):
        self.defaults = defaults

    def add_filter(self, filter: Filter):
        self.filters.append(filter)

    def process(self, metrics: Metrics) -> Metrics:
        metrics = apply_defaults(metrics, self.defaults)
        for filter in self.filters:
            log.info("Apply filter", filter=filter.__class__.__name__)
            for metric in metrics:
                try:
                    metric = filter.process(metric)
                except ValueError as e:  # pragma: no cover
                    log.warning("Ignoring metric", date=metric.timestamp.isoformat(), error=str(e))
                    continue
        return metrics
