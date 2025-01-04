from typing import List, Literal, Optional, Union
from pydantic import BaseModel, Field, field_validator, model_validator
from enum import Enum
from .base import BaseChartMetadata, BaseChartData, BaseChart, ChartType
from .misc import Color

class BarPattern(str, Enum):
    SOLID = "solid"
    STRIPES = "stripes"
    DOTS = "dots"
    CROSSHATCH = "crosshatch"
    DIAGONAL = "diagonal"
    ZIGZAG = "zigzag"

class BarChartDatasetConfig(BaseModel):
    label: str = Field(..., min_length=1, max_length=100)
    color: Union[Color, List[Color]] = Field(default="#000000")
    pattern: Optional[BarPattern] = None

class BarChartAxisConfig(BaseModel):
    label: str = Field(..., min_length=1, max_length=100)
    show_grid: bool = Field(default=True)
    show_line: bool = Field(default=True)

class BarChartYAxisConfig(BarChartAxisConfig):
    min: Optional[float] = None
    max: Optional[float] = None
    log_scale: bool = Field(default=False)

class BarChartMetadata(BaseChartMetadata):
    type: Literal[ChartType.BAR]
    dataset_configs: List[BarChartDatasetConfig] = Field(..., min_length=1, max_length=10)
    x_axis: BarChartAxisConfig
    y_axis: BarChartYAxisConfig
    show_legend: bool = Field(default=True)
    background_color: Color = Field(default="#FFFFFF")
    bar_width: float = Field(default=0.8, ge=0.1, le=1.0)
    stack_mode: Literal["none", "stack", "stack_100"] = Field(default="none")
    horizontal: bool = Field(default=False)
    rounded_corners: bool = Field(default=False)

class BarChartData(BaseChartData):
    chart_type: Literal[ChartType.BAR] = ChartType.BAR
    data: List[List[Union[str, float]]] = Field(
        ...,
        min_length=1,
        description="List of points, where each point is [category, value1, value2, ...]"
    )

    @field_validator('data')
    def validate_data_structure(cls, data):
        # Track categories for uniqueness
        categories = set()
        
        # Validate each row
        for i, row in enumerate(data):
            # Validate category
            category = row[0]
            if not isinstance(category, str):
                raise ValueError(f"First element of row {i} must be a string category")
            
            if category in categories:
                raise ValueError(f"Duplicate category found: {category}")
            categories.add(category)

            # Validate values
            for j, value in enumerate(row[1:], 1):
                if value is not None and not isinstance(value, (int, float)):
                    raise ValueError(f"Value at row {i}, column {j} must be a number or None")

        return data

class BarChart(BaseChart):
    metadata: BarChartMetadata
    data: BarChartData

    @model_validator(mode='after')
    def validate_dataset_consistency(self):
        """Ensure number of values matches number of dataset configs"""
        if not self.data.data:
            return self
            
        expected_length = len(self.metadata.dataset_configs) + 1  # +1 for category
        for i, row in enumerate(self.data.data):
            if len(row) != expected_length:
                raise ValueError(f"Row {i} has {len(row)} values, expected {expected_length}")

        return self