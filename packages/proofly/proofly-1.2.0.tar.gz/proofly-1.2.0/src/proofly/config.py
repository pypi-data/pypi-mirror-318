from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class AnalysisConfig:
    logging_level: str = "INFO"
    cache_enabled: bool = True
    validation_mode: str = "strict"

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]):
        return cls(**config_dict)

@dataclass
class MetricConfig:
    ranges: Dict[str, Any]
    condition: str

    @classmethod
    def get_condition_config(cls, condition: str):
        default_ranges = {
            "diabetes": {
                "blood_glucose": {"normal": (70, 120)},
                "hba1c": {"normal": (4.0, 5.7)},
                "blood_pressure": {"normal": (90, 120)}
            }
        }
        return cls(ranges=default_ranges.get(condition, {}), condition=condition)
