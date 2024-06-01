from typing import Dict, Protocol


class Writer(Protocol):
    def write(self, data: Dict) -> None: ...
