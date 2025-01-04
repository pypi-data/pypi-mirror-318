import asyncio
from decimal import Decimal, InvalidOperation
from turtle import up
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple
import time
from bidict import bidict

from hummingbot.connector import exchange
from hummingbot.connector.constants import s_decimal_NaN
from hummingbot.connector.exchange.coinstore import (
    coinstore_constants as CONSTANTS,
    coinstore_utils,
    coinstore_web_utils as web_utils,
)
from hummingbot.connector.exchange.coinstore.coinstore_auth import CoinstoreAuth
from hummingbot.connector.exchange.coinstore.coinstore_api_order_book_data_source import CoinstoreAPIOrderBookDataSource
from hummingbot.connector.exchange.coinstore.coinstore_api_user_stream_data_source import CoinstoreAPIUserStreamDataSource
from hummingbot.connector.exchange.coinstore.coinstore_utils import (
    convert_to_exchange_trading_pair,
    convert_from_exchange_trading_pair
)
from hummingbot.connector.exchange_py_base import ExchangePyBase
from hummingbot.connector.trading_rule import TradingRule
from hummingbot.connector.utils import TradeFillOrderDetails, combine_to_hb_trading_pair
from hummingbot.core.data_type.common import OrderType, TradeType
from hummingbot.core.data_type.in_flight_order import InFlightOrder, OrderUpdate, TradeUpdate
from hummingbot.core.data_type.order_book_tracker_data_source import OrderBookTrackerDataSource
from hummingbot.core.data_type.trade_fee import DeductedFromReturnsTradeFee, TokenAmount, TradeFeeBase
from hummingbot.core.data_type.user_stream_tracker_data_source import UserStreamTrackerDataSource
from hummingbot.core.event.events import MarketEvent, OrderFilledEvent
from hummingbot.core.utils.async_utils import safe_gather
from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory
from hummingbot.core.network_iterator import NetworkStatus
from hummingbot.connector.time_synchronizer import TimeSynchronizer

if TYPE_CHECKING:
    from hummingbot.client.config.config_helpers import ClientConfigAdapter

class CoinstoreExchange(ExchangePyBase):
    UPDATE_ORDER_STATUS_MIN_INTERVAL = 10.0

    web_utils = web_utils

    def __init__(self,
                 client_config_map: "ClientConfigAdapter",
                 coinstore_api_key: str,
                 coinstore_secret_key: str,
                 trading_pairs: Optional[List[str]] = None,
                 trading_required: bool = True,
                 domain: str = CONSTANTS.REST_URL,
                 ):
        self.api_key = coinstore_api_key
        self.secret_key = coinstore_secret_key
        self._domain = domain
        self._trading_required = trading_required
        self._trading_pairs = trading_pairs
        self._last_trades_poll_coinstore_timestamp = 1.0
        
        super().__init__(client_config_map)
        
        # Initialize time synchronizer with local time
        self._time_synchronizer.add_time_offset_ms_sample(0.0)  # No offset needed since we're using local time
        
    @staticmethod
    def coinstore_order_type(order_type: OrderType) -> str:
        return order_type.name.upper()

    @staticmethod
    def to_hb_order_type(coinstore_type: str) -> OrderType:
        return OrderType[coinstore_type]

    @property
    def authenticator(self):
        return CoinstoreAuth(
            api_key=self.api_key,
            secret_key=self.secret_key,
            time_provider=self._time_synchronizer)

    @property
    def name(self) -> str:
        return "coinstore"

    @property
    def rate_limits_rules(self):
        return CONSTANTS.RATE_LIMITS

    @property
    def client_order_id_max_length(self):
        return CONSTANTS.MAX_ORDER_ID_LEN

    @property
    def client_order_id_prefix(self):
        return CONSTANTS.HBOT_ORDER_ID_PREFIX

    @property
    def trading_rules_request_path(self):
        return CONSTANTS.EXCHANGE_INFO_PATH_URL

    @property
    def trading_pairs_request_path(self):
        return CONSTANTS.EXCHANGE_INFO_PATH_URL

    @property
    def check_network_request_path(self):
        return self.trading_pairs_request_path

    @property
    def trading_pairs(self) -> List[str]:
        return self._trading_pairs if self._trading_pairs is not None else []

    @property
    def is_cancel_request_in_exchange_synchronous(self) -> bool:
        return True

    @property
    def is_trading_required(self) -> bool:
        return self._trading_required
    
    @property
    def domain(self) -> str:
        return self._domain

    def supported_order_types(self):
        return [OrderType.LIMIT, OrderType.MARKET]

    def _is_request_exception_related_to_time_synchronizer(self, request_exception: Exception):
        return str(CONSTANTS.TIMESTAMP_RELATED_ERROR_CODE) in str(
            request_exception
        ) and CONSTANTS.TIMESTAMP_RELATED_ERROR_MESSAGE in str(request_exception)

    def _is_order_not_found_during_status_update_error(self, status_update_exception: Exception) -> bool:
        if status_update_exception is None:
            return False
        return str(CONSTANTS.ORDER_NOT_EXIST_ERROR_CODE) in str(status_update_exception) and \
            CONSTANTS.ORDER_NOT_EXIST_MESSAGE in str(status_update_exception)

    def _is_order_not_found_during_cancelation_error(self, cancelation_exception: Exception) -> bool:
        return str(CONSTANTS.UNKNOWN_ORDER_ERROR_CODE) in str(
            cancelation_exception
        ) and CONSTANTS.UNKNOWN_ORDER_MESSAGE in str(cancelation_exception)

    def _create_web_assistants_factory(self) -> WebAssistantsFactory:
        return web_utils.build_api_factory(
            throttler=self._throttler,
            auth=self._auth)

    def _create_order_book_data_source(self) -> OrderBookTrackerDataSource:
        return CoinstoreAPIOrderBookDataSource(
            trading_pairs=self._trading_pairs,
            connector=self,
            api_factory=self._web_assistants_factory)

    def _create_user_stream_data_source(self) -> UserStreamTrackerDataSource:
        return CoinstoreAPIUserStreamDataSource(
            auth=self._auth,
            trading_pairs=self._trading_pairs,
            connector=self,
            api_factory=self._web_assistants_factory
        )
    
    def _get_fee(self,
                base_currency: str,
                quote_currency: str,
                order_type: OrderType,
                order_side: TradeType,
                amount: Decimal,
                price: Decimal = s_decimal_NaN,
                is_maker: Optional[bool] = None) -> TradeFeeBase:
        is_maker = order_type is OrderType.LIMIT_MAKER
        return DeductedFromReturnsTradeFee(percent=self.estimate_fee_pct(is_maker))

    def _get_poll_interval(self, timestamp: float) -> float:
        return 1.0

    async def _place_order(self,
                        order_id: str,
                        trading_pair: str,
                        amount: Decimal,
                        trade_type: TradeType,
                        order_type: OrderType,
                        price: Decimal,
                        **kwargs) -> Tuple[str, float]:
        """
        Places an order on Coinstore
        :param order_id: The client order ID
        :param trading_pair: The trading pair to place order for
        :param amount: The order amount
        :param trade_type: BUY or SELL
        :param order_type: LIMIT or MARKET
        :param price: The order price (for LIMIT orders)
        """
        order_result = None
        amount_str = f"{amount:f}"
        type_str = self.coinstore_order_type(order_type)
        side_str = CONSTANTS.SIDE_BUY if trade_type is TradeType.BUY else CONSTANTS.SIDE_SELL
        symbol = convert_to_exchange_trading_pair(trading_pair=trading_pair)
        timestamp = int(time.time()) * 1000
        api_params = {
            "symbol": symbol,
            "side": side_str,
            "ordQty": amount_str,
            "ordType": type_str,
            "clOrdId": order_id,
            "timestamp": timestamp
        }
        if order_type is OrderType.LIMIT:
            price_str = f"{price:f}"
            api_params["ordPrice"] = price_str
            api_params["timeInForce"] = CONSTANTS.TIME_IN_FORCE_GTC

        try:
            order_result = await self._api_post(
                path_url=CONSTANTS.ORDER_PATH_URL,
                data=api_params,
                is_auth_required=True)
            exchange_order_id = str(order_result["data"]["ordId"])
            return exchange_order_id, self.current_timestamp
        except Exception as e:
            self.logger().network(
                f"Error submitting {side_str} {type_str} order to Coinstore for "
                f"{amount} {trading_pair} "
                f"{price if order_type is OrderType.LIMIT else ''}."
                f"\nError: {str(e)}"
            )
            raise e

    async def _place_cancel(self, order_id: str, tracked_order: InFlightOrder):
        """
        Cancels an order on Coinstore
        :param order_id: The client_order_id of the order to cancel
        :param tracked_order: The InFlightOrder object to cancel
        """
        try:
            symbol = convert_to_exchange_trading_pair(tracked_order.trading_pair)
            exchange_order_id = tracked_order.exchange_order_id

            api_params = {
                "ordId": exchange_order_id,
                "symbol": symbol
            }
            self.logger().info(f"The api_params is: {api_params}")
            cancel_result = await self._api_post(
                path_url=CONSTANTS.CANCEL_ORDER_PATH_URL,
                data=api_params,
                is_auth_required=True
            )
            self.logger().info(f"Cancel order result: {cancel_result}")
            if cancel_result["data"]["state"] == "CANCELED":
                return True
            return False

        except Exception as e:
            self.logger().error(
                f"Failed to cancel order {order_id}: {str(e)}",
                exc_info=True,
                app_warning_msg=f"Failed to cancel the order {order_id} on Coinstore. "
                              f"Check API key and network connection."
            )
            raise e

    async def _format_trading_rules(self, exchange_info_dict: Dict[str, Any]) -> List[TradingRule]:
        """
        Format the trading rules response from the exchange into our internal trading rules format
        Rule looks like this:
        {
            "symbolId": 186,
            "symbolCode": "xrpusdt",  # Note: Coinstore returns lowercase symbols
            "tradeCurrencyCode": "xrp",
            "quoteCurrencyCode": "USDT",
            "openTrade": true,
            "tickSz": 4,
            "lotSz": 0,
            "minLmtPr": "0.0001",
            "minLmtSz": "1",
            "minMktVa": "1",
            "minMktSz": "1",
            "makerFee": "0.002",
            "takerFee": "0.002"
        }
        """
        trading_pair_rules = exchange_info_dict.get("data", [])
        self.logger().info(f"Got {len(trading_pair_rules)} trading pair rules from exchange")
        retval = []
        
        for rule in filter(coinstore_utils.is_exchange_information_valid, trading_pair_rules):
            try:
                symbol = rule.get("symbolCode", "").upper()  # Convert to uppercase
                if symbol:
                    # Convert base and quote separately to handle case sensitivity
                    base_asset = rule.get("tradeCurrencyCode", "").upper()
                    quote_asset = rule.get("quoteCurrencyCode", "").upper()
                    trading_pair = f"{base_asset}-{quote_asset}"
                    
                    self.logger().info(f"Processing trading rule for {symbol} -> {trading_pair}")

                    min_order_size = Decimal(str(rule.get("minLmtSz", "0")))
                    # Convert decimal places to actual increments
                    tick_size = int(rule.get("tickSz", 0))
                    lot_size = int(rule.get("lotSz", 0))
                    min_price_increment = Decimal("1") / Decimal(str(10 ** tick_size))
                    min_base_amount_increment = Decimal("1") / Decimal(str(10 ** lot_size))
                    min_notional = Decimal(str(rule.get("minMktVa", "0")))

                    self.logger().info(f"Created trading rule for {trading_pair}: "
                                     f"min_order_size={min_order_size}, "
                                     f"tick_size={tick_size}, lot_size={lot_size}, "
                                     f"min_price_increment={min_price_increment}, "
                                     f"min_base_amount_increment={min_base_amount_increment}, "
                                     f"min_notional={min_notional}")

                    retval.append(
                        TradingRule(
                            trading_pair=trading_pair,
                            min_order_size=min_order_size,
                            min_price_increment=min_price_increment,
                            min_base_amount_increment=min_base_amount_increment,
                            min_notional_size=min_notional,
                        ))

            except Exception:
                self.logger().error(f"Error parsing trading pair rule {rule}. Skipping.", exc_info=True)
        
        self.logger().info(f"Successfully created {len(retval)} trading rules")
        return retval

    async def _status_polling_loop_fetch_updates(self):
        await self._update_order_fills_from_trades()
        await super()._status_polling_loop_fetch_updates()
    
    async def _update_trading_fees(self):
        """
        Update fees information from the exchange
        """
        pass

    async def _user_stream_event_listener(self):
        """
        This functions runs in background continuously processing the events received from the exchange by the user
        stream data source. It keeps reading events from the queue until the task is interrupted.
        The events received are balance updates, order updates and trade events.
        """

        # TODO Add on private trade endpoint if there is any
        user_channels = [
            CONSTANTS.WS_CHANNEL_SPOT_ENDPOINT_NAME,
            CONSTANTS.WS_CHANNEL_BALANCE_ENDPOINT_NAME,
        ]

        async for event_message in self._iter_user_event_queue():
            try:
                channel_field_name = "T"
                channel = event_message.get(channel_field_name, None)
                data = event_message

                # CONTINUE FROM HERE
                if channel == CONSTANTS.WS_CHANNEL_SPOT_ENDPOINT_NAME:  # Order update
                    # Do a if else statement, for trade or update data
                    if data.get("delOrderIds", []) != []:
                        filled_order_state_machine = None

                        list_of_order_filled, list_of_order_cancelled = await self._check_if_order_is_filled_or_cancelled(data["delOrderIds"])
                        data['cancelOrderDetailsList'] = list_of_order_cancelled
                        if list_of_order_filled != []: 
                            data['delOrderIds'] = list_of_order_filled
                            list_of_trade_info_details = []
                            for order_data in list_of_order_filled:
                                trade_info = await self._check_trade_order_filled(order_data)
                                list_of_trade_info_details.append(trade_info)
                            
                            self._process_trade_message(list_of_trade_info_details)

                    self._process_order_message(data)
                elif channel == CONSTANTS.WS_CHANNEL_BALANCE_ENDPOINT_NAME:  # Balance update
                    self._process_balance_message_ws(data)

            except asyncio.CancelledError:
                raise
            except Exception:
                self.logger().error("Unexpected error in user stream listener loop.", exc_info=True)
                await self._sleep(5.0)
    
    async def _check_if_order_is_filled_or_cancelled(self, list_of_order_id: list):
        """
        order_info = {"data":
        {"baseCurrency":"XRP",
        "quoteCurrency":"USDT",
        "orderUpdateTime":1733558306000,
        "timestamp":1733558306000,
        "symbol":"XRPUSDT",
        "cumQty":"0",
        "ordId":1817767635321311,
        "clOrdId":"0",
        "timeInForce":"GTC",
        "accountId"::21032707,
        ordStatus":"CANCELED",
        "ordType":"LIMIT",
        "ordPrice":"0.6","ordQty":"5","cumAmt":"0","leavesQty":"5","avgPrice":"0"},
        "code":0}
        Checks the status of an order via REST API
        :param order_id: The exchange order ID
        :return: The order status response from the exchange
        """

        try:
            list_of_order_filled = []
            list_of_order_cancelled = []
            url = CONSTANTS.TRADE_ORDER_ORDERINFO_PATH_URL

            for order_id in list_of_order_id:
                params = {
                    "ordId": order_id
                }
                
                order_info = await self._api_get(
                        path_url=url,
                        params=params,
                    is_auth_required=True)

                self.logger().info(f"Order info: {order_info}")

                data = order_info.get("data", {})
                if data.get("ordStatus") == "FILLED":
                    self.logger().info(f"Order {order_id} is filled")
                    list_of_order_filled.append(data)
                elif data.get("ordStatus") == "CANCELED":
                    self.logger().info(f"Order {order_id} is cancelled")
                    list_of_order_cancelled.append(data)
            
            return list_of_order_filled, list_of_order_cancelled

        except Exception as e:
            self.logger().error(f"Error getting order status: {str(e)}", exc_info=True)
            return [], []
    
    async def _check_trade_order_filled(self, order_data) -> list:
        try:
            url = CONSTANTS.TRADE_HISTORY_PATH_URL

            order_id = order_data["ordId"]
            symbol = order_data["symbol"]

            params = {
                "symbol": symbol,
                "ordId": order_id,
            }
        
            trade_info = await self._api_get(
                        path_url=url,
                        params=params,
                    is_auth_required=True,
                    limit_id=CONSTANTS.TRADE_HISTORY_PATH_URL)
            self.logger().info(f"Order info: {trade_info}")

            data = trade_info.get("data", [])
            trade_data = data[0]
            
            # Not sure why the returned response has no baseCurrencyName, so i add in as symbol
            trade_data["symbol"] = symbol
            return trade_data
        
        except Exception as e:
            self.logger().error(f"Error getting trade order filled status: {str(e)}", exc_info=True)

    def _process_balance_message_ws(self, balance_update):
        try:
            asset_list = balance_update.get("assets", [])
            
            for asset_details in asset_list:
                asset_name = asset_details.get("symbol")
                if asset_name:
                    self._account_available_balances[asset_name] = Decimal(str(asset_details.get("usableAmount", 0)))
                    self._account_balances[asset_name] = Decimal(str(asset_details.get("usableAmount", 0))) + Decimal(
                        str(asset_details.get("frozenAmount", 0)))
        except Exception as e:
            self.logger().error(f"Error processing balance message: {str(e)}", exc_info=True)
    
    def extract_base_symbol(trading_pair: str) -> str:
        """
        Extracts the base symbol from a trading pair by removing known quote currencies.
        Example: 'BTCUSDT' -> 'BTC', 'XRPUSD' -> 'XRP'
        """
        quote_currencies = ['USDT', 'USD', 'USDC']
        
        # Sort by length in descending order to match longer strings first
        # This prevents 'USD' from matching before 'USDT'
        quote_currencies.sort(key=len, reverse=True)
        
        for quote in quote_currencies:
            if trading_pair.endswith(quote):
                return trading_pair[:-len(quote)]
        
        return trading_pair  # Return original if no quote currency found

    #TODO from trade update
    def _create_trade_update_with_order_fill_data(self, order_fill: Dict[str, Any], order: InFlightOrder):
        """
        Creates a trade update object from the trade fill data.
        :param order_fill: The trade fill data from the exchange
        :param order: The in-flight order associated with the trade fill
        :return: A TradeUpdate object

        :order_fill:
        {"id":456399686,"remainingQty":0,
        "matchRole":2,"feeCurrencyId":135,"acturalFeeRate":0.002,
        "role":-1,"accountId":21032707,"instrumentId":186,"baseCurrencyId":135,
        "quoteCurrencyId":30,"execQty":1,"orderState":50,"matchId":2244917470,
        "orderId":1818069597948211,"side":1,"execAmt":2.047,"selfDealingQty":0,
        "tradeId":51343060,"fee":0.002,"matchTime":1733846305,"seq":null,
        "taxRate":0,"tradeScale":null,"baseCurrencyName":null,
        "orderType":null}
        """
        try: 
            symbol = order_fill["symbol"]
            symbol = convert_to_exchange_trading_pair(symbol)
            fee_asset = self.extract_base_symbol(symbol)
            fee_amount = order_fill["fee"]

            fee = TradeFeeBase.new_spot_fee(
                fee_schema=self.trade_fee_schema(),
                trade_type=order.trade_type,
                percent_token=fee_asset,
                flat_fees=[TokenAmount(
                    amount=Decimal(str(fee_amount)), 
                    token=fee_asset 
                )]
            )

            trade_id = str(order_fill["tradeId"])
            volume_quantity = order_fill["execQty"]
            quote_amount = order_fill["execAmt"]
            fill_price = Decimal(str(order_fill["execAmt"])) / Decimal(str(order_fill["execQty"]))

            event_timestamp = order_fill["matchTime"] # Seems to be in seconds
            
            trade_update = TradeUpdate(
                trade_id=trade_id,
                client_order_id=order.client_order_id,
                exchange_order_id=order.exchange_order_id,
                trading_pair=order.trading_pair,
                fill_base_amount=Decimal(volume_quantity),
                fill_quote_amount=Decimal(quote_amount),
                fill_price=fill_price,
                fill_timestamp=event_timestamp,
                fee=fee
            )
            return trade_update

        except Exception as e:
            self.logger().error(f"Error creating trade update: {str(e)}", exc_info=True)
            raise
    
    # The idea is to take from delOrders
    def _process_trade_message(self, trade_details: list):
        for trade in trade_details:
            client_order_id = str(trade["clOrdId"]) # Otherwise can change to exchange order id, ordId
            # TODO Later check where is this track order from
            tracked_order = self._order_tracker.all_fillable_orders.get(client_order_id)
            if tracked_order is None:
                self.logger().debug(f"Ignoring trade message with id {client_order_id}: not in in_flight_orders.")
            else:
                trade_update = self._create_trade_update_with_order_fill_data(
                    order_fill=trade,
                    order=tracked_order)
                self._order_tracker.process_trade_update(trade_update)


    def _create_order_update_with_order_status_data(self, order_status: Dict[str, Any], order: InFlightOrder):
        """
        Creates an order update object from the order status data.
        :param order_status: The order status data from the exchange
        :param order: The in-flight order associated with the order status
        :return: An OrderUpdate object
        """
        # Same field name for both cancelledOrderDetails from API call and the incrOrderList websocket
        order_timestamp = int(int(order_status["timestamp"]) * 1e-3)
        exchange_order_id = str(order_status["ordId"])
        client_order_id = str(order_status["clOrdId"])
        state = order_status["ordStatus"]
    
        order_update = OrderUpdate(
            trading_pair=order.trading_pair,
            update_timestamp=order_timestamp,
            new_state=CONSTANTS.WS_ORDER_STATE[state],
            client_order_id=client_order_id,
            exchange_order_id=exchange_order_id,
        )
        return order_update
    
    def _process_order_list(self, order_list: List[Dict[str, Any]]):
         for order in order_list:
            client_order_id = order["clOrdId"]
            tracked_order = self._order_tracker.all_updatable_orders.get(client_order_id)
            if not tracked_order:
                self.logger().debug(f"Ignoring order message with id {client_order_id}: not in in_flight_orders.")
                continue  # Changed from return to continue to process remaining orders

            order_update = self._create_order_update_with_order_status_data(
                order_status=order, 
                order=tracked_order
            )
            self._order_tracker.process_order_update(order_update=order_update)

    def _process_order_message(self, raw_msg: Dict[str, Any]):
        if raw_msg["incrOrderList"]:
            incr_order_list = raw_msg["incrOrderList"]
            self._process_order_list(incr_order_list)

        if raw_msg["cancelOrderDetailsList"]:
            cancel_order_details_list = raw_msg["cancelOrderDetailsList"]
            self._process_order_list(cancel_order_details_list)

    async def _update_order_fills_from_trades(self):
        return

    async def _all_trade_updates_for_order(self, order: InFlightOrder) -> List[TradeUpdate]:
        trade_updates = []
        if order.exchange_order_id is not None:
            try:
                exchange_order_id = int(order.exchange_order_id)
                trading_pair = convert_to_exchange_trading_pair(order.trading_pair)
                params = {
                        "symbol": trading_pair,
                        "ordId": exchange_order_id,
                    }
                
                # self.logger().info(f'Parameters for trade updates for order: {params}')
                all_fills_response = await self._api_get(
                    path_url=CONSTANTS.TRADE_HISTORY_PATH_URL,
                    params=params,
                    is_auth_required=True,
                    limit_id=CONSTANTS.TRADE_HISTORY_PATH_URL
                )
                
                # Get the data array from the response
                trades_data = all_fills_response.get("data", [])
                self.logger().info(f"All fills response response: {all_fills_response}")
                self.logger().info(f"Trade history response: {trades_data}")

                for trade in trades_data:
                    try:
                        exchange_order_id = str(trade.get("orderId", ""))
                        fee_asset = self.extract_base_symbol(trading_pair)

                        # Safely get trade values with defaults
                        fee_amount = Decimal(str(trade.get("fee", "0")))
                        exec_qty = Decimal(str(trade.get("execQty", "0")))
                        exec_amt = Decimal(str(trade.get("execAmt", "0")))
                        
                        # Avoid division by zero
                        fill_price = exec_amt / exec_qty if exec_qty != 0 else Decimal("0")

                        fee = TradeFeeBase.new_spot_fee(
                            fee_schema=self.trade_fee_schema(),
                            trade_type=order.trade_type,
                            percent_token=fee_asset,
                            flat_fees=[TokenAmount(amount=fee_amount, token=fee_asset)]
                        )

                        trade_id = str(trade.get("tradeId", ""))

                        trade_update = TradeUpdate(
                            trade_id=trade_id,
                            client_order_id=order.client_order_id,
                            exchange_order_id=exchange_order_id,
                            trading_pair=order.trading_pair,
                            fee=fee,
                            fill_base_amount=exec_qty,
                            fill_quote_amount=exec_amt,
                            fill_price=fill_price,
                            fill_timestamp=trade.get("matchTime", int(time.time())),
                        )
                        trade_updates.append(trade_update)
                    except Exception as e:
                        self.logger().error(f"Error processing trade update: {str(e)}", exc_info=True)
                        continue

            except Exception as e:
                self.logger().error(f"Error fetching trades: {str(e)}", exc_info=True)

        return trade_updates
    
    async def _request_order_status(self, tracked_order: InFlightOrder) -> OrderUpdate:
        """
        Request order status from the exchange for the specified order.
        :param tracked_order: Order being tracked
        :return: OrderUpdate containing the updated order status
        """
        trading_pair = convert_to_exchange_trading_pair(tracked_order.trading_pair)
        
        # Prepare parameters for the request
        api_params = {
            "clOrdId": tracked_order.client_order_id,
            "symbol": trading_pair
        }
        self.logger().info(f"Requesting order status with params: {api_params}")

        updated_order_data_resp = await self._api_get(
            path_url=CONSTANTS.ORDER_STATUS_PATH_URL,
            params=api_params,
            is_auth_required=True,
            limit_id=CONSTANTS.ORDER_STATUS_PATH_URL
        )
        self.logger().info(f"Order status response: {updated_order_data_resp}")
        
        updated_order_data_list = updated_order_data_resp.get('data',[])
        
        if len(updated_order_data_list) > 1:
            self.logger().info(f"Order status response: {updated_order_data_resp}")
            self.logger().error(f"Error fetching order data. The length of order_data_list is {len(updated_order_data_list)}. Should be 1")
        
        updated_order_data = updated_order_data_list[0]

        # Safe dictionary access with error handling
        order_status = updated_order_data.get("ordStatus")
        if order_status not in CONSTANTS.ORDER_STATE:
            self.logger().warning(f"Unrecognized order status: {order_status}. Order: {tracked_order.client_order_id}")
            # Instead of returning None, return an order update with the current state
            return OrderUpdate(
                client_order_id=tracked_order.client_order_id,
                exchange_order_id=str(updated_order_data.get("ordId", "")),
                trading_pair=tracked_order.trading_pair,
                update_timestamp=int(updated_order_data.get("timestamp", int(time.time() * 1000))) * 1e-3,
                new_state=tracked_order.current_state  # Keep the current state instead of None
            )

        new_state = CONSTANTS.ORDER_STATE[order_status]
        
        order_update = OrderUpdate(
            client_order_id=tracked_order.client_order_id,
            exchange_order_id=str(updated_order_data.get("ordId", "")),
            trading_pair=tracked_order.trading_pair,
            update_timestamp=int(updated_order_data.get("timestamp", int(time.time() * 1000))) * 1e-3,
            new_state=new_state
        )
        self.logger().info(f'Successfully updated order: {order_update}')

        return order_update

    async def _get_last_traded_price(self, trading_pair: str) -> float:
        params = {
            "symbol": convert_to_exchange_trading_pair(trading_pair)
        }

        url = CONSTANTS.LATEST_TRADE_PATH_URL + '/' + symbol

        resp_json = await self._api_request(
            method=RESTMethod.GET,
            path_url=url,
            params=params
        )

        # Seems to return a data field with an array. Latest one being index 0
        latest_record = resp_json["data"][0]

        return float(latest_record["price"])
    
    def convert_balance_format(self, raw_balances: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert raw balance data from Coinstore format to standardized format.
        Example response:
        {
            'data': [
                {'uid': 9946912, 'accountId': 21032707, 'accountType': 1, 'currency': 'XRP', 'balance': '0', 'type': 4, 'typeName': 'FROZEN'},
                {'uid': 9946912, 'accountId': 21032707, 'accountType': 1, 'currency': 'XRP', 'balance': '0.998', 'type': 1, 'typeName': 'AVAILABLE'},
                {'uid': 9946912, 'accountId': 21032707, 'accountType': 1, 'currency': 'USDT', 'balance': '0', 'type': 4, 'typeName': 'FROZEN'},
                {'uid': 9946912, 'accountId': 21032707, 'accountType': 1, 'currency': 'USDT', 'balance': '2.953', 'type': 1, 'typeName': 'AVAILABLE'}
            ],
            'code': 0
        }
        
        :param raw_balances: Raw balance data from Coinstore API
        :return: Converted balance data in standardized format
        """
        try:
            self.logger().debug(f"Converting raw balances: {raw_balances}")
            
            # Initialize a dictionary to store processed balances
            processed_balances = {}
            
            # Get the list of balances from the response
            balance_data = raw_balances.get("data", [])
            self.logger().debug(f"Balance data from response: {balance_data}")
            
            if not isinstance(balance_data, list):
                self.logger().error(f"Expected list for balance_data, got {type(balance_data)}: {balance_data}")
                return {"balances": []}
            
            # Process each balance entry
            for entry in balance_data:
                self.logger().debug(f"Processing balance entry: {entry}")
                
                if not isinstance(entry, dict):
                    self.logger().warning(f"Skipping invalid entry (not a dict): {entry}")
                    continue
                    
                currency = entry.get("currency", "")
                balance = entry.get("balance", "0")
                type_name = entry.get("typeName", "")
                
                self.logger().debug(f"Entry details - currency: {currency}, balance: {balance}, type: {type_name}")
                
                if not currency:
                    self.logger().warning("Skipping entry with empty currency")
                    continue
                
                # Initialize currency entry if not exists
                if currency not in processed_balances:
                    processed_balances[currency] = {
                        "asset": currency,
                        "free": Decimal("0"),
                        "locked": Decimal("0")
                    }
                
                # Update the appropriate balance type
                try:
                    balance_dec = Decimal(str(balance))
                    if type_name == "AVAILABLE":
                        processed_balances[currency]["free"] += balance_dec
                    elif type_name == "FROZEN":
                        processed_balances[currency]["locked"] += balance_dec
                except (InvalidOperation, TypeError) as e:
                    self.logger().error(f"Error converting balance for {currency}: {str(e)}")
                    continue
            
            # Convert to list format
            result = {
                "balances": [
                    {
                        "asset": currency,
                        "free": str(details["free"]),
                        "locked": str(details["locked"])
                    }
                    for currency, details in processed_balances.items()
                ]
            }
            
            self.logger().debug(f"Final converted balances: {result}")
            return result
            
        except Exception as e:
            self.logger().error(f"Error in convert_balance_format: {str(e)}", exc_info=True)
            return {"balances": []}
    
    # Used in _format_trading_rules
    async def _make_trading_rules_request(self):
        exchange_info = await self._api_post(path_url=self.trading_rules_request_path,
                                             data={},
                                             is_auth_required=True)
        
        return exchange_info

    # Used in _initialize_trading_pair_symbols_from_exchange_info
    async def _make_trading_pairs_request(self) -> Any:
        """
        Get the list of trading pairs from the exchange.
        """
        try:
            exchange_info = await self._api_post(
                path_url=self.trading_pairs_request_path,
                data={},
                is_auth_required=False)
            
            self.logger().debug(f"Trading pairs response from exchange: {exchange_info}")
            return exchange_info
            
        except Exception as e:
            self.logger().error(f"Error getting trading pairs: {str(e)}", exc_info=True)
            raise

    async def _make_network_check_request(self):
        """
        This is used by the base class to make the network check request.
        We override it to use the trading pairs endpoint instead of a ping endpoint.
        """
        return await self._api_post(
            path_url=self.trading_pairs_request_path,
            data={},
            is_auth_required=False
        )

    def _initialize_trading_pair_symbols_from_exchange_info(self, exchange_info: Dict[str, Any]):
        """
        Initialize the mapping of exchange symbols to trading pairs.
        
        :param exchange_info: Exchange info dictionary from Coinstore API
        """
        try:
            exchange_info_data = exchange_info.get("data", [])
            self.logger().info(f"Initializing trading pairs. Exchange info from coinstore")
            self.logger().debug(f"Initializing trading pairs. Exchange info: {exchange_info_data}")
            
            mapping = bidict()
            
            for symbol_data in filter(coinstore_utils.is_exchange_information_valid, exchange_info_data):
                base_asset = symbol_data["tradeCurrencyCode"].upper()
                quote_asset = symbol_data["quoteCurrencyCode"].upper()
                
                trading_pair = combine_to_hb_trading_pair(base=base_asset, quote=quote_asset)
                exchange_symbol = symbol_data["symbolCode"].upper()
                
                # Can consider removing the logger info line
                # self.logger().info(f"Initialized trading pair {trading_pair} with exchange symbol {exchange_symbol}")
                mapping[exchange_symbol] = trading_pair
            
            self._set_trading_pair_symbol_map(mapping)
            
        except Exception as e:
            self.logger().error(f"Error initializing trading pair symbols: {str(e)}", exc_info=True)
            raise

    async def _update_balances(self):
        """
        Calls REST API to update total and available balances.
        """
        try:
            local_asset_names = set(self._account_balances.keys())
            remote_asset_names = set()

            account_info = await self._api_post(
                path_url=CONSTANTS.ACCOUNTS_PATH_URL,
                data={},  # Empty JSON body required by Coinstore API
                is_auth_required=True)
            
            self.logger().debug(f"Account info response: {account_info}")
            self.logger().info(f"Account info response: {account_info}")
            balances = self.convert_balance_format(account_info)
            self.logger().debug(f"Converted balances: {balances}")
            
            for balance_entry in balances["balances"]:
                asset_name = balance_entry["asset"]
                self._account_available_balances[asset_name] = Decimal(balance_entry["free"])
                self._account_balances[asset_name] = Decimal(balance_entry["free"]) + Decimal(balance_entry["locked"])
                remote_asset_names.add(asset_name)

            asset_names_to_remove = local_asset_names - remote_asset_names
            for asset_name in asset_names_to_remove:
                del self._account_available_balances[asset_name]
                del self._account_balances[asset_name]
                
        except Exception as e:
            self.logger().error(f"Could not update balances: {str(e)}", exc_info=True)
            raise

    async def check_network(self) -> NetworkStatus:
        """
        Checks if the exchange is online and available for trading.
        Uses the trading pairs endpoint as a ping since Coinstore doesn't have a dedicated ping endpoint.
        """
        try:
            await self._api_post(
                path_url=self.trading_pairs_request_path,
                data={},
                is_auth_required=False
            )
            return NetworkStatus.CONNECTED
        except Exception:
            return NetworkStatus.NOT_CONNECTED
