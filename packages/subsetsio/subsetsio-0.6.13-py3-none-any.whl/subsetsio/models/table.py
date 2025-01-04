from typing import List, Literal, Optional, Union
from pydantic import BaseModel, Field, ConfigDict, field_validator
from .base import BaseChartMetadata, BaseChartData, BaseChart, ChartType

class ColumnConfig(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    label: str = Field(..., min_length=1, max_length=50)
    align: str = Field("left", pattern="^(left|center|right)$")
    width: Optional[int] = None
    format: Optional[str] = None

class TableChartMetadata(BaseChartMetadata):
    model_config = ConfigDict(extra='forbid')
    
    type: Literal[ChartType.TABLE]
    column_configs: List[ColumnConfig] = Field(
        ...,
        min_length=2,
        description="Configuration for each column in the data array"
    )
    striped: bool = Field(default=True)
    hoverable: bool = Field(default=True)
    page_size: Optional[int] = Field(default=10, ge=1)
    sortable: bool = Field(default=True)

class TableChartData(BaseChartData):
    model_config = ConfigDict(extra='forbid')
    
    data: List[List[Union[str, int, float]]] = Field(
        ...,
        min_length=2,
        description="List of rows, where each row is [value1, value2, ...]"
    )

    @field_validator('data')
    def validate_data_structure(cls, data):
        if not data:
            raise ValueError("Data cannot be empty")

        # Check for consistent row lengths
        row_length = len(data[0])
        for i, row in enumerate(data):
            if len(row) != row_length:
                raise ValueError(f"Row {i} has {len(row)} values, expected {row_length} (must match first row)")

            # Validate value types
            for j, value in enumerate(row):
                if not isinstance(value, (str, int, float)):
                    raise ValueError(f"Value at row {i}, column {j} must be a string or number, got {type(value)}")

        return data

class TableChart(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    metadata: TableChartMetadata
    data: TableChartData

    @field_validator('data')
    def validate_column_count(cls, v, info):
        """Validate that the number of columns matches the column configs"""
        metadata = info.data.get('metadata')
        if not metadata:
            return v

        expected_columns = len(metadata.column_configs)
        actual_columns = len(v.data[0]) if v.data else 0

        if actual_columns != expected_columns:
            raise ValueError(
                f"Data has {actual_columns} columns but {expected_columns} column configs were provided"
            )

        return v