import yaml

from emica.logger import get_logger

log = get_logger()


class InstanceConfig:  # pragma: no cover
    def __init__(self, path: str):
        self.demo_data = {"global": {}, "instances": {}}
        with open(path, "r") as f:
            self._data = yaml.safe_load(f)

    def get_defaults(self, name: str):
        try:
            return self._data["instances"][name]
        except KeyError:
            log.warning("Applied global config", instance=name)
            return self._data["global"]
