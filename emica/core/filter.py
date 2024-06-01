from typing import Protocol


class Filter(Protocol):
    def process(self, data: dict) -> dict: ...
