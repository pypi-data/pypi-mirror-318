import pandas as pd
from MetaTrader5 import TIMEFRAME_M15, copy_rates_from_pos, symbols_get
from .mappers import get_timeframe_map


def get_market_data(symbol='USDJPY', timeframe=TIMEFRAME_M15, number_of_candles=500):
    """Retrieve market data for a given symbol and timeframe.

    Args:
        symbol (str): The trading symbol.
        timeframe (int): The timeframe value from MetaTrader.
        number_of_candles (int): The number of candles to retrieve.

    Returns:
        DataFrame: A DataFrame containing the market data.

    Raises:
        RuntimeError: If data retrieval fails.
    """
    rates = copy_rates_from_pos(symbol, timeframe, 0, number_of_candles)

    if rates is None:
        raise RuntimeError(f"Failed to retrieve data for {symbol}.")

    data = pd.DataFrame(rates)
    data['time'] = pd.to_datetime(data['time'], unit='s')

    # Remove the last row if it's an incomplete candle
    if not data.empty:
        data.drop(data.index[-1], inplace=True)

    return data[['time', 'open', 'high', 'low', 'close', 'tick_volume']]


def get_symbol_names():
    """Retrieve a list of available symbol names.

    Returns:
        list: A list of symbol names.

    Raises:
        RuntimeError: If symbols retrieval fails.
    """
    symbols = symbols_get()

    if symbols is None:
        raise RuntimeError("Failed to retrieve symbols.")

    return [symbol.name for symbol in symbols]


def get_timeframes():
    timeframes = ['M1', 'M5', 'M15', 'M30', 'H1', 'H4', 'D1', 'W1', 'MN1']

    return timeframes


def get_timeframe_value(timeframe):
    """Get the corresponding MetaTrader timeframe value.

    Args:
        timeframe (str): The timeframe string (e.g., 'M1').

    Returns:
        int: The corresponding timeframe value.

    Raises:
        KeyError: If the timeframe is not recognized.
    """
    timeframe_map = get_timeframe_map()

    if timeframe not in timeframe_map:
        raise KeyError(f"Unknown timeframe: {timeframe}")

    return timeframe_map[timeframe]
