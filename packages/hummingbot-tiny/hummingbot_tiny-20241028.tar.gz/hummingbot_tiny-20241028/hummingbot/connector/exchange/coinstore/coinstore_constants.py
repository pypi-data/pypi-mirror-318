from hummingbot.core.api_throttler.data_types import RateLimit
from hummingbot.core.data_type.in_flight_order import OrderState

DEFAULT_DOMAIN = ""

EXCHANGE_NAME = "coinstore"
REST_URL = "https://api.coinstore.com/api"
WSS_URL = "wss://ws.coinstore.com/s/ws"

# Public API endpoints or CoinStore exchange
SNAPSHOT_PATH_URL = "/v1/market/depth"
LATEST_TRADE_PATH_URL = "/v1/market/trade"
TICKER_PRICE_URL = "/v1/market/tickers"
EXCHANGE_INFO_PATH_URL = "/v2/public/config/spot/symbols"

# Private API endpoints or CoinStore exchange
ACCOUNTS_PATH_URL = "/spot/accountList"
ORDER_PATH_URL = "/trade/order/place"
CANCEL_ORDER_PATH_URL = "/trade/order/cancel"
TRADE_ORDER_ORDERINFO_PATH_URL = "trade/order/orderInfo"
TRADE_HISTORY_PATH_URL = "/trade/match/accountMatches"

# Not sure if the values here is true
ORDER_STATUS_PATH_URL = "/v2/trade/order/active"

WS_CHANNEL_SPOT_ENDPOINT_NAME = "spot_order"
WS_CHANNEL_BALANCE_ENDPOINT_NAME = "spot_asset"
 
# REST API Order States
ORDER_STATE = {
    "REJECTED": OrderState.FAILED,
    "SUBMITTING": OrderState.PENDING_CREATE,
    "SUBMITTED": OrderState.OPEN,
    "PARTIAL_FILLED": OrderState.PARTIALLY_FILLED,
    "CANCELING": OrderState.PENDING_CANCEL,
    "CANCELED": OrderState.CANCELED,
    "EXPIRED": OrderState.FAILED,
    "STOPPED": OrderState.CANCELED,
    "FILLED": OrderState.FILLED,
}

# WebSocket Order States (adjust these numbers based on Coinstore's WebSocket documentation)
WS_ORDER_STATE = {
    "SUBMITTED": OrderState.OPEN,           # SUBMITTED
    "PARTIAL_FILLED": OrderState.PARTIALLY_FILLED,  # PARTIAL_FILLED
    "FILLED": OrderState.FILLED,         # FILLED
    "CANCELED": OrderState.CANCELED,       # CANCELED
    "REJECTED": OrderState.FAILED,         # REJECTED/EXPIRED
    "CANCELING": OrderState.PENDING_CANCEL, # CANCELING
}
ORDER_DEPTH_LEVEL = 5

# Order types
ORDER_TYPE_LIMIT = "LIMIT"
ORDER_TYPE_MARKET = "MARKET"


# Sides
SIDE_BUY = "BUY"
SIDE_SELL = "SELL"

# Time in force
TIME_IN_FORCE_GTC = "GTC"  # Good till cancelled
TIME_IN_FORCE_IOC = "IOC"  # Immediate or cancel
TIME_IN_FORCE_FOK = "FOK"  # Fill or kill

# WebSocket
WSS_URL = "wss://ws.coinstore.com/s/ws"
HEARTBEAT_TIME_INTERVAL = 30.0
WS_CONNECTION_TIME_INTERVAL = 20

# WebSocket channels
DIFF_EVENT_TYPE = "depth"
TRADE_EVENT_TYPE = "trade"

# WebSocket Response Codes
WSS_HEARTBEAT_CODE = 0
WSS_TRADE_CODE = 1
WSS_DIFF_CODE = 2

# WebSocket subscription topics
WS_DEPTH_SUBSCRIPTION = "depth"
WS_TRADE_SUBSCRIPTION = "trade"
WS_ORDER_SUBSCRIPTION = "spot_order"
WS_BALANCE_SUBSCRIPTION = "spot_asset"

# Rate Limits
RATE_LIMITS = [
    # Pool Limits - 300 requests per 3 seconds for same IP
    RateLimit(limit_id=EXCHANGE_NAME, limit=100, time_interval=1),  # 300/3 = 100 per second
    # User Limits - 120 requests per 3 seconds for same user
    RateLimit(limit_id="USER", limit=40, time_interval=1),  # 120/3 = 40 per second
    # Public API
    RateLimit(limit_id=SNAPSHOT_PATH_URL, limit=40, time_interval=1),
    RateLimit(limit_id=LATEST_TRADE_PATH_URL, limit=40, time_interval=1),
    RateLimit(limit_id=TICKER_PRICE_URL, limit=40, time_interval=1),
    RateLimit(limit_id=EXCHANGE_INFO_PATH_URL, limit=40, time_interval=1),
    # Private API
    RateLimit(limit_id=ACCOUNTS_PATH_URL, limit=40, time_interval=1),
    RateLimit(limit_id=ORDER_PATH_URL, limit=40, time_interval=1),
    RateLimit(limit_id=CANCEL_ORDER_PATH_URL, limit=40, time_interval=1),
    RateLimit(limit_id=TRADE_ORDER_ORDERINFO_PATH_URL, limit=40, time_interval=1),
    RateLimit(limit_id=TRADE_HISTORY_PATH_URL, limit=40, time_interval=1),
    RateLimit(limit_id=ORDER_STATUS_PATH_URL, limit=40, time_interval=1),
]

MAX_ORDER_ID_LEN = 32
HBOT_ORDER_ID_PREFIX = "CS_"

TIMESTAMP_RELATED_ERROR_CODE = "-9" # There is no timestamp related error. hence placeholder
TIMESTAMP_RELATED_ERROR_MESSAGE = "-9"
ORDER_NOT_EXIST_ERROR_CODE = "3103"
ORDER_NOT_EXIST_MESSAGE = "Order not found or does not belong to the current account"
UNKNOWN_ORDER_ERROR_CODE = "3103"
UNKNOWN_ORDER_MESSAGE = "Unknown error has occurred"
