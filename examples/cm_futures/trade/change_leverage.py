#!/usr/bin/env python
import logging
from binance.cm_futures import CMFutures as Client
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret, base_url="https://dapi.binance.com")

try:
    response = client.change_leverage(symbol="BTCUSD_PERP", leverage=2, recvWindow=6000)
    logging.info(response)
except ClientError as error:
    logging.error(
        f"Found error. status: {error.status_code}, error code: {error.error_code}, error message: {error.error_message}"
    )
