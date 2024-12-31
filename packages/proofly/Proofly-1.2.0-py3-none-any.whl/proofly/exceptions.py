class ValidationError(Exception):
    def __init__(self, message: str, invalid_fields: Optional[list] = None):
        super().__init__(message)
        self.message = message
        self.invalid_fields = invalid_fields or []

class ConfigurationError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class AnalysisError(Exception):
    def __init__(self, message: str, error_code: Optional[str] = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code