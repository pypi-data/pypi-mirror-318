import MetaTrader5 as mt5

__all__ = ["get_account_balance", "get_account_credit_balance", "get_account_number", "get_account_name",
           "get_net_profit", "get_open_net_profit", "get_free_margin", "get_used_margin", "get_account_exposure"]


def get_account_balance():
    """Retrieve the account balance formatted as a string."""
    account_info = mt5.account_info()

    if account_info is None:
        raise RuntimeError("Failed to retrieve account information.")

    return f"{account_info.currency} {account_info.balance:.2f}"


def get_account_credit_balance():
    """Retrieve the account credit balance formatted as a string."""
    account_info = mt5.account_info()

    if account_info is None:
        raise RuntimeError("Failed to retrieve account information.")

    return f"{account_info.currency} {account_info.credit:.2f}"


def get_account_number():
    """Retrieve the account number and server information formatted as a string."""
    account_info = mt5.account_info()

    if account_info is None:
        raise RuntimeError("Failed to retrieve account information.")

    return f"{account_info.login} - {account_info.server}"


def get_account_name():
    """Retrieve the account name."""
    account_info = mt5.account_info()

    if account_info is None:
        raise RuntimeError("Failed to retrieve account information.")

    return account_info.name


def get_net_profit():
    """Calculate the total net profit from all positions."""
    account_info = mt5.account_info()

    if account_info is None:
        raise RuntimeError("Failed to retrieve account information.")

    positions = mt5.positions_get()
    trades_profit = sum(position.profit for position in positions if position.profit is not None)

    return f"{account_info.currency} {trades_profit:.2f}"


def get_open_net_profit():
    """Calculate the net profit from open positions."""
    account_info = mt5.account_info()

    if account_info is None:
        raise RuntimeError("Failed to retrieve account information.")

    positions = mt5.positions_get()
    trades_profit = round(
        sum(position.profit for position in positions if position.type in [0, 1] and position.profit is not None), 2)

    return f"{account_info.currency} {trades_profit:.2f}"


def get_free_margin():
    """Retrieve the free margin."""
    account_info = mt5.account_info()

    if account_info is None:
        raise RuntimeError("Failed to retrieve account information.")

    return account_info.margin_free


def get_used_margin():
    """Retrieve the used margin."""
    account_info = mt5.account_info()

    if account_info is None:
        raise RuntimeError("Failed to retrieve account information.")

    return account_info.margin_level


def get_account_exposure():
    """Calculate the total exposure of the account."""
    positions = mt5.positions_get()
    account_exposure = sum(position.volume for position in positions) if positions else 0.0

    return f"{account_exposure:.1f}"
