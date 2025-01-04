import asyncio
import time
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from hummingbot.connector.exchange.coinstore import coinstore_constants as CONSTANTS
from hummingbot.connector.exchange.coinstore.coinstore_order_book import CoinstoreOrderBook
from hummingbot.connector.exchange.coinstore.coinstore_utils import convert_to_exchange_trading_pair, convert_to_exchange_trading_pair_for_ws, convert_from_exchange_trading_pair
from hummingbot.core.data_type.order_book_message import OrderBookMessage
from hummingbot.core.data_type.order_book_tracker_data_source import OrderBookTrackerDataSource
from hummingbot.core.web_assistant.connections.data_types import RESTMethod, WSJSONRequest
from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory
from hummingbot.core.web_assistant.ws_assistant import WSAssistant
from hummingbot.logger import HummingbotLogger

if TYPE_CHECKING:
    from hummingbot.connector.exchange.coinstore.coinstore_exchange import CoinstoreExchange

class CoinstoreAPIOrderBookDataSource(OrderBookTrackerDataSource):
    _logger: Optional[HummingbotLogger] = None

    def __init__(self,
                 trading_pairs: List[str],
                 connector: 'CoinstoreExchange',
                 api_factory: WebAssistantsFactory):
        super().__init__(trading_pairs)
        self._connector = connector
        self._trade_messages_queue_key = CONSTANTS.TRADE_EVENT_TYPE
        self._diff_messages_queue_key = CONSTANTS.DIFF_EVENT_TYPE
        self._api_factory = api_factory

   
    async def _request_order_book_snapshot(self, trading_pair: str) -> Dict[str, Any]:
        """
        Retrieves a copy of the full order book from the exchange, for a particular trading pair.

        :param trading_pair: the trading pair for which the order book will be retrieved

        :return: the response from the exchange (JSON dictionary)
        """
        params = {
            "depth": f"{CONSTANTS.ORDER_DEPTH_LEVEL}"  # You can adjust this value based on your needs
        }

        rest_assistant = await self._api_factory.get_rest_assistant()
        url = CONSTANTS.REST_URL + CONSTANTS.SNAPSHOT_PATH_URL + '/' + convert_to_exchange_trading_pair(trading_pair)
        data = await rest_assistant.execute_request(
            url=url,
            params=params,
            method=RESTMethod.GET,
            throttler_limit_id=CONSTANTS.SNAPSHOT_PATH_URL,
        )

        return data

    async def _order_book_snapshot(self, trading_pair: str) -> OrderBookMessage:
        """
        Get a snapshot of the order book from the exchange.
        
        :param trading_pair: The trading pair for which to get the order book snapshot
        :return: The order book message containing the snapshot
        """
        snapshot: Dict[str, Any] = await self._request_order_book_snapshot(trading_pair)
        snapshot_timestamp: int = int(time.time()) * 1000
        snapshot_msg: OrderBookMessage = CoinstoreOrderBook.snapshot_message_from_exchange(
            snapshot,
            snapshot_timestamp,
            metadata={"trading_pair": trading_pair}
        )
        return snapshot_msg

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

    async def _subscribe_channels(self, ws: WSAssistant):
        """
        Subscribes to the trade events and diff orders events through the provided websocket connection.
        
        :param ws: the websocket assistant used to connect to the exchange
        """
        try:
            trade_params = []
            depth_params = []
            depth_constant = CONSTANTS.ORDER_DEPTH_LEVEL

            for trading_pair in self._trading_pairs:
                # Convert trading pair to exchange format
                symbol = convert_to_exchange_trading_pair_for_ws(trading_pair)
                trade_params.append(f"{symbol}@trade")
                depth_params.append(f"{symbol}@depth@{depth_constant}")
                
            # Subscribe to trade channel
            trade_payload = {
                "op": "SUB",
                "channel": trade_params,
                "param": {
                    "size": 2
                }
            }
            trade_request = WSJSONRequest(payload=trade_payload)
            
            # Subscribe to order book channel
            depth_payload = {
                "op": "SUB",
                "channel": depth_params
            }
            depth_request = WSJSONRequest(payload=depth_payload)
            
            # Log subscription messages
            self.logger().info(f"Subscribing to public channels with trade payload: {trade_payload}")
            self.logger().info(f"Subscribing to public channels with depth payload: {depth_payload}")
            
            # Send subscription messages
            await ws.send(trade_request)
            await ws.send(depth_request)
            
            self.logger().info("Subscribed to public order book and trade channels...")
        except asyncio.CancelledError:
            raise
        except Exception:
            self.logger().error(
                "Unexpected error occurred subscribing to order book trading and delta streams...",
                exc_info=True
            )
            raise

    async def get_last_traded_prices(self,
                                   trading_pair: str,
                                   domain: Optional[str] = None) -> float:
        """
        Return the last traded price for the specified trading pair.
        
        :param trading_pair: trading pair to get the price for
        :param domain: which domain to get the prices from (optional)
        :return: Last traded price for the trading pair
        """
        rest_assistant = await self._api_factory.get_rest_assistant()
        
        try:
            symbol = convert_to_exchange_trading_pair(trading_pair)
            url = CONSTANTS.REST_URL + CONSTANTS.LATEST_TRADE_PATH_URL + '/' + symbol
            
            resp = await rest_assistant.execute_request(
                url=url,
                method=RESTMethod.GET,
                throttler_limit_id=CONSTANTS.LATEST_TRADE_PATH_URL
            )
            
            if resp and "data" in resp and len(resp["data"]) > 0:
                return float(resp["data"][0]["price"])
            else:
                self.logger().warning(f"No latest trade data found for {trading_pair}")
                return float(0)
                
        except Exception:
            self.logger().error(f"Error requesting trade price for {trading_pair}.", exc_info=True)
            return float(0)

    async def _parse_trade_message(self, raw_message: Dict[str, Any], message_queue: asyncio.Queue):
        """
        Parses a trade message and puts it to the trade messages queue
        :param raw_message: The raw message from the websocket
        :param message_queue: The queue to put the parsed message into
        """
        if isinstance(raw_message, OrderBookMessage):
            message_queue.put_nowait(raw_message)
            return
            
        self.logger().debug(f"Received trade message: {raw_message}")
        self.logger().info(f"Received trade message: {raw_message}")
        if raw_message.get("T") == "trade":
            if "data" in raw_message:  # Batch historical trades
                self.logger().info(f"Processing batch of {len(raw_message['data'])} historical trades")
                for trade_data in raw_message["data"]:
                    symbol = trade_data.get("symbol", "")
                    trading_pair = convert_from_exchange_trading_pair(symbol)
                    trade_message = CoinstoreOrderBook.trade_message_from_exchange(
                        trade_data,
                        metadata={"trading_pair": trading_pair}
                    )
                    message_queue.put_nowait(trade_message)
            else:  # Single real-time trade
                self.logger().debug("Processing single real-time trade")
                symbol = raw_message.get("symbol", "")
                trading_pair = convert_from_exchange_trading_pair(symbol)
                trade_message = CoinstoreOrderBook.trade_message_from_exchange(
                    raw_message,
                    metadata={"trading_pair": trading_pair}
                )
                message_queue.put_nowait(trade_message)
    
    def _channel_originating_message(self, event_message: Dict[str, Any]) -> str:
        """
        Determines the channel for the message based on its content.
        :param event_message: The message from the websocket
        :return: The channel key for the message
        """
        channel = ""
        if "T" in event_message:
            event_type = event_message.get("T", "")
            if event_type == "depth":
                channel = self._diff_messages_queue_key
            elif event_type == "trade":
                channel = self._trade_messages_queue_key
        return channel

    async def _parse_order_book_diff_message(self, raw_message: Dict[str, Any], message_queue: asyncio.Queue):
        """
        Parses an order book diff message and puts it to the order book messages queue
        :param raw_message: The raw message from the websocket
        :param message_queue: The queue to put the parsed message into
        """

        if isinstance(raw_message, OrderBookMessage):
            message_queue.put_nowait(raw_message)
            return
            
        self.logger().info(f"Received order message: {raw_message}")
        if "T" in raw_message and raw_message["T"] == "depth":
            symbol = raw_message.get("symbol", "")
            trading_pair = convert_from_exchange_trading_pair(symbol)

            timestamp = int(time.time() * 1000)  # we use current time as update time

            order_book_message: OrderBookMessage = CoinstoreOrderBook.diff_message_from_exchange(
                raw_message,
                timestamp,
                {"trading_pair": trading_pair}
            )
            message_queue.put_nowait(order_book_message)

    async def _process_websocket_messages(self, websocket_assistant: WSAssistant):
        """
        Handles and routes different websocket messages to appropriate handlers.
        """
        async for ws_response in websocket_assistant.iter_messages():
            try:
                data = ws_response.data
                message_type = data.get("T", "")
                
                # Only log non-empty messages
                if message_type:
                    self.logger().debug(f"Received WebSocket message: {data}")
                
                channel = self._channel_originating_message(data)
                if channel:
                    message_queue = self._message_queue[channel]
                    if message_type == "trade":
                        await self._parse_trade_message(data, message_queue)
                    elif message_type == "depth":
                        await self._parse_order_book_diff_message(data, message_queue)
            except Exception as e:
                self.logger().error(f"Error processing WebSocket message: {data}. Error: {str(e)}", exc_info=True)