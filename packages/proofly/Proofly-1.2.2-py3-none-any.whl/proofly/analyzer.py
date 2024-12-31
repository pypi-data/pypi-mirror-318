# src/proofly/analyzer.py
from dataclasses import dataclass
from typing import Dict, Any, Optional, List, Union
from .models import DiabetesMetrics, HypertensionMetrics, COPDMetrics
from .config import AnalysisConfig
from .exceptions import ValidationError, AnalysisError

@dataclass
class AnalysisResult:
    health_score: float
    risk_level: str
    confidence_score: float
    recommendations: List[str]
    
    def get_detailed_analysis(self):
        return {
            "health_score": self.health_score,
            "risk_level": self.risk_level,
            "confidence_score": self.confidence_score,
            "recommendations": self.recommendations
        }

class HealthAnalyzer:
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = AnalysisConfig(**(config or {}))

    def analyze_metrics(self, condition: str, metrics: Union[DiabetesMetrics, HypertensionMetrics, COPDMetrics]):
        if not self._validate_metrics(condition, metrics):
            raise ValidationError("Invalid metrics provided for condition")
        
        try:
            health_score = self._calculate_health_score(condition, metrics)
            risk_level = self._determine_risk_level(health_score)
            confidence = self._calculate_confidence(metrics)
            recommendations = self._generate_recommendations(condition, metrics, risk_level)
            
            return AnalysisResult(
                health_score=health_score,
                risk_level=risk_level,
                confidence_score=confidence,
                recommendations=recommendations
            )
        except Exception as e:
            raise AnalysisError(f"Analysis failed: {str(e)}")

    def _validate_metrics(self, condition: str, metrics: Any) -> bool:
        condition_map = {
            "diabetes": DiabetesMetrics,
            "hypertension": HypertensionMetrics,
            "copd": COPDMetrics
        }
        return isinstance(metrics, condition_map.get(condition, object))

    def _calculate_health_score(self, condition: str, metrics: Any) -> float:
        if condition == "diabetes":
            base_score = 100
            if metrics.blood_glucose > 120:
                base_score -= 10
            if metrics.hba1c > 6.5:
                base_score -= 15
            return max(0, min(100, base_score))
        elif condition == "hypertension":
            base_score = 100
            if metrics.systolic_pressure > 130:
                base_score -= 10
            if metrics.diastolic_pressure > 85:
                base_score -= 10
            return max(0, min(100, base_score))
        elif condition == "copd":
            base_score = 100
            if metrics.oxygen_saturation < 95:
                base_score -= 15
            if metrics.respiratory_rate > 20:
                base_score -= 10
            return max(0, min(100, base_score))
        return 75.0

    def _determine_risk_level(self, health_score: float) -> str:
        if health_score >= 80:
            return "LOW"
        elif health_score >= 60:
            return "MODERATE"
        return "HIGH"

    def _calculate_confidence(self, metrics: Any) -> float:
        return 85.0

    def _generate_recommendations(self, condition: str, metrics: Any, risk_level: str) -> List[str]:
        recommendations = {
            "diabetes": ["Monitor blood glucose regularly", "Maintain a balanced diet"],
            "hypertension": ["Monitor blood pressure daily", "Reduce sodium intake"],
            "copd": ["Practice breathing exercises", "Follow medication schedule"]
        }
        return recommendations.get(condition, ["Consult healthcare provider"])