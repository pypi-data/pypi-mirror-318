from dataclasses import dataclass
from typing import Optional


@dataclass
class IndicatorPlotConfig:
    col_name: str
    trace_name: str
    legend_group: Optional[str] = None
    separate: bool = True
