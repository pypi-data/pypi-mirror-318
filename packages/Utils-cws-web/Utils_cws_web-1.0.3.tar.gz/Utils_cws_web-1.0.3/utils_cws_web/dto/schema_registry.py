from marshmallow import Schema
from typing import Dict, Type, Optional

from utils_cws_web.dto.schema_error import SchemaErrorType
from utils_cws_web.exception.schema_exception import SchemaException

class Schema_registry:
    _instance = None
    _schemas: Dict[str, Type[Schema]] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def register(cls, schema_name: str, schema_cls: Type[Schema]) -> None:
        if schema_name in cls._schemas:
            raise SchemaException(
                message=f"Schema '{schema_name}' ya está registrado",
                error_type=SchemaErrorType.REGISTRATION_ERROR
            )
        cls._schemas[schema_name] = schema_cls

    @classmethod
    def get(cls, schema_name: str) -> Optional[Type[Schema]]:
        return cls._schemas.get(schema_name)

    @classmethod
    def clear(cls) -> None:
        cls._schemas.clear()