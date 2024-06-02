from typing import Protocol

from emica.core.metrics import Metrics


class Loader(Protocol):  # pragma: no cover
    def fetch_data(self) -> Metrics: ...
