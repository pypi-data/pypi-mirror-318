from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Literal, Optional, Union
from .base import BaseChart, ChartType

class ScatterplotMarkerStyle(str, Enum):
    CIRCLE = "circle"
    SQUARE = "square"
    TRIANGLE = "triangle"

class ScatterplotDatasetConfig(BaseModel):
    label: str = Field(..., min_length=1, max_length=100)
    marker_style: ScatterplotMarkerStyle = Field(default=ScatterplotMarkerStyle.CIRCLE)

class ScatterplotAxisConfig(BaseModel):
    label: str = Field(..., min_length=1, max_length=100)
    log_scale: bool = Field(default=False)
    show_grid: bool = Field(default=True)
    show_line: bool = Field(default=True)

class ScatterplotChartMetadata(BaseChart):
    type: Literal[ChartType.SCATTERPLOT]
    dataset_configs: List[ScatterplotDatasetConfig] = Field(
        ...,
        min_items=1
    )
    x_axis: ScatterplotAxisConfig
    y_axis: ScatterplotAxisConfig
    show_legend: bool = Field(default=True)
    correlation_coefficient_visible: bool = Field(default=False)

class ScatterplotChart(ScatterplotChartMetadata):
    data: List[List[Union[str, float]]] = Field(
        ...,
        min_items=1,
        description="List of points where each point is [label, x, y]"
    )