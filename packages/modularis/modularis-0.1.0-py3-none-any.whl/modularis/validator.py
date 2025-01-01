from typing import Any, Dict, Type, Optional
from pydantic import BaseModel, create_model, ValidationError

class SchemaValidator:
    def __init__(self):
        self._schemas: Dict[str, Type[BaseModel]] = {}

    def add_schema(self, name: str, schema: Dict[str, Any]):
        model = create_model(name, **schema)
        self._schemas[name] = model

    def validate_request(self, kwargs: Dict[str, Any], schema_name: Optional[str] = None) -> None:
        if not schema_name or schema_name not in self._schemas:
            return
        
        schema = self._schemas[schema_name]
        data = kwargs.get('json', {})
        
        try:
            validated_data = schema(**data)
            kwargs['json'] = validated_data.dict()
        except ValidationError as e:
            raise ValidationException(str(e))

    def validate_response(self, data: Any, schema_name: str) -> Any:
        if schema_name not in self._schemas:
            raise ValueError(f"Schema {schema_name} not found")
        
        schema = self._schemas[schema_name]
        
        try:
            validated_data = schema(**data)
            return validated_data.dict()
        except ValidationError as e:
            raise ValidationException(str(e))

    def remove_schema(self, name: str):
        self._schemas.pop(name, None)

class ValidationException(Exception):
    pass
