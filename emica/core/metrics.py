from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Optional


@dataclass
class Metric:
    timestamp: datetime
    """Start date of observation as UTC datetime"""
    duration: int
    """Duration of observation in seconds"""
    energy: Optional[float] = None
    """Total energy in kWh"""
    carbon: Optional[float] = None
    """Total carbon in gCO2eq"""
    carbon_embodied: Optional[float] = None
    """Embodied carbon in gCO2eg"""
    carbon_operational: Optional[float] = None
    """Operational carbon in gCO2eg"""
    cpu_utilization: Optional[float] = None
    """Utilisation of CPU in percent"""
    cpu_energy: Optional[float] = None
    """Energy used by the CPU in kWh"""
    cpu_thermal_design_power: Optional[int] = None
    """Thermal design power in Watt"""
    memory_energy_per_gb: float = 0.00039
    """Energy used to for every used GB of memory in kWh"""
    memory_utilization: Optional[float] = None
    """Utilisation of memory in percent"""
    memory_capacity: Optional[int] = None
    """Total capacity of memory in GB"""
    memory_energy: Optional[float] = None
    """Energy used by the memory in kWh"""
    device_emission_embodied: Optional[int] = None
    """The total Life Cycle Assessment (LCA) emissions of the device in gCO2eg"""
    device_expected_lifespan: Optional[int] = None
    """The excepted lifespan from manufaturing to disposal in seconds"""
    ressources_total: int = 1
    ressources_used: int = 1
    """Number of total ressources (cpu) which can be used for operation"""
    """Number of actually rsed ressources (cpu) for operation"""
    grid_carbon_intesity: Optional[int] = None
    """The emitted carbon during operation in gCO2eg"""
    funtional_unit: Optional[str] = None
    """The functional unit in which to express the carbon impact. Must a name of a attribute present in the metrics dataset"""
    funtional_unit_time: Optional[timedelta] = None
    """The time to be used for functional unit conversions"""
    sci: Optional[float] = None
    """SCI in gCO2eg per functional unit"""


@dataclass
class Metrics:
    data: List[Metric]
