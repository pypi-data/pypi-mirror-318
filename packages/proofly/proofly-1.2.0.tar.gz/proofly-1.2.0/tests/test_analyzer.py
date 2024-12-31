import pytest
from proofly import HealthAnalyzer
from proofly.models import DiabetesMetrics
from proofly.exceptions import ValidationError

def test_health_analyzer_initialization():
    analyzer = HealthAnalyzer()
    assert analyzer is not None

def test_analyze_diabetes_metrics():
    analyzer = HealthAnalyzer()
    metrics = DiabetesMetrics(
        blood_glucose=120,
        hba1c=6.5,
        blood_pressure=130
    )
    result = analyzer.analyze_metrics("diabetes", metrics)
    assert isinstance(result.health_score, float)
    assert isinstance(result.risk_level, str)
    assert isinstance(result.confidence_score, float)
    assert isinstance(result.recommendations, list)