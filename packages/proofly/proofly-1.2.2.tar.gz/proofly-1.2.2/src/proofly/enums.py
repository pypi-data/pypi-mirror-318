from enum import Enum

class ValidationMode(str, Enum):
    STRICT = "strict"
    LENIENT = "lenient"

class RiskModel(str, Enum):
    CONSERVATIVE = "conservative"
    MODERATE = "moderate"
    AGGRESSIVE = "aggressive"

class ReportFormat(str, Enum):
    PDF = "pdf"
    JSON = "json"
    HTML = "html"