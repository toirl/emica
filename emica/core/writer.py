from typing import Protocol

from emica.core.metrics import Instances


class Writer(Protocol):  # pragma: no cover
    def write(self, instances: Instances) -> None: ...
