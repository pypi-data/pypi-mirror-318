from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import List, Literal, Optional, Union
from .base import BaseChartMetadata, BaseChartData, BaseChart, ChartType
from .misc import Color

class MapChartMetadata(BaseChartMetadata):
    model_config = ConfigDict(extra='forbid')
    
    type: Literal[ChartType.MAP]
    low_value_color: Color = Field(default=Color("#FFFFFF"))
    high_value_color: Color = Field(default=Color("#00FF00"))

class MapChartData(BaseChartData):
    model_config = ConfigDict(extra='forbid')
    
    data: List[List[Union[str, float]]] = Field(
        ...,
        min_length=1,
        description="List of data points, where each point is [country_code, value]"
    )

    @field_validator('data')
    def validate_data_structure(cls, data):
        if not data:
            raise ValueError("Data cannot be empty")

        for i, point in enumerate(data):
            # Check row length
            if len(point) != 2:
                raise ValueError(f"Point {i} has {len(point)} values, expected 2 (country_code, value)")
            
            # Validate country code
            country_code = point[0]
            if not isinstance(country_code, str):
                raise ValueError(f"Country code at point {i} must be a string")
            if not (len(country_code) == 2 and country_code.isalpha() and country_code.isupper()):
                raise ValueError(f"Country code '{country_code}' must be a 2-letter uppercase code")

            # Validate value
            value = point[1]
            if not isinstance(value, (int, float)):
                raise ValueError(f"Value at point {i} must be a number, got {type(value)}")

        # Check for duplicate country codes
        country_codes = [point[0] for point in data]
        duplicates = {code for code in country_codes if country_codes.count(code) > 1}
        if duplicates:
            raise ValueError(f"Duplicate country codes found: {', '.join(duplicates)}")

        return data

class MapChart(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    metadata: MapChartMetadata
    data: MapChartData