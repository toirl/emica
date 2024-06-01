from typing import List

from emica.logger import get_logger

from .filter import Filter

log = get_logger()


class Pipeline:
    def __init__(self):
        self.filters: List[Filter] = []

    def add_filter(self, filter: Filter):
        self.filters.append(filter)

    def process(self, data: dict) -> dict:
        for filter in self.filters:
            log.info("Apply filter", filter=filter.__class__.__name__)
            data = filter.process(data)
        return data
