from typing import Protocol

from emica.core.metrics import Metric


class Filter(Protocol):  # pragma: no cover
    def process(self, metric: Metric) -> Metric: ...
