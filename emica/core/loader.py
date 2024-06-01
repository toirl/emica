from typing import Dict, Protocol


class Loader(Protocol):
    def fetch_data(self) -> Dict: ...
