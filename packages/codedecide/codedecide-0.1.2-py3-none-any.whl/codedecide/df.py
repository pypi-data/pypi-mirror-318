import pandas as pd


def read_feather_file(file_path, top_n: int = -1, date_col: str = 'date'):
    """
    read ohlcv feather file
    """
    df = pd.read_feather(file_path)
    df[date_col] = pd.to_datetime(df[date_col])
    if top_n > 0:
        df = df.head(top_n)
    return df


def merge_bars(df: pd.DataFrame, timeframe: str):
    """
    example: merge_bars(df, '5min')
    :param df: origin data frame, DateTimeIndex and open,high,low,close,volume columns are requires
    :param timeframe: time frame，such as 5T,3D,10H,5min,30s, etc.，refer to pandas.date_range
    :return:
    """
    ohlc_dict = {
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum'
    }
    return df.resample(timeframe).agg(ohlc_dict)
