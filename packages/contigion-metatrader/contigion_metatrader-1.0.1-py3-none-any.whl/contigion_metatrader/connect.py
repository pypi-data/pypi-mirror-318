from MetaTrader5 import initialize, shutdown
from contigion_utils import print_success, print_warning, print_info

__all__ = ["connect", "disconnect"]


def connect():
    print_info("Connecting to MT5 ... \n")
    connected = initialize()
    retries = 0
    max_retries = 10

    while not connected:
        if retries > max_retries:
            raise RuntimeError("Failed to establish MetaTrader 5 connection. \n")

        print_warning(f"Unable to establish MetaTrader5 connection. Retrying ({retries} / {max_retries}) ... \n")
        connected = initialize()
        retries += 1

    print_success("Successfully connected to MetaTrader 5. \n")


def disconnect():
    """Shut down the MetaTrader 5 connection."""
    disconnected = shutdown()

    if not disconnected:
        raise RuntimeError("Failed to close MetaTrader 5 connection. \n")

    print_success("Disconnected from MetaTrader 5. \n")
