from datetime import datetime, timedelta
import MetaTrader5 as mt5

__all__ = ["get_trade_history", "get_profit_loss_history", "get_profit_loss_history_totals",
           "get_profit_loss_history_count"]


def get_trade_history(hours_ago=None, days_ago=None, year=None, is_close_history=False):
    """
    Retrieve trade history within a specified time range or year.

    Parameters:
        hours_ago (int, optional): Number of hours ago to start the history range.
        days_ago (int, optional): Number of days ago to start the history range.
        year (int, optional): Year to retrieve the history for (uses January 1st as the start date).
        is_close_history (bool, optional): If True, filters for close trade history; otherwise, filters for open trades.

    Returns:
        list: List of trades matching the criteria.

    Raises:
        ValueError: If none or multiple time parameters are provided simultaneously.
        RuntimeError: If trade history retrieval fails.
    """
    now = datetime.now()

    # Validate input parameters
    if not any([hours_ago, days_ago, year]):
        raise ValueError("At least one of 'hours_ago', 'days_ago', or 'year' must be provided.")
    if sum(param is not None for param in [hours_ago, days_ago, year]) > 1:
        raise ValueError("Only one of 'hours_ago', 'days_ago', or 'year' can be specified at a time.")

    # Determine start date
    if hours_ago:
        start_date = now - timedelta(hours=hours_ago)
    elif days_ago:
        start_date = now - timedelta(days=days_ago)
    else:
        start_date = datetime(year, 1, 1)

    end_date = now + timedelta(hours=3)
    trade_entry = 1 if is_close_history else 0
    trades = mt5.history_deals_get(start_date, end_date)

    if trades is None:
        raise RuntimeError("Failed to retrieve trade.")

    history = [trade for trade in trades if trade.entry == trade_entry]
    return history


def get_profit_loss_history(year=2025):
    """Get the profit and loss history."""
    trade_history = get_trade_history(year=year)
    profit_history = [trade.profit for trade in trade_history if trade.type in [0, 1] and trade.profit >= 0]
    loss_history = [abs(trade.profit) for trade in trade_history if trade.type in [0, 1] and trade.profit < 0]

    return profit_history, loss_history


def get_profit_loss_history_totals():
    """Calculate total profit and loss."""
    profit_history, loss_history = get_profit_loss_history()
    total_profit = round(sum(profit_history), 2)
    total_loss = round(sum(loss_history), 2)

    return f"{total_profit:.2f}", f"{total_loss:.2f}"


def get_profit_loss_history_count():
    """Count the number of profitable and losing trades."""
    profit_history, loss_history = get_profit_loss_history()
    profit_count = len(profit_history)
    loss_count = len(loss_history)

    return profit_count, loss_count
