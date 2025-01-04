from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import List, Literal, Optional, Union
from .base import BaseChartMetadata, BaseChartData, BaseChart, ChartType
from .misc import Color
from enum import Enum

class GradientStop(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    color: Color
    position: float = Field(ge=0, le=1, description="Position of the color stop (0-1)")
    opacity: float = Field(default=1.0, ge=0, le=1)

class GradientDirection(str, Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    DIAGONAL = "diagonal"
    RADIAL = "radial"

class BackgroundEffect(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    gradient_stops: List[GradientStop] = Field(min_length=2, max_length=4)
    direction: GradientDirection = Field(default=GradientDirection.VERTICAL)
    blur_radius: float = Field(default=0, ge=0, le=100, description="Blur effect radius in pixels")

class CounterChartMetadata(BaseChartMetadata):
    model_config = ConfigDict(extra='forbid')
    
    type: Literal[ChartType.COUNTER]
    text_color: Color = Field(default=Color("#000000"))
    background_color: Color = Field(default=Color("#FFFFFF"))
    background_effect: Optional[BackgroundEffect] = None
    prefix: Optional[str] = None
    postfix: Optional[str] = None
    value_color: Color = Field(default=Color("#000000"))
    prefix_color: Color = Field(default=Color("#000000"))
    postfix_color: Color = Field(default=Color("#000000"))

    @field_validator('prefix', 'postfix')
    def validate_affix(cls, v):
        if v is not None and len(v.strip()) == 0:
            raise ValueError("Prefix/postfix cannot be empty or just whitespace")
        return v

class CounterChartData(BaseChartData):
    model_config = ConfigDict(extra='forbid')
    
    data: float = Field(
        ...,
        description="The numeric value to display"
    )

class CounterChart(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    metadata: CounterChartMetadata
    data: CounterChartData

    @field_validator('data')
    def validate_value(cls, v):
        """Additional validation could be added here if needed"""
        return v