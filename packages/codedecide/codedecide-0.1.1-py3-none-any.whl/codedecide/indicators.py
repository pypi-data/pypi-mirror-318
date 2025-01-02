from dataclasses import dataclass

@dataclass
class IndicatorPlotConfig:
    col_name: str
    trace_name: str
    legend_group: str
    separate: bool