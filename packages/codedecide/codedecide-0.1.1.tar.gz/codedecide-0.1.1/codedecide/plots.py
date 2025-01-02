import plotly.graph_objects as go
from plotly.subplots import make_subplots
from codedecide.indicators import IndicatorPlotConfig


def calc_row_number(with_volume: bool, indicators: list[IndicatorPlotConfig]):
    """calc subplot rows
    """
    rows = 2 if with_volume else 1
    if indicators is not None and len(indicators) > 0:
        for indicator in indicators:
            if indicator.separate:
                rows += 1
    return rows


def plot_ohlcv(df, with_volume: bool = True, with_rangeslider: bool = True,
               title: str = None, show_legend: bool = False,
               indicators: list[IndicatorPlotConfig] = None):
    fig = None
    real_title = "Price" if title is None else title
    row_number = calc_row_number(with_volume, indicators)
    has_indicator = indicators is not None and len(indicators) > 0
    # set initial height
    height = 500
    if row_number == 1:
        fig = go.Figure(data=[go.Candlestick(x=df.index,
                                             open=df['open'],
                                             high=df['high'],
                                             low=df['low'],
                                             close=df['close'])])
        # add indicators
        if has_indicator:
            for indicator in indicators:
                fig.add_trace(go.Scatter(x=df.index, y=df[indicator.col_name],
                                         legendgroup=indicator.legend_group,
                                         name=indicator.trace_name), row=1, col=1)
        fig.update_layout(xaxis_rangeslider_visible=with_rangeslider)
        fig.update_layout(title=real_title, height=height,
                          showlegend=show_legend)
    else:
        fig = make_subplots(rows=row_number, cols=1, shared_xaxes=True,
                            subplot_titles=(real_title, "Volume"), vertical_spacing=0.3)
        fig.add_trace(
            go.Candlestick(
                x=df.index, open=df['open'], high=df['high'], low=df['low'],
                close=df['close']), row=1, col=1)
        # add non-separate indicators in kline subplot
        if has_indicator:
            for indicator in indicators:
                if not indicator.separate:
                    fig.add_trace(go.Scatter(x=df.index, y=df[indicator.col_name],
                                             legendgroup=indicator.legend_group,
                                             name=indicator.trace_name), row=1, col=1)
        row_idx = 2
        if with_volume:
            # add volume plot
            height += 200
            fig.add_trace(
                go.Bar(x=df.index, y=df['volume'], name="Volume"), row=row_idx, col=1)
        # add separate indicators in left subplots
        if has_indicator:
            for indicator in indicators:
                if indicator.separate:
                    row_idx += 1
                    height += 200
                    fig.add_trace(go.Scatter(x=df.index, y=df[indicator.col_name],
                                             legendgroup=indicator.legend_group,
                                             name=indicator.trace_name), row=row_idx, col=1)
        fig.update_layout(xaxis_rangeslider_visible=with_rangeslider)
        fig.update_layout(title=title, height=height, showlegend=show_legend)
    fig.show()
