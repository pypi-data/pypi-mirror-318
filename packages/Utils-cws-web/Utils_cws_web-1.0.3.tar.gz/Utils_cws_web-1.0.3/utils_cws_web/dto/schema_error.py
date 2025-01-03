from enum import Enum

class SchemaErrorType(Enum):
    VALIDATION_ERROR = "validation_error"
    SCHEMA_NOT_FOUND = "schema_not_found"
    REGISTRATION_ERROR = "registration_error"
    DATA_ACCESS_ERROR = "data_access_error"
    PROCESSING_ERROR = "processing_error"
    RETURN_TYPE_ERROR = "return_type_error"