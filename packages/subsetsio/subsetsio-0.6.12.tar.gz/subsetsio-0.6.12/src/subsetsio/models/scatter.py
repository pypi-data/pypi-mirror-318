from enum import Enum
from pydantic import BaseModel, Field, field_validator
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
        min_length=1
    )
    x_axis: ScatterplotAxisConfig
    y_axis: ScatterplotAxisConfig
    show_legend: bool = Field(default=True)
    correlation_coefficient_visible: bool = Field(default=False)

class ScatterplotChart(ScatterplotChartMetadata):
    data: List[List[Union[str, float]]] = Field(
        ...,
        min_length=1,
        description="List of points where each point is [label, x, y]"
    )

    @field_validator('data')
    def validate_data_structure(cls, data, info):
        if not data:
            raise ValueError("Data cannot be empty")

        dataset_count = len(info.data.get('dataset_configs', []))
        if dataset_count < 1:
            raise ValueError("At least one dataset config is required")

        # Expected values per row: [label, x, y]
        expected_length = 3

        # Validate each row
        for i, row in enumerate(data):
            # Check row length
            if len(row) != expected_length:
                raise ValueError(f"Row {i} has {len(row)} values, expected {expected_length} (label, x, y)")
            
            # Validate label
            if not isinstance(row[0], str):
                raise ValueError(f"First element of row {i} must be a string label, got {type(row[0])}")

            # Validate x and y coordinates
            for j, value in enumerate(row[1:], 1):
                if value is not None and not isinstance(value, (int, float)):
                    raise ValueError(f"Value at row {i}, column {j} must be a number or None, got {type(value)}")

            # If using log scale, validate positive values
            if info.data.get('x_axis', {}).get('log_scale', False) and row[1] is not None:
                if row[1] <= 0:
                    raise ValueError(f"X values must be positive when using log scale (row {i})")
                    
            if info.data.get('y_axis', {}).get('log_scale', False) and row[2] is not None:
                if row[2] <= 0:
                    raise ValueError(f"Y values must be positive when using log scale (row {i})")

        # Group points by dataset to ensure we have data for each configured dataset
        point_sets = {}
        for row in data:
            label = row[0]
            point_sets[label] = point_sets.get(label, 0) + 1

        # Verify each dataset has points
        dataset_labels = {config.label for config in info.data.get('dataset_configs', [])}
        for label in dataset_labels:
            if label not in point_sets:
                raise ValueError(f"No data points found for dataset '{label}'")

        return data