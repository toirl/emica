from typing import Protocol

from emica.core.metrics import Metrics


class Loader(Protocol):
    def fetch_data(self) -> Metrics: ...
