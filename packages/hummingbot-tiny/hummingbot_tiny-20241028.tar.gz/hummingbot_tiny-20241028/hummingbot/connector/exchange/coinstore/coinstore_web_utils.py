from typing import Any, Dict, Optional
from email.utils import parsedate_to_datetime
import time

from hummingbot.connector.exchange.coinstore import coinstore_constants as CONSTANTS
from hummingbot.core.api_throttler.async_throttler import AsyncThrottler
from hummingbot.core.web_assistant.auth import AuthBase
from hummingbot.core.web_assistant.connections.data_types import RESTMethod
from hummingbot.core.web_assistant.rest_pre_processors import RESTPreProcessorBase
from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory


def public_rest_url(path_url: str, domain: str = CONSTANTS.REST_URL) -> str:
    """
    Creates a full URL for provided public REST endpoint
    :param path_url: a public REST endpoint
    :param domain: the Coinstore domain to connect to
    :return: the full URL to the endpoint
    """
    return domain + path_url


def private_rest_url(path_url: str, domain: str = CONSTANTS.REST_URL) -> str:
    """
    Creates a full URL for provided private REST endpoint
    :param path_url: a private REST endpoint
    :param domain: the Coinstore domain to connect to
    :return: the full URL to the endpoint
    """
    return domain + path_url


def build_api_factory(
    throttler: Optional[AsyncThrottler] = None,
    time_synchronizer: Optional[RESTPreProcessorBase] = None,
    auth: Optional[AuthBase] = None,
    domain: str = CONSTANTS.REST_URL,
) -> WebAssistantsFactory:
    """
    Builds an API factory configured for Coinstore
    :param throttler: to be used to limit request rates
    :param time_synchronizer: to be used to synchronize timestamps with the server
    :param auth: to be used to authenticate requests
    :param domain: to be used to connect to
    :return: an API factory
    """
    api_factory = WebAssistantsFactory(
        throttler=throttler, auth=auth, rest_pre_processors=[time_synchronizer] if time_synchronizer else None
    )
    return api_factory


def is_exchange_information_valid(exchange_info: Dict[str, Any]) -> bool:
    """
    Verifies if the exchange information response is valid
    :param exchange_info: the response from the exchange
    :return: True if the response is valid, False otherwise
    """
    return all(map(lambda x: x in exchange_info, ["code", "data"]))


def calculate_fee(price: str, amount: str, fee_rate: str) -> str:
    """
    Calculates the fee amount based on price, amount and fee rate
    :param price: the price of the trade
    :param amount: the amount of the trade
    :param fee_rate: the fee rate to apply
    :return: the fee amount
    """
    return str(float(price) * float(amount) * float(fee_rate))


async def get_current_server_time(
    throttler: AsyncThrottler,
    domain: str = CONSTANTS.REST_URL,
) -> float:
    """
    Gets the current time in milliseconds.
    Since Coinstore doesn't provide a server time endpoint, we use local time.
    :param throttler: not used, kept for interface compatibility
    :param domain: not used, kept for interface compatibility
    :return: current time in milliseconds
    """
    return float(time.time() * 1000)