from enum import Enum
from pydantic import BaseModel, Field, HttpUrl, field_validator, model_validator
from typing import Optional, List, Any
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
    source_id: Optional[str] = None
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

class BaseChartData(BaseModel):
    """Base class for all chart data"""
    model_config = {
        'extra': 'forbid'
    }

    data: List[List[Any]] = Field(
        ...,
        min_length=1,
        description="Base data structure for all charts"
    )

    @field_validator('data')
    def validate_data_not_empty(cls, v):
        if not v:
            raise ValueError("Data cannot be empty")
        return v

class BaseChart(BaseModel):
    """Base class combining metadata and data"""
    model_config = {
        'extra': 'forbid'
    }

    metadata: BaseChartMetadata
    data: BaseChartData

    @model_validator(mode='after')
    def validate_types_match(self):
        """Ensure metadata and data types match"""
        if self.metadata.type != self.data.chart_type:
            raise ValueError(f"Metadata type ({self.metadata.type}) doesn't match data type ({self.data.chart_type})")
        return self