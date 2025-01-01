import pandas as pd

def read_feather_file(file_path, top_n = -1, date_col = 'date'):
    """read ohlcv feather file
    """
    df = pd.read_feather(file_path)
    df[date_col] = pd.to_datetime(df[date_col])
    if top_n > 0:
        df = df.head(top_n)
    return df

def merge_bars(df, timeframe):
    """
    example: merge_bars(df, '5min')
    :param df: 原始数据, 要求为DateTimeIndex,拥有open,high,low,close,volume列
    :param timeframe: 新的时间窗口，例如5T,3D,10H,5min,30s等，参考pandas.date_range
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