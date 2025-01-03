from .sdk import SubsetsClient, ChartDiff, ChartDiffer

# Base models and types
from .models.base import BaseChart, ChartType

# Bar chart models
from .models.bar import (
    BarPattern,
    BarChartDatasetConfig,
    BarChartAxisConfig,
    BarChartYAxisConfig,
    BarChartMetadata,
    BarChart
)

# Line chart models
from .models.line import (
    LineStyle,
    LineChartDatasetConfig,
    LineChartAxisConfig,
    LineChartYAxisConfig,
    LineChartMetadata,
    LineChart
)

# Map chart models
from .models.map import (
    MapChartMetadata,
    MapChart
)

# Counter chart models
from .models.counter import (
    GradientStop,
    GradientDirection,
    BackgroundEffect,
    CounterChartMetadata,
    CounterChart
)

# Scatterplot models
from .models.scatter import (
    ScatterplotMarkerStyle,
    ScatterplotDatasetConfig,
    ScatterplotAxisConfig,
    ScatterplotChartMetadata,
    ScatterplotChart
)

# Table models
from .models.table import (
    ColumnConfig,
    TableChartMetadata,
    TableChart
)

# Misc utilities and types
from .models.misc import Color

# Time/Date types
from .models.time import (
    ISODateTime,
    ISODate,
    ISOWeek,
    Month,
    Quarter,
    Year,
    DateType
)

# Chart parsing and type unions
from .models.chart import (
    Chart,
    ChartMetadata,
    parse_chart,
    parse_chart_metadata
)

# Update models
from .models.update import (
    BarChartMetadataUpdate,
    LineChartMetadataUpdate,
    MapChartMetadataUpdate,
    CounterChartMetadataUpdate,
    ScatterplotChartMetadataUpdate,
    TableChartMetadataUpdate,
    ChartUpdate
)

__version__ = "0.1.0"

__all__ = [
    # SDK
    "SubsetsClient",
    "ChartDiff",
    "ChartDiffer",
    
    # Base
    "BaseChart",
    "ChartType",
    
    # Bar Chart
    "BarPattern",
    "BarChartDatasetConfig",
    "BarChartAxisConfig",
    "BarChartYAxisConfig",
    "BarChartMetadata",
    "BarChart",
    
    # Line Chart
    "LineStyle",
    "LineChartDatasetConfig",
    "LineChartAxisConfig",
    "LineChartYAxisConfig",
    "LineChartMetadata",
    "LineChart",
    
    # Map Chart
    "MapChartMetadata",
    "MapChart",
    
    # Counter Chart
    "GradientStop",
    "GradientDirection",
    "BackgroundEffect",
    "CounterChartMetadata",
    "CounterChart",
    
    # Scatterplot
    "ScatterplotMarkerStyle",
    "ScatterplotDatasetConfig",
    "ScatterplotAxisConfig",
    "ScatterplotChartMetadata",
    "ScatterplotChart",
    
    # Table
    "ColumnConfig",
    "TableChartMetadata",
    "TableChart",
    
    # Misc
    "Color",
    
    # Time/Date
    "ISODateTime",
    "ISODate",
    "ISOWeek",
    "Month",
    "Quarter",
    "Year",
    "DateType",
    
    # Chart Types and Parsing
    "Chart",
    "ChartMetadata",
    "parse_chart",
    "parse_chart_metadata",
    
    # Updates
    "BarChartMetadataUpdate",
    "LineChartMetadataUpdate",
    "MapChartMetadataUpdate",
    "CounterChartMetadataUpdate",
    "ScatterplotChartMetadataUpdate",
    "TableChartMetadataUpdate",
    "ChartUpdate"
]