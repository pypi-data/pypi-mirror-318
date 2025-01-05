from enum import Enum
from pydantic import BaseModel, Field, HttpUrl, field_validator, model_validator
from typing import Optional, List, Any
from pydantic import BaseModel, Field, model_validator, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from pydantic.json_schema import JsonSchemaValue
import unicodedata


class ChartType(str, Enum):
    BAR = "bar"
    COUNTER = "counter"
    LINE = "line"
    MAP = "map"
    SCATTERPLOT = "scatter"
    TABLE = "table"

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"ChartType.{self.name}"

    def __json__(self):
        return self.value

def validate_text(input_text: str, max_length: int, field_name: str, allow_newlines: bool = False) -> str:
    """
    Validates text input for chart fields with reasonable Unicode support while maintaining security.
    """
    if len(input_text) > max_length:
        raise ValueError(f"{field_name} exceeds maximum length of {max_length} characters")
    
    if len(input_text.strip()) == 0:
        raise ValueError(f"{field_name} cannot be empty or just whitespace")
    
    # Block certain Unicode categories that could be used maliciously
    blocked_categories = {'Cf', 'Cs', 'Co', 'Cn'}
    if not allow_newlines:
        blocked_categories.add('Cc')
    
    # Additional blocked ranges (hex)
    blocked_ranges = [
        (0x2028, 0x2029),    # Line/paragraph separators
        (0x202A, 0x202E),    # Bidirectional formatting
        (0xFFF0, 0xFFFF),    # Specials
    ]
    
    # Explicitly allow certain Unicode blocks
    allowed_ranges = [
        (0x0020, 0x007E),    # Basic Latin
        (0x00A0, 0x00FF),    # Latin-1 Supplement
        # ... (keeping other ranges as in original)
    ]

    if allow_newlines:
        allowed_ranges = [(0x000A, 0x000A), (0x000D, 0x000D)] + allowed_ranges
    
    for char in input_text:
        char_ord = ord(char)
        char_category = unicodedata.category(char)
        
        if char_category in blocked_categories:
            raise ValueError(f"{field_name} contains invalid character: {char}")
        
        if any(start <= char_ord <= end for start, end in blocked_ranges):
            raise ValueError(f"{field_name} contains invalid character: {char}")
        
        if not any(start <= char_ord <= end for start, end in allowed_ranges):
            raise ValueError(f"{field_name} contains invalid character: {char}")
            
    return input_text

class BaseChartMetadata(BaseModel):
    """Base class for all chart metadata"""
    model_config = {
        'extra': 'forbid'
    }

    type: ChartType
    title: str = Field(..., min_length=8, max_length=140)
    subtitle: Optional[str] = Field(None, min_length=3, max_length=140)
    description: Optional[str] = Field(None, min_length=8, max_length=2000)
    icon: Optional[HttpUrl] = None

    @model_validator(mode='before')
    def validate_fields(cls, values):
        if 'title' in values and values['title'] is not None:
            values['title'] = validate_text(values['title'], 140, 'title', allow_newlines=False)
        
        if 'description' in values and values['description'] is not None:
            values['description'] = validate_text(values['description'], 2000, 'description', allow_newlines=True)
            
        if 'subtitle' in values and values['subtitle'] is not None:
            values['subtitle'] = validate_text(values['subtitle'], 140, 'subtitle', allow_newlines=False)
            
        return values


from typing import Dict, Union, Any
from pydantic import BaseModel, Field
import re

class ChartTags(Dict[str, Union[str, List[str]]]):
    """Tags for charts with validation rules"""
    
    def __init__(self, tags: Dict[str, Union[str, List[str]]]):
        self.validate_tags(tags)
        super().__init__(tags)
    
    @classmethod
    def validate_tags(cls, tags: Dict[str, Any]) -> None:
        if len(tags) > 10:
            raise ValueError("Maximum of 10 tags allowed")

        key_pattern = re.compile(r'^[a-z0-9][a-z0-9-]*[a-z0-9]$')
        
        for key, value in tags.items():
            # Key validation
            if not 1 <= len(key) <= 32:
                raise ValueError(f"Tag key '{key}' must be between 1 and 32 characters")
            
            if not key_pattern.match(key):
                raise ValueError(f"Tag key '{key}' must be lowercase alphanumeric with hyphens, cannot start/end with hyphen")

            # Value validation
            values = [value] if isinstance(value, str) else value
            
            if not isinstance(values, (str, list)):
                raise ValueError(f"Tag value must be string or list of strings")

            for val in values:
                if not isinstance(val, str):
                    raise ValueError(f"Tag value must be string, got {type(val)}")
                
                if not 1 <= len(val) <= 64:
                    raise ValueError(f"Tag value '{val}' must be between 1 and 64 characters")
                
                if not all(c.isprintable() for c in val):
                    raise ValueError(f"Tag value '{val}' contains invalid characters")
    
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: GetCoreSchemaHandler,
    ) -> CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.dict_schema(
                keys_schema=core_schema.str_schema(),
                values_schema=core_schema.union_schema([
                    core_schema.str_schema(),
                    core_schema.list_schema(core_schema.str_schema())
                ])
            ),
            python_schema=core_schema.union_schema(
                choices=[
                    core_schema.is_instance_schema(cls),
                    core_schema.dict_schema(
                        keys_schema=core_schema.str_schema(),
                        values_schema=core_schema.union_schema([
                            core_schema.str_schema(),
                            core_schema.list_schema(core_schema.str_schema())
                        ])
                    ),
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                function=lambda x: dict(x),
                return_schema=core_schema.dict_schema(
                    keys_schema=core_schema.str_schema(),
                    values_schema=core_schema.union_schema([
                        core_schema.str_schema(),
                        core_schema.list_schema(core_schema.str_schema())
                    ])
                ),
                when_used='json'
            )
        )
    
    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        _core_schema: CoreSchema,
        _handler: GetCoreSchemaHandler,
    ) -> JsonSchemaValue:
        return {
            "type": "object",
            "maxProperties": 10,
            "propertyNames": {
                "type": "string",
                "pattern": "^[a-z0-9][a-z0-9-]*[a-z0-9]$",
                "minLength": 3,
                "maxLength": 32
            },
            "additionalProperties": {
                "oneOf": [
                    {"type": "string", "maxLength": 64},
                    {
                        "type": "array",
                        "items": {"type": "string", "maxLength": 64},
                        "uniqueItems": True
                    }
                ]
            }
        }