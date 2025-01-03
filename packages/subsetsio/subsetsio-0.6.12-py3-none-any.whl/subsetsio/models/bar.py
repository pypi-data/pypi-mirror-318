from enum import Enum
from pydantic import BaseModel, Field, field_validator
from typing import List, Literal, Optional, Union
from .misc import Color
from .base import BaseChart, ChartType

class BarPattern(str, Enum):
    SOLID = "solid"
    STRIPES = "stripes"
    DOTS = "dots"
    CROSSHATCH = "crosshatch"
    DIAGONAL = "diagonal"
    ZIGZAG = "zigzag"

class BarChartDatasetConfig(BaseModel):
    label: str = Field(..., min_length=1, max_length=100, description="Label for this dataset")
    color: Union[Color, List[Color]] = Field(default="#000000", description="Single color or array of colors for individual bars")
    pattern: Optional[BarPattern] = Field(None, description="Fill pattern for bars")

    @field_validator('color')
    def validate_colors_length(cls, v, values, **kwargs):
        if isinstance(v, list) and 'parent_data' in kwargs['field_info'].extra:
            data_length = len(kwargs['field_info'].extra['parent_data'])
            if len(v) != data_length:
                raise ValueError(f"Colors array length ({len(v)}) must match dataset length ({data_length})")
        return v

class BarChartAxisConfig(BaseModel):
    label: str = Field(..., min_length=1, max_length=100)
    show_grid: bool = Field(default=True)
    show_line: bool = Field(default=True)

class BarChartYAxisConfig(BarChartAxisConfig):
    min: Optional[float] = None
    max: Optional[float] = None
    log_scale: bool = Field(default=False)

class BarChartMetadata(BaseChart):
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


class BarChart(BarChartMetadata):
    data: List[List[Union[str, float]]] = Field(
        ...,
        min_length=1,
        description="List of points, where each point is [category, value1, value2, ...]"
    )

    @field_validator('data')
    def validate_data_structure(cls, data, info):
        if not data:
            raise ValueError("Data cannot be empty")

        expected_length = len(info.data.get('dataset_configs', [])) + 1  # +1 for category
        if expected_length < 2:
            raise ValueError("At least one dataset config is required")

        # Track categories for uniqueness and ordering
        categories = set()
        
        # Validate each row
        for i, row in enumerate(data):
            # Check row length
            if len(row) != expected_length:
                raise ValueError(f"Row {i} has {len(row)} values, expected {expected_length} (category + value for each dataset)")
            
            # Validate category
            category = row[0]
            if not isinstance(category, str):
                raise ValueError(f"First element of row {i} must be a string category, got {type(category)}")
            
            # Check category uniqueness
            if category in categories:
                raise ValueError(f"Duplicate category found: {category}")
            categories.add(category)

            # Validate values
            for j, value in enumerate(row[1:], 1):
                if value is not None and not isinstance(value, (int, float)):
                    raise ValueError(f"Value at row {i}, column {j} must be a number or None, got {type(value)}")
                if value is not None and info.data.get('stack_mode') in ['stack', 'stack_100'] and value < 0:
                    raise ValueError(f"Stacked bars cannot contain negative values (found in row {i}, column {j})")

        return data

    @field_validator('data')
    def validate_stack_100(cls, data, info):
        if info.data.get('stack_mode') == 'stack_100':
            for i, row in enumerate(data):
                values = [v for v in row[1:] if v is not None]
                if values:  # Only check if there are non-null values
                    total = sum(values)
                    if not (99.99 <= total <= 100.01):  # Allow for small floating point errors
                        raise ValueError(f"Values in row {i} sum to {total}, expected 100 for stack_100 mode")
        return data

    @field_validator('dataset_configs')
    def validate_colors_match_data(cls, v, info):
        if not info.data.get('data'):
            return v
        
        for config in v:
            if isinstance(config.color, list):
                if len(config.color) != len(info.data['data']):
                    raise ValueError(
                        f"Color array length ({len(config.color)}) must match number of categories ({len(info.data['data'])})"
                    )
        return v