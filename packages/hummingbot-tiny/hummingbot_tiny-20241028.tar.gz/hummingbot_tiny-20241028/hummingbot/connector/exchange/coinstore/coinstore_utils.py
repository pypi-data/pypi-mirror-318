from typing import Any, Dict, Optional

from hummingbot.core.api_throttler.data_types import RateLimit
from hummingbot.core.data_type.trade_fee import TradeFeeSchema
from pydantic import Field, SecretStr
from hummingbot.client.config.config_data_types import BaseConnectorConfigMap, ClientFieldData
from decimal import Decimal

CENTRALIZED = True
EXAMPLE_PAIR = "BTC-USDT"

DEFAULT_FEES = TradeFeeSchema(
    maker_percent_fee_decimal=Decimal("0.002"),
    taker_percent_fee_decimal=Decimal("0.002"),
    buy_percent_fee_deducted_from_returns=True
)

def convert_to_exchange_trading_pair(trading_pair: str) -> str:
    """
    Converts a trading pair string to the format expected by the Coinstore exchange.
    Removes any hyphens or underscores and converts to uppercase.
    
    Example:
        "BTC-USDT" -> "BTCUSDT"
        "ETH_USDT" -> "ETHUSDT"
    
    :param trading_pair: The trading pair to convert
    :return: The converted trading pair string
    """
    return trading_pair.replace("-", "").replace("_", "").upper()

def convert_to_exchange_trading_pair_for_ws(trading_pair: str) -> str:
    """
    Converts a trading pair string to the format expected by the Coinstore exchange.
    Removes any hyphens or underscores and converts to uppercase.
    
    Example:
        "BTC-USDT" -> "BTCUSDT"
        "ETH_USDT" -> "ETHUSDT"
    
    :param trading_pair: The trading pair to convert
    :return: The converted trading pair string
    """
    return trading_pair.replace("-", "").replace("_", "").lower()

def convert_from_exchange_trading_pair(exchange_trading_pair: str) -> str:
    """
    Converts an exchange trading pair (e.g. BTCUSDT) to hummingbot format (e.g. BTC-USDT)
    """
    # Known quote assets in order of priority
    known_quote_assets = ["USDT", "BTC", "ETH", "USD"]
    
    for quote in known_quote_assets:
        if exchange_trading_pair.endswith(quote):
            base = exchange_trading_pair[:-len(quote)]
            return f"{base}-{quote}"
    
    # If no known quote asset is found, try to split in the middle
    mid = len(exchange_trading_pair) // 2
    return f"{exchange_trading_pair[:mid]}-{exchange_trading_pair[mid:]}"

def is_exchange_information_valid(exchange_info: Dict[str, Any]) -> bool:
    """
    Verifies if a trading pair is enabled to operate with based on its exchange information
    
    :param exchange_info: Dictionary with trading pair information from Coinstore API
    :return: True if the trading pair is enabled for trading, False otherwise
    """
    return exchange_info.get("openTrade", False) is True # Adjusted based on Coinstore's API response

class CoinstoreConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="coinstore", const=True, client_data=None)
    coinstore_api_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Coinstore API key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )
    coinstore_secret_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Coinstore secret key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )

    class Config:
        title = "coinstore"

KEYS = CoinstoreConfigMap.construct()