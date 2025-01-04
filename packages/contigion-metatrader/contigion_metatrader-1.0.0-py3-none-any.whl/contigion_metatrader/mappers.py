from MetaTrader5 import (ORDER_TYPE_BUY, ORDER_TYPE_SELL, TIMEFRAME_M1, TIMEFRAME_M5, TIMEFRAME_M15, TIMEFRAME_M30,
                         TIMEFRAME_H1, TIMEFRAME_H4, TIMEFRAME_D1, TIMEFRAME_W1, TIMEFRAME_MN1, symbol_info
                         )

TIMEFRAME_MAP = {
    'M1': TIMEFRAME_M1,
    'M5': TIMEFRAME_M5,
    'M15': TIMEFRAME_M15,
    'M30': TIMEFRAME_M30,
    'H1': TIMEFRAME_H1,
    'H4': TIMEFRAME_H4,
    'D1': TIMEFRAME_D1,
    'W1': TIMEFRAME_W1,
    'MN1': TIMEFRAME_MN1,
}

CLOSE_MAP = {
    ORDER_TYPE_BUY: ORDER_TYPE_SELL,
    ORDER_TYPE_SELL: ORDER_TYPE_BUY,
}

ACTION_MAP = {
    'buy': ORDER_TYPE_BUY,
    'sell': ORDER_TYPE_SELL,
}


def get_timeframe_map():
    return TIMEFRAME_MAP


def get_order_close_map():
    return CLOSE_MAP


def get_action_map():
    return ACTION_MAP


def get_market_price_map(position):
    """Retrieve market prices for the given position's symbol.

    Args:
        position (object): The position object from which to get the symbol.

    Returns:
        dict: A mapping of order types to current market prices.

    Raises:
        RuntimeError: If symbol information retrieval fails.
    """

    info = symbol_info(position.symbol)

    if info is None:
        raise RuntimeError(f"Failed to retrieve market information for symbol: {position.symbol}")

    return {
        ORDER_TYPE_BUY: info.bid,
        ORDER_TYPE_SELL: info.ask,
    }


def convert_action(action):
    return ACTION_MAP[action]


def convert_signal(data):
    """Convert 'buy' and 'sell' signals in the DataFrame to numerical values.

    Args:
        data (pd.DataFrame): The DataFrame containing the 'signal' column.

    Returns:
        pd.DataFrame: A new DataFrame with the 'signal' column converted.
    """
    result = data.copy(deep=True)
    result['signal'] = result['signal'].replace(get_action_map())
    return result
