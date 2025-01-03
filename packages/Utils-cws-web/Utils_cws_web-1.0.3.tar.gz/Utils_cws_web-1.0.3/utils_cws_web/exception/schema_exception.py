from typing import Optional, Dict, Any

from utils_cws_web.dto.schema_error import SchemaErrorType

class SchemaException(Exception):
    def __init__(self, 
                 message: str, 
                 error_type: SchemaErrorType, 
                 details: Optional[Dict] = None,
                 original_exception: Optional[Exception] = None):
        super().__init__(message)
        self.error_type = error_type
        self.details = details or {}
        self.original_exception = original_exception

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error_type": self.error_type.value,
            "message": str(self),
            "details": self.details
        }