#!/usr/bin/env python
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

um_futures_client = UMFutures(key=key, secret=secret)
try:
    response = um_futures_client.modify_isolated_position_margin(
        symbol="BTCUSDT", amount=100, type=1, recvWindow=6000
    )
    logging.info(response)
except ClientError as error:
    logging.error(
        f"Found error. status: {error.status_code}, error code: {error.error_code}, error message: {error.error_message}"
    )
