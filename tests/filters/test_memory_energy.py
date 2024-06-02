from datetime import UTC, datetime

import pytest

from emica.core.metrics import Metric
from emica.filters.memory_energy import Memory2Energy


def test_process():
    # Arrange
    m = Metric(timestamp=datetime.now(tz=UTC), duration=60, memory_capacity=16, memory_utilization=26.267051696777344)
    f = Memory2Energy()
    # Act
    r = f.process(m)
    # Assert
    assert r.memory_energy == 0.001647469482421875


@pytest.mark.parametrize("attr", ["memory_capacity", "memory_utilization"])
def test_fail_on_missing_attr(attr: str):
    # Arrange
    m = Metric(timestamp=datetime.now(tz=UTC), duration=60, memory_capacity=16, memory_utilization=26.267051696777344)
    setattr(m, attr, None)
    f = Memory2Energy()
    # Act
    with pytest.raises(ValueError):
        f.process(m)
