from typing import Dict, Protocol


class Writer(Protocol):  # pragma: no cover
    def write(self, data: Dict) -> None: ...
