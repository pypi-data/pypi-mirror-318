from MetaTrader5 import positions_get, symbol_info, ORDER_TYPE_BUY, ORDER_TYPE_SELL
from .mappers import get_order_close_map, get_market_price_map
from .util.requests import (adjust_stop_loss_request, adjust_stops_request,
                            adjust_take_profit_request,
                            create_trade_request, execute_request)

__all__ = ["open_long_trade", "open_short_trade", "close_trade", "adjust_take_profit", "adjust_stop_loss",
           "adjust_stops"]


def open_long_trade(symbol, volume, stop_loss=0, take_profit=0, comment="Contigion Open Order"):
    """Place a long trade for the specified symbol.

    Args:
        symbol (str): The trading symbol.
        volume (float): The trade volume.
        stop_loss (float, optional): The stop loss in pips. Defaults to 0.
        take_profit (float, optional): The take profit in pips. Defaults to 0.
        comment (str, optional): Comment for the trade. Defaults to "PipsPy".

    Returns:
        result: The result of the order execution.

    Raises:
        ValueError: If the symbol is invalid or volume is non-positive.
    """
    info = symbol_info(symbol)

    if info is None:
        raise ValueError(f"Invalid symbol: {symbol}")

    point = info.point
    price = info.ask
    direction = ORDER_TYPE_BUY
    request = create_trade_request(direction, symbol, volume, price, comment)

    if stop_loss > 0:
        request['sl'] = price - (stop_loss * point)

    if take_profit > 0:
        request['tp'] = price + (take_profit * point)

    return execute_request(request)


def open_short_trade(symbol, volume, stop_loss=0, take_profit=0, comment="PipsPy Open Order"):
    """Place a short trade for the specified symbol.

    Args:
        symbol (str): The trading symbol.
        volume (float): The trade volume.
        stop_loss (float, optional): The stop loss in pips. Defaults to 0.
        take_profit (float, optional): The take profit in pips. Defaults to 0.
        comment (str, optional): Comment for the trade. Defaults to "PipsPy Open Order".

    Returns:
        result: The result of the order execution.

    Raises:
        ValueError: If the symbol is invalid or volume is non-positive.
    """
    info = symbol_info(symbol)

    if info is None:
        raise ValueError(f"Invalid symbol: {symbol}")

    point = info.point
    price = info.bid  # Use bid price for short trades
    direction = ORDER_TYPE_SELL
    request = create_trade_request(direction, symbol, volume, price, comment)

    if stop_loss > 0:
        request['sl'] = price + (stop_loss * point)

    if take_profit > 0:
        request['tp'] = price - (take_profit * point)

    return execute_request(request)


def close_trade(ticket):
    """Close the specified order by ticket.

    Args:
        ticket (int): The ticket number of the order to close.

    Returns:
        result: The result of the order execution, or an error message if the ticket does not exist.
    """
    positions = positions_get(ticket=ticket)

    if not positions:
        raise ValueError(f"Ticket does not exist: {ticket}")

    position = positions[0]

    order_close_map = get_order_close_map()
    market_price_map = get_market_price_map(position)

    direction = order_close_map[position.type]
    price = market_price_map[position.type]
    comment = 'Contigion Close Order'
    request = create_trade_request(direction, position.symbol, position.volume, price, comment)
    request['ticket'] = position.ticket

    return execute_request(request)


def adjust_take_profit(ticket, take_profit):
    """Adjust the take profit for a given trade ticket."""
    request = adjust_take_profit_request(ticket, take_profit)
    return execute_request(request)


def adjust_stop_loss(ticket, stop_loss):
    """Adjust the stop loss for a given trade ticket."""
    request = adjust_stop_loss_request(ticket, stop_loss)
    return execute_request(request)


def adjust_stops(ticket, take_profit, stop_loss):
    """Adjust the take profit and stop loss for a given trade ticket."""
    request = adjust_stops_request(ticket, take_profit, stop_loss)
    return execute_request(request)
