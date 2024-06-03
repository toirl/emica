import pytest

from emica.core.metrics import Metric
from emica.filters.memory_energy import Memory2Energy


def test_process(metric: Metric):
    # Arrange
    f = Memory2Energy()
    # Act
    r = f.process(metric)
    # Assert
    assert r.memory_energy == 0.001647469482421875


@pytest.mark.parametrize("attr", ["memory_capacity", "memory_utilization"])
def test_fail_on_missing_attr(attr: str, metric: Metric):
    # Arrange
    setattr(metric, attr, None)
    f = Memory2Energy()
    # Act
    with pytest.raises(ValueError):
        f.process(metric)
