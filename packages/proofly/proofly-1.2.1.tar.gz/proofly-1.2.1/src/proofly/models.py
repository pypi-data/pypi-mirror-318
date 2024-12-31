from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class DiabetesMetrics:
    blood_glucose: float
    hba1c: float
    blood_pressure: float
    timestamp: Optional[datetime] = None

@dataclass
class HypertensionMetrics:
    systolic_pressure: float
    diastolic_pressure: float
    heart_rate: float
    timestamp: Optional[datetime] = None

@dataclass
class COPDMetrics:
    oxygen_saturation: float
    peak_flow: float
    respiratory_rate: float
    timestamp: Optional[datetime] = None