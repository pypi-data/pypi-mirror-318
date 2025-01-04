import hashlib
import hmac
import json
from typing import Any, Dict, List
import time
from hummingbot.connector.time_synchronizer import TimeSynchronizer
from hummingbot.core.web_assistant.auth import AuthBase
from hummingbot.core.web_assistant.connections.data_types import RESTMethod, RESTRequest, WSRequest, WSJSONRequest
from urllib.parse import urlparse
import math
import logging
from hummingbot.logger import HummingbotLogger


class CoinstoreAuth(AuthBase):
    """
    Auth class required by Coinstore API
    """
    _logger = None
    
    @classmethod
    def logger(cls) -> HummingbotLogger:
        if cls._logger is None:
            cls._logger = logging.getLogger(__name__)
        return cls._logger
    
    def __init__(self, api_key: str, secret_key: str, time_provider: TimeSynchronizer):
        self.api_key = api_key
        self.secret_key = secret_key
        self.time_provider = time_provider

    async def rest_authenticate(self, request: RESTRequest) -> RESTRequest:
        """
        Adds the server time and the signature to the request, required for authenticated interactions.
        It also adds the required parameters in the request header.
        :param request: the request to be configured for authenticated interaction
        """
        expires = int(time.time() * 1000)
        expires_key = str(math.floor(expires / 30000))
        
        # First HMAC calculation using expires_key
        key = hmac.new(
            self.secret_key.encode("utf-8"),
            expires_key.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()
        
        # For GET requests with params, create query string for signature
        if request.method == RESTMethod.GET and request.params:
            # Convert params to query string format
            query_string = "&".join([f"{k}={v}" for k, v in request.params.items()])
            self.logger().debug(f"GET request query string for signature: {query_string}")
            signature_payload = query_string
        else:
            # For POST requests, use request body
            signature_payload = request.data if request.data else "{}"
            if isinstance(signature_payload, dict):
                signature_payload = json.dumps(signature_payload)
            
        # Log the payload being used for signature
        self.logger().debug(f"Payload for signature calculation: {signature_payload}")
            
        signature = hmac.new(
            key.encode("utf-8"),
            signature_payload.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        self.logger().debug(f"Generated signature: {signature}")

        # Prepare headers
        headers = {
            "X-CS-APIKEY": self.api_key,
            "X-CS-SIGN": signature,
            "X-CS-EXPIRES": str(expires),
            "Content-Type": "application/json",
            "Accept": "*/*",
            "exch-language": "en_US",
        }
        
        if request.headers is not None:
            headers.update(request.headers)
        request.headers = headers

        return request

    async def ws_authenticate(self, channel: List[str], params = {}) -> Dict[str, Any]:
        """
        Generates authentication payload for websocket connection
        :param channel: List of channels to authenticate for
        :return: Authentication payload
        """
        expires = int(time.time() * 1000)
        expires_key = str(math.floor(expires / 30000)).encode('utf-8')
        secret_key_bytes = self.secret_key.encode('utf-8')

        # First HMAC: Generate new secret key
        new_secret = hmac.new(
            secret_key_bytes,
            expires_key,
            digestmod=hashlib.sha256
        ).hexdigest()

        # Second HMAC: Generate final signature
        signature = hmac.new(
            new_secret.encode('utf-8'),
            str(expires).encode('utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()

        # Create authentication payload
        auth_payload = {
            "op": "login",
            "channel": channel,
            "auth": {
                "token": self.api_key,
                "type": "apikey",
                "expires": str(expires),
                "signature": signature
            },
            "params": params
        }

        return auth_payload

    async def get_ws_auth_payload(self, channel: List[str], params = {}) -> WSJSONRequest:
        """
        Creates a WSJSONRequest with authentication payload
        :param channel: List of channels to authenticate for
        :return: WSJSONRequest with auth payload
        """
        auth_payload = await self.ws_authenticate(channel, params)
        return WSJSONRequest(payload=auth_payload)