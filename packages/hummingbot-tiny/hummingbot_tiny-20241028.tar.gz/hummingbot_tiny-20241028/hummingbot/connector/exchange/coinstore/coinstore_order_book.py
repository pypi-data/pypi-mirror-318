from typing import Dict, Optional
import time
from typing import Any, Dict
from hummingbot.core.data_type.common import TradeType
from hummingbot.core.data_type.order_book import OrderBook
from hummingbot.core.data_type.order_book_message import (
    OrderBookMessage,
    OrderBookMessageType
)


class CoinstoreOrderBook(OrderBook):
    @classmethod
    def snapshot_message_from_exchange(cls,
                                     msg: Dict[str, any],
                                     timestamp: int,
                                     metadata: Optional[Dict] = None) -> OrderBookMessage:
        """
        Creates a snapshot message with the order book snapshot message
        :param msg: the response from the exchange when requesting the order book snapshot
        :param timestamp: the snapshot timestamp
        :param metadata: a dictionary with extra information to add to the snapshot data
        :return: a snapshot message with the snapshot information received from the exchange
        """
        data = msg.get("data", {})
        return OrderBookMessage(OrderBookMessageType.SNAPSHOT, {
            "trading_pair": data.get('symbol',''),
            "update_id": int(data.get("timestamp", int(timestamp * 1000))),  # Convert timestamp to milliseconds if API timestamp not available
            "bids": data.get("b", []),  # bids
            "asks": data.get("a", [])   # asks
        }, timestamp=timestamp)

    @classmethod
    def diff_message_from_exchange(cls,
                                 msg: Dict[str, any],
                                 timestamp: Optional[float] = None,
                                 metadata: Optional[Dict] = None) -> OrderBookMessage:
        """
        Creates a diff message with the changes in the order book received from the exchange
        :param msg: the changes in the order book
        :param timestamp: the timestamp of the difference
        :param metadata: a dictionary with extra information to add to the difference data
        :return: a diff message with the changes in the order book
        """
        if metadata:
            msg.update(metadata)
        return OrderBookMessage(OrderBookMessageType.DIFF, {
            "trading_pair": msg["trading_pair"],
            "update_id": msg['S'],  # Sequence number
            "bids": [[price, amount] for price, amount, _ in msg.get("b", [])],
            "asks": [[price, amount] for price, amount, _ in msg.get("a", [])]
        }, timestamp=timestamp * 1e-3)

    @classmethod
    def trade_message_from_exchange(cls,
                                  msg: Dict[str, Any],
                                  metadata: Optional[Dict] = None) -> OrderBookMessage:
        """
        Creates a trade message with the trade information received from the exchange
        :param msg: the trade event details sent by the exchange
        :param metadata: a dictionary with extra information to add to the trade message
        :return: a trade message with the details of the trade as provided by the exchange
        """
        if metadata is None:
            metadata = {}

        return OrderBookMessage(OrderBookMessageType.TRADE, {
            "trading_pair": metadata["trading_pair"],
            "trade_type": float(TradeType.BUY.value) if msg["takerSide"] == "BUY" else float(TradeType.SELL.value),
            "trade_id": msg["tradeId"],
            "update_id": msg["seq"],
            "price": float(msg["price"]),
            "amount": float(msg["volume"])
        }, timestamp=float(msg["time"])) 