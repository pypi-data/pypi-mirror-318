from enum import Enum
from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import List, Literal, Optional, Union, Dict
from .base import BaseChartMetadata, BaseChartData, BaseChart, ChartType

class ScatterplotMarkerStyle(str, Enum):
    CIRCLE = "circle"
    SQUARE = "square"
    TRIANGLE = "triangle"

class ScatterplotDatasetConfig(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    label: str = Field(..., min_length=1, max_length=100)
    marker_style: ScatterplotMarkerStyle = Field(default=ScatterplotMarkerStyle.CIRCLE)

class ScatterplotAxisConfig(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    label: str = Field(..., min_length=1, max_length=100)
    log_scale: bool = Field(default=False)
    show_grid: bool = Field(default=True)
    show_line: bool = Field(default=True)

class ScatterplotChartMetadata(BaseChartMetadata):
    model_config = ConfigDict(extra='forbid')
    
    type: Literal[ChartType.SCATTERPLOT]
    dataset_configs: List[ScatterplotDatasetConfig] = Field(
        ...,
        min_length=1
    )
    x_axis: ScatterplotAxisConfig
    y_axis: ScatterplotAxisConfig
    show_legend: bool = Field(default=True)
    correlation_coefficient_visible: bool = Field(default=False)

class ScatterplotChartData(BaseChartData):
    model_config = ConfigDict(extra='forbid')
    
    data: List[List[Union[str, float, None]]] = Field(
        ...,
        min_length=1,
        description="List of points where each point is [label, x, y]"
    )

    @field_validator('data')
    def validate_data_structure(cls, data):
        if not data:
            raise ValueError("Data cannot be empty")

        # Expected values per row: [label, x, y]
        expected_length = 3

        # Track points by label
        point_sets: Dict[str, int] = {}

        # Validate each row
        for i, row in enumerate(data):
            # Check row length
            if len(row) != expected_length:
                raise ValueError(f"Row {i} has {len(row)} values, expected {expected_length} (label, x, y)")
            
            # Validate label
            if not isinstance(row[0], str):
                raise ValueError(f"First element of row {i} must be a string label")
            
            # Track point for this label
            label = row[0]
            point_sets[label] = point_sets.get(label, 0) + 1

            # Validate x and y coordinates
            for j, value in enumerate(row[1:], 1):
                if value is not None and not isinstance(value, (int, float)):
                    raise ValueError(f"Value at row {i}, column {j} must be a number or None")

        return data

class ScatterplotChart(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    metadata: ScatterplotChartMetadata
    data: ScatterplotChartData

    @field_validator('data')
    def validate_datasets_match(cls, v, info):
        """Validate that data points exist for each configured dataset"""
        metadata = info.data.get('metadata')
        if not metadata:
            return v

        # Get configured dataset labels
        dataset_labels = {config.label for config in metadata.dataset_configs}

        # Get actual dataset labels from data
        data_labels = {row[0] for row in v.data}

        # Build error message for all validation issues
        errors = []
        
        # Check for missing datasets
        missing_datasets = dataset_labels - data_labels
        if missing_datasets:
            errors.append(f"Missing data points for datasets: {', '.join(missing_datasets)}")

        # Check for undefined datasets
        extra_datasets = data_labels - dataset_labels
        if extra_datasets:
            errors.append(f"Found data points for undefined datasets: {', '.join(extra_datasets)}")

        if errors:
            raise ValueError(". ".join(errors))

        return v

    @field_validator('data')
    def validate_log_scale_values(cls, v, info):
        """Validate values for log scale axes"""
        metadata = info.data.get('metadata')
        if not metadata:
            return v

        errors = []
        for i, row in enumerate(v.data):
            if metadata.x_axis.log_scale and row[1] is not None:
                if row[1] <= 0:
                    errors.append(f"X values must be positive when using log scale (row {i})")
                    
            if metadata.y_axis.log_scale and row[2] is not None:
                if row[2] <= 0:
                    errors.append(f"Y values must be positive when using log scale (row {i})")

        if errors:
            raise ValueError(". ".join(errors))

        return v