from enum import Enum
from typing import List

from scipy.interpolate import CubicSpline, interp1d

from emica.core.metrics import Metric


class InterpolationMode(Enum):
    LINEAR = 1
    SPLINE = 2


class CPU2Energy:
    def __init__(self, interpolation: InterpolationMode = InterpolationMode.SPLINE):
        self._curve: List[float] = [0.12, 0.32, 0.75, 1.02]
        self._points: List[float] = [0, 10, 50, 100]
        self._interpolation = interpolation
        self._spline = CubicSpline(self._points, self._curve)
        self._linear = interp1d(self._points, self._curve, kind="linear")

    def process(self, metric: Metric) -> Metric:
        if metric.cpu_thermal_design_power is None:
            raise ValueError("cpu_thermal_design_power must be set")
        if metric.cpu_utilization is None:
            raise ValueError("cpu_utilization must be set")

        if self._interpolation == InterpolationMode.SPLINE:
            # Spline interpolation
            percent = self._spline(metric.cpu_utilization)
            watts = float(percent) * metric.cpu_thermal_design_power
        else:
            # Linear interpolation
            percent = self._linear(metric.cpu_utilization)
            watts = float(percent) * metric.cpu_thermal_design_power

        metric.cpu_energy = watts * metric.duration / 3600 / 1000  # kWh/sec
        return metric
