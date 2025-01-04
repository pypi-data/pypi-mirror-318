import asyncio
import time
from typing import TYPE_CHECKING, List, Optional, Dict, Any

from hummingbot.connector.exchange.coinstore import coinstore_constants as CONSTANTS
from hummingbot.connector.exchange.coinstore.coinstore_auth import CoinstoreAuth
from hummingbot.core.data_type.user_stream_tracker_data_source import UserStreamTrackerDataSource
from hummingbot.core.web_assistant.connections.data_types import RESTMethod, WSJSONRequest
from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory
from hummingbot.core.web_assistant.ws_assistant import WSAssistant
from hummingbot.logger import HummingbotLogger

if TYPE_CHECKING:
    from hummingbot.connector.exchange.coinstore.coinstore_exchange import CoinstoreExchange


class CoinstoreAPIUserStreamDataSource(UserStreamTrackerDataSource):
    HEARTBEAT_TIME_INTERVAL = 30.0

    _logger: Optional[HummingbotLogger] = None

    def __init__(self,
                 auth: CoinstoreAuth,
                 trading_pairs: List[str],
                 connector: 'CoinstoreExchange',
                 api_factory: WebAssistantsFactory):
        super().__init__()
        self._auth: CoinstoreAuth = auth
        self._trading_pairs = trading_pairs
        self._connector = connector
        self._api_factory = api_factory

    async def _connected_websocket_assistant(self) -> WSAssistant:
        """
        Creates an instance of WSAssistant connected to the exchange
        """
        ws: WSAssistant = await self._api_factory.get_ws_assistant()
        await ws.connect(
            ws_url=CONSTANTS.WSS_URL,
            ping_timeout=CONSTANTS.HEARTBEAT_TIME_INTERVAL,
            message_timeout=CONSTANTS.HEARTBEAT_TIME_INTERVAL
        )
        return ws

    async def _subscribe_channels(self, websocket_assistant: WSAssistant):
        """
        Authenticates and subscribes to private channels
        """
        try:
            # First send login request
            login_payload = {
                "op": "LOGIN"
            }
            login_request = WSJSONRequest(payload=login_payload)
            self.logger().info(f"Sending login request with payload: {login_payload}")
            await websocket_assistant.send(login_request)

            # Subscribe to order channel
            order_payload = {
                "op": "SUB",
                "channel": ["spot_order"]
            }
            order_request = WSJSONRequest(payload=order_payload)
            self.logger().info(f"Subscribing to order channel with payload: {order_payload}")

            # Subscribe to balance channel
            balance_payload = {
                "op": "SUB",
                "channel": ["spot_asset"]
            }
            balance_request = WSJSONRequest(payload=balance_payload)
            self.logger().info(f"Subscribing to balance channel with payload: {balance_payload}")

            # Send subscription messages
            await websocket_assistant.send(order_request)
            await websocket_assistant.send(balance_request)

            self.logger().info("Subscribed to private order and balance channels...")
        except asyncio.CancelledError:
            raise
        except Exception:
            self.logger().exception("Unexpected error occurred subscribing to user streams...")
            raise

    async def _process_websocket_messages(self, websocket_assistant: WSAssistant, queue: asyncio.Queue):
        while True:
            try:
                async for ws_response in websocket_assistant.iter_messages():
                    data = ws_response.data
                    event_type = data.get("T", "")
                    
                    # Only log non-empty messages
                    if event_type:
                        self.logger().debug(f"Received WebSocket event: {data}")
                    
                    # Put the message in the queue for processing
                    queue.put_nowait(data)

                await asyncio.wait_for(
                    super()._process_websocket_messages(websocket_assistant=websocket_assistant, queue=queue),
                    timeout=CONSTANTS.WS_CONNECTION_TIME_INTERVAL
                )
            except asyncio.TimeoutError:
                epochMillis = int(time.time() * 1000)
                pong_message = {
                    "op": "pong",
                    "epochMillis": epochMillis
                }
                ping_request = WSJSONRequest(payload=pong_message)
                self.logger().debug(f"Sending pong message: {pong_message}")
                await websocket_assistant.send(ping_request)