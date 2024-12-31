from dataclasses import dataclass
from typing import Dict, Any, Optional, List, Union, Type
from decimal import Decimal, ROUND_HALF_UP
from enum import Enum
from .models import DiabetesMetrics, HypertensionMetrics, COPDMetrics
from .config import AnalysisConfig
from .exceptions import ValidationError, AnalysisError

class RiskLevel(Enum):
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"

    @classmethod
    def from_score(cls, score: float) -> 'RiskLevel':
        if score >= 80:
            return cls.LOW
        elif score >= 60:
            return cls.MODERATE
        return cls.HIGH

@dataclass
class AnalysisResult:
    health_score: Decimal
    risk_level: RiskLevel
    confidence_score: Decimal
    recommendations: List[str]

    def __post_init__(self):
        self.health_score = Decimal(str(self.health_score)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        self.confidence_score = Decimal(str(self.confidence_score)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

    def get_detailed_analysis(self) -> Dict[str, Any]:
        return {
            "health_score": float(self.health_score),
            "risk_level": self.risk_level.value,
            "confidence_score": float(self.confidence_score),
            "recommendations": self.recommendations
        }

class MetricAnalyzer:
    def __init__(self, base_score: int = 100):
        self.base_score = base_score
        self._deductions = []

    def add_deduction(self, condition: bool, amount: int, reason: str):
        if condition:
            self._deductions.append((amount, reason))

    def get_score(self) -> float:
        final_score = self.base_score - sum(amount for amount, _ in self._deductions)
        return max(0, min(100, final_score))

    def get_confidence(self) -> float:
        return max(0, 100 - (len(self._deductions) * 5))

class HealthAnalyzer:
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = AnalysisConfig(**(config or {}))
        self._condition_map = {
            "diabetes": (DiabetesMetrics, self._analyze_diabetes),
            "hypertension": (HypertensionMetrics, self._analyze_hypertension),
            "copd": (COPDMetrics, self._analyze_copd)
        }
        self._recommendations = self._initialize_recommendations()

    def analyze_metrics(self, condition: str, metrics: Union[DiabetesMetrics, HypertensionMetrics, COPDMetrics]) -> AnalysisResult:
        if condition not in self._condition_map:
            raise ValidationError(f"Unsupported condition: {condition}")

        expected_type, analyzer_func = self._condition_map[condition]
        if not isinstance(metrics, expected_type):
            raise ValidationError(f"Invalid metrics type for {condition}")

        try:
            analyzer = MetricAnalyzer()
            analyzer_func(metrics, analyzer)
            
            health_score = analyzer.get_score()
            risk_level = RiskLevel.from_score(health_score)
            confidence_score = analyzer.get_confidence()
            
            return AnalysisResult(
                health_score=health_score,
                risk_level=risk_level,
                confidence_score=confidence_score,
                recommendations=self._get_recommendations(condition, risk_level)
            )
        except Exception as e:
            raise AnalysisError(f"Analysis failed: {str(e)}")

    def _analyze_diabetes(self, metrics: DiabetesMetrics, analyzer: MetricAnalyzer):
        analyzer.add_deduction(
            metrics.blood_glucose > 120,
            10,
            "Elevated blood glucose"
        )
        analyzer.add_deduction(
            metrics.hba1c > 6.5,
            15,
            "High HbA1c"
        )

    def _analyze_hypertension(self, metrics: HypertensionMetrics, analyzer: MetricAnalyzer):
        analyzer.add_deduction(
            metrics.systolic_pressure > 130,
            10,
            "Elevated systolic pressure"
        )
        analyzer.add_deduction(
            metrics.diastolic_pressure > 85,
            10,
            "Elevated diastolic pressure"
        )

    def _analyze_copd(self, metrics: COPDMetrics, analyzer: MetricAnalyzer):
        analyzer.add_deduction(
            metrics.oxygen_saturation < 95,
            15,
            "Low oxygen saturation"
        )
        analyzer.add_deduction(
            metrics.respiratory_rate > 20,
            10,
            "High respiratory rate"
        )

    def _initialize_recommendations(self) -> Dict[str, Dict[RiskLevel, List[str]]]:
        return {
            "diabetes": {
                RiskLevel.LOW: [
                    "Continue monitoring blood glucose regularly",
                    "Maintain current diet and exercise routine"
                ],
                RiskLevel.MODERATE: [
                    "Increase blood glucose monitoring frequency",
                    "Review and adjust diet plan",
                    "Consider consulting with diabetes educator"
                ],
                RiskLevel.HIGH: [
                    "Schedule immediate consultation with healthcare provider",
                    "Monitor blood glucose multiple times daily",
                    "Strictly follow medication schedule",
                    "Review and modify lifestyle factors"
                ]
            },
            "hypertension": {
                RiskLevel.LOW: [
                    "Continue daily blood pressure monitoring",
                    "Maintain healthy lifestyle habits"
                ],
                RiskLevel.MODERATE: [
                    "Increase blood pressure monitoring frequency",
                    "Reduce sodium intake",
                    "Implement stress management techniques"
                ],
                RiskLevel.HIGH: [
                    "Seek immediate medical attention",
                    "Monitor blood pressure several times daily",
                    "Strictly follow medication regimen",
                    "Implement comprehensive lifestyle changes"
                ]
            },
            "copd": {
                RiskLevel.LOW: [
                    "Continue prescribed medication routine",
                    "Practice regular breathing exercises"
                ],
                RiskLevel.MODERATE: [
                    "Increase frequency of breathing exercises",
                    "Review and optimize medication usage",
                    "Monitor symptoms more closely"
                ],
                RiskLevel.HIGH: [
                    "Contact healthcare provider immediately",
                    "Use rescue medications as prescribed",
                    "Monitor oxygen levels frequently",
                    "Minimize exposure to triggers"
                ]
            }
        }

    def _get_recommendations(self, condition: str, risk_level: RiskLevel) -> List[str]:
        return self._recommendations.get(condition, {}).get(
            risk_level,
            ["Consult healthcare provider for personalized recommendations"]
        )