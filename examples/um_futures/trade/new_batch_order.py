#!/usr/bin/env python
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

um_futures_client = UMFutures(key=key, secret=secret)

params = [
    {
        "symbol": "BTCUSDT",
        "side": "BUY",
        "type": "LIMIT",
        "quantity": "0.001",
        "timeInForce": "GTC",
        "price": "10000.1",
    },
    {
        "symbol": "BTCUSDT",
        "side": "BUY",
        "type": "LIMIT",
        "quantity": "0.01",
        "timeInForce": "GTC",
        "price": "8000.1",
    },
]

try:
    response = um_futures_client.new_batch_order(params)
    logging.info(response)
except ClientError as error:
    logging.error(
        f"Found error. status: {error.status_code}, error code: {error.error_code}, error message: {error.error_message}"
    )
