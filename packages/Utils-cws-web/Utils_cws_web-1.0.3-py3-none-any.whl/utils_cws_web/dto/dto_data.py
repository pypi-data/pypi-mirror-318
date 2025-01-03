from marshmallow import Schema, fields, ValidationError
from typing import Dict, Any, Union, NoReturn

from utils_cws_web.dto.schema_error import SchemaErrorType
from utils_cws_web.exception.schema_exception import SchemaException

from utils_cws_web.dto.schema_registry import Schema_registry


class DTOData:
    def __init__(self, data: Dict[str, Any], schema: Schema):
        self._data = data
        self._schema = schema

    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            return self._data[name]
        raise SchemaException(
            message=f"Attribute '{name}' not found",
            error_type=SchemaErrorType.DATA_ACCESS_ERROR
        )

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def to_dict(self) -> Dict[str, Any]:
        return self._data.copy()

    def update(self, **kwargs) -> None:
        self._data.update(kwargs)

    def serialize(self) -> Dict[str, Any]:
        try:
            return self._schema.dump(self._data)
        except Exception as e:
            raise SchemaException(
                message="Error serializing data",
                error_type=SchemaErrorType.PROCESSING_ERROR,
                original_exception=e
            )

    def to_json(self) -> str:
        try:
            return self._schema.dumps(self._data)
        except Exception as e:
            raise SchemaException(
                message="Error converting to JSON",
                error_type=SchemaErrorType.PROCESSING_ERROR,
                original_exception=e
            )

    def validate(self) -> Dict[str, Any]:
        try:
            errors = self._schema.validate(self._data)
            if errors:
                raise SchemaException(
                    message="Validation error",
                    error_type=SchemaErrorType.VALIDATION_ERROR,
                    details={"validation_errors": errors}
                )
            return self._data
        except Exception as e:
            if not isinstance(e, SchemaException):
                raise SchemaException(
                    message="Error validating data",
                    error_type=SchemaErrorType.VALIDATION_ERROR,
                    original_exception=e
                )
            raise

    @staticmethod
    def from_schema_name(schema_name: str, data: Dict[str, Any]) -> 'DTOData':
        """Create an instance using the schema name"""
        schema_cls = Schema_registry.get(schema_name)
        if schema_cls is None:
            raise SchemaException(
                message=f"Schema '{schema_name}' not found",
                error_type=SchemaErrorType.SCHEMA_NOT_FOUND
            )
        
        schema = schema_cls()
        try:
            validated_data = schema.load(data)
            return DTOData(validated_data, schema)
        except ValidationError as ve:
            raise SchemaException(
                message="Validation error",
                error_type=SchemaErrorType.VALIDATION_ERROR,
                details={"validation_errors": ve.messages}
            )

    @staticmethod
    def from_json(schema_name: str, json_str: str) -> 'DTOData':
        """Create an instance from a JSON string"""
        schema_cls = Schema_registry.get(schema_name)
        if schema_cls is None:
            raise SchemaException(
                message=f"Schema '{schema_name}' not found",
                error_type=SchemaErrorType.SCHEMA_NOT_FOUND
            )
        
        schema = schema_cls()
        try:
            data = schema.loads(json_str)
            return DTOData(data, schema)
        except Exception as e:
            raise SchemaException(
                message="Error loading from JSON",
                error_type=SchemaErrorType.PROCESSING_ERROR,
                original_exception=e
            )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}({self._data})>"

def create_dto(schema_name: str, fields_dict: Dict[str, fields.Field]):
    """
    Decorator to create and register a DTO with its associated schema.
    Ensures that the decorated function always returns a DTOData.
    """
    def decorator(func):
        try:
            # Create the schema class
            schema_cls = type(f"{schema_name}Schema", (Schema,), fields_dict)
            Schema_registry.register(schema_name, schema_cls)
            schema = schema_cls()

            def wrapper(*args, **kwargs) -> DTOData:
                try:
                    # Get and validate input data
                    input_data = kwargs.get("data", args[0] if args else {})
                    if isinstance(input_data, DTOData):
                        data_wrapper = input_data
                    else:
                        try:
                            validated_data = schema.load(input_data)
                            data_wrapper = DTOData(validated_data, schema)
                        except ValidationError as ve:
                            raise SchemaException(
                                message="Error in data validation",
                                error_type=SchemaErrorType.VALIDATION_ERROR,
                                details={"validation_errors": ve.messages}
                            )
                    
                    # Execute the decorated function
                    result = func(data_wrapper)

                    if not isinstance(result, DTOData) or result is None:
                        raise SchemaException(
                            message="The decorated function did not return a DTOData",
                            error_type=SchemaErrorType.RETURN_TYPE_ERROR
                        )
                    
                    return result

                except Exception as e:
                    if isinstance(e, SchemaException):
                        raise
                    raise SchemaException(
                        message="Error processing data",
                        error_type=SchemaErrorType.PROCESSING_ERROR,
                        original_exception=e
                    )
            return wrapper

        except Exception as e:
            raise SchemaException(
                message=f"Error creating schema '{schema_name}'",
                error_type=SchemaErrorType.REGISTRATION_ERROR,
                original_exception=e
            )
    return decorator