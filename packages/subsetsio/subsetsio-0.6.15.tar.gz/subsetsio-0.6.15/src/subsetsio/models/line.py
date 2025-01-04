from enum import Enum
from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import List, Literal, Optional, Union
from .time import DateType
from .misc import Color
from .base import BaseChartMetadata, BaseChartData, BaseChart, ChartType

class LineStyle(str, Enum):
    SOLID = "solid"
    DASHED = "dashed"
    DOTTED = "dotted"

class LineChartDatasetConfig(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    label: str = Field(..., min_length=1, max_length=100)
    line_style: LineStyle = Field(default=LineStyle.SOLID)
    color: Color = Field(default="#000000")
    point_size: int = Field(default=4, ge=2, le=10)

class LineChartAxisConfig(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    label: str = Field(..., min_length=1, max_length=100)
    show_grid: bool = Field(default=True)
    show_line: bool = Field(default=True)

class LineChartYAxisConfig(LineChartAxisConfig):
    min: Optional[float] = None
    max: Optional[float] = None
    log_scale: bool = Field(default=False)

class LineChartMetadata(BaseChartMetadata):
    model_config = ConfigDict(extra='forbid')
    
    type: Literal[ChartType.LINE]
    dataset_configs: List[LineChartDatasetConfig] = Field(..., min_length=1, max_length=8)
    x_axis: LineChartAxisConfig
    y_axis: LineChartYAxisConfig
    show_legend: bool = Field(default=True)
    connect_null_points: bool = Field(default=False)
    background_color: Color = Field(default="#FFFFFF")
    interpolation: Literal["linear", "smooth"] = Field(default="linear")
    stacked: bool = Field(default=False)

class LineChartData(BaseChartData):
    model_config = ConfigDict(extra='forbid')
    
    data: List[List[Union[DateType, float, None]]] = Field(
        ...,
        min_length=1,
        description="List of points, where each point is [date, value1, value2, ...]"
    )

    @field_validator('data')
    def validate_data_structure(cls, data):
        if not data:
            raise ValueError("Data cannot be empty")

        # Validate each row
        prev_date = None
        for i, row in enumerate(data):
            # Validate date
            date = row[0]
            if not isinstance(date, (str, DateType)):
                raise ValueError(f"First element of row {i} must be a date, got {type(date)}")
            
            # Check date ordering
            if prev_date is not None and date < prev_date:
                raise ValueError(f"Dates must be in ascending order, found {date} after {prev_date}")
            prev_date = date

            # Validate values
            for j, value in enumerate(row[1:], 1):
                if value is not None and not isinstance(value, (int, float)):
                    raise ValueError(f"Value at row {i}, column {j} must be a number or None")

        return data

class LineChart(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    metadata: LineChartMetadata
    data: LineChartData