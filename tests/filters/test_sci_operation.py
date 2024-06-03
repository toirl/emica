import pytest

from emica.core.metrics import Metric
from emica.filters.sci_operation import SCIOperation


@pytest.mark.parametrize("attr", ["energy", "grid_carbon_intensity"])
def test_fail_on_missing_energy_attr(attr: str, metric: Metric):
    # Arrange
    setattr(metric, attr, None)
    f = SCIOperation()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(metric)


def test_calculation(metric: Metric):
    # Arrange
    # Act
    f = SCIOperation()
    r = f.process(metric)
    # Assert
    assert r.carbon_operational == 0.8734594542010893
