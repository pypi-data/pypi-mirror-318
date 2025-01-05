from typing import Final

# Metadata
__version__: Final[str] 
__author__: Final[str] 

# Timeframes
TIMEFRAME_M1: Final[int] 
TIMEFRAME_M2: Final[int] 
TIMEFRAME_M3: Final[int] 
TIMEFRAME_M4: Final[int] 
TIMEFRAME_M5: Final[int] 
TIMEFRAME_M6: Final[int] 
TIMEFRAME_M10: Final[int] 
TIMEFRAME_M12: Final[int] 
TIMEFRAME_M15: Final[int] 
TIMEFRAME_M20: Final[int] 
TIMEFRAME_M30: Final[int] 
TIMEFRAME_H1: Final[int] 
TIMEFRAME_H2: Final[int] 
TIMEFRAME_H3: Final[int] 
TIMEFRAME_H4: Final[int] 
TIMEFRAME_H6: Final[int] 
TIMEFRAME_H8: Final[int] 
TIMEFRAME_H12: Final[int] 
TIMEFRAME_D1: Final[int] 
TIMEFRAME_W1: Final[int] 
TIMEFRAME_MN1: Final[int]

# Tick copy flags
COPY_TICKS_ALL: Final[int] 
COPY_TICKS_INFO: Final[int] 
COPY_TICKS_TRADE: Final[int]

# Tick flags
TICK_FLAG_BID: Final[int] 
TICK_FLAG_ASK: Final[int] 
TICK_FLAG_LAST: Final[int] 
TICK_FLAG_VOLUME: Final[int] 
TICK_FLAG_BUY: Final[int] 
TICK_FLAG_SELL: Final[int] 

# Position type
POSITION_TYPE_BUY: Final[int] 
POSITION_TYPE_SELL: Final[int] 

# Position reason
POSITION_REASON_CLIENT: Final[int] 
POSITION_REASON_MOBILE: Final[int] 
POSITION_REASON_WEB: Final[int] 
POSITION_REASON_EXPERT: Final[int] 

# Order types
ORDER_TYPE_BUY: Final[int] 
ORDER_TYPE_SELL: Final[int] 
ORDER_TYPE_BUY_LIMIT: Final[int] 
ORDER_TYPE_SELL_LIMIT: Final[int] 
ORDER_TYPE_BUY_STOP: Final[int] 
ORDER_TYPE_SELL_STOP: Final[int] 
ORDER_TYPE_BUY_STOP_LIMIT: Final[int] 
ORDER_TYPE_SELL_STOP_LIMIT: Final[int] 
ORDER_TYPE_CLOSE_BY: Final[int] 

# Order state
ORDER_STATE_STARTED: Final[int] 
ORDER_STATE_PLACED: Final[int] 
ORDER_STATE_CANCELED: Final[int] 
ORDER_STATE_PARTIAL: Final[int] 
ORDER_STATE_FILLED: Final[int] 
ORDER_STATE_REJECTED: Final[int] 
ORDER_STATE_EXPIRED: Final[int] 
ORDER_STATE_REQUEST_ADD: Final[int] 
ORDER_STATE_REQUEST_MODIFY: Final[int] 
ORDER_STATE_REQUEST_CANCEL: Final[int] 

# Order filling
ORDER_FILLING_FOK: Final[int] 
ORDER_FILLING_IOC: Final[int] 
ORDER_FILLING_RETURN: Final[int] 
ORDER_FILLING_BOC: Final[int] 

# Order time
ORDER_TIME_GTC: Final[int] 
ORDER_TIME_DAY: Final[int] 
ORDER_TIME_SPECIFIED: Final[int] 
ORDER_TIME_SPECIFIED_DAY: Final[int] 

# Order reason
ORDER_REASON_CLIENT: Final[int] 
ORDER_REASON_MOBILE: Final[int] 
ORDER_REASON_WEB: Final[int] 
ORDER_REASON_EXPERT: Final[int] 
ORDER_REASON_SL: Final[int] 
ORDER_REASON_TP: Final[int] 
ORDER_REASON_SO: Final[int] 

# Deal types
DEAL_TYPE_BUY: Final[int] 
DEAL_TYPE_SELL: Final[int] 
DEAL_TYPE_BALANCE: Final[int] 
DEAL_TYPE_CREDIT: Final[int] 
DEAL_TYPE_CHARGE: Final[int] 
DEAL_TYPE_CORRECTION: Final[int] 
DEAL_TYPE_BONUS: Final[int] 
DEAL_TYPE_COMMISSION: Final[int] 
DEAL_TYPE_COMMISSION_DAILY: Final[int] 
DEAL_TYPE_COMMISSION_MONTHLY: Final[int] 
DEAL_TYPE_COMMISSION_AGENT_DAILY: Final[int] 

DEAL_TYPE_COMMISSION_AGENT_MONTHLY: Final[int] 

DEAL_TYPE_INTEREST: Final[int] 

DEAL_TYPE_BUY_CANCELED: Final[int] 

DEAL_TYPE_SELL_CANCELED: Final[int] 

DEAL_DIVIDEND: Final[int] 

DEAL_DIVIDEND_FRANKED: Final[int] 

DEAL_TAX: Final[int] 


# Deal entry
DEAL_ENTRY_IN: Final[int] 
DEAL_ENTRY_OUT: Final[int] 
DEAL_ENTRY_INOUT: Final[int] 
DEAL_ENTRY_OUT_BY: Final[int] 

# Deal reason
DEAL_REASON_CLIENT: Final[int] 
DEAL_REASON_MOBILE: Final[int] 
DEAL_REASON_WEB: Final[int] 
DEAL_REASON_EXPERT: Final[int] 
DEAL_REASON_SL: Final[int] 
DEAL_REASON_TP: Final[int] 
DEAL_REASON_SO: Final[int] 
DEAL_REASON_ROLLOVER: Final[int] 
DEAL_REASON_VMARGIN: Final[int] 
DEAL_REASON_SPLIT: Final[int] 

# Trade actions
TRADE_ACTION_DEAL: Final[int] 
TRADE_ACTION_PENDING: Final[int] 
TRADE_ACTION_SLTP: Final[int] 
TRADE_ACTION_MODIFY: Final[int] 
TRADE_ACTION_REMOVE: Final[int] 
TRADE_ACTION_CLOSE_BY: Final[int] 

# Symbol chart mode
SYMBOL_CHART_MODE_BID: Final[int] 
SYMBOL_CHART_MODE_LAST: Final[int] 

# Symbol calc mode
SYMBOL_CALC_MODE_FOREX: Final[int] 
SYMBOL_CALC_MODE_FUTURES: Final[int] 
SYMBOL_CALC_MODE_CFD: Final[int] 
SYMBOL_CALC_MODE_CFDINDEX: Final[int] 
SYMBOL_CALC_MODE_CFDLEVERAGE: Final[int] 
SYMBOL_CALC_MODE_FOREX_NO_LEVERAGE: Final[int] 
SYMBOL_CALC_MODE_EXCH_STOCKS: Final[int] 
SYMBOL_CALC_MODE_EXCH_FUTURES: Final[int] 
SYMBOL_CALC_MODE_EXCH_OPTIONS: Final[int] 
SYMBOL_CALC_MODE_EXCH_OPTIONS_MARGIN: Final[int] 
SYMBOL_CALC_MODE_EXCH_BONDS: Final[int] 
SYMBOL_CALC_MODE_EXCH_STOCKS_MOEX: Final[int] 
SYMBOL_CALC_MODE_EXCH_BONDS_MOEX: Final[int] 
SYMBOL_CALC_MODE_SERV_COLLATERAL: Final[int] 

# Symbol trade mode
SYMBOL_TRADE_MODE_DISABLED: Final[int] 
SYMBOL_TRADE_MODE_LONGONLY: Final[int] 
SYMBOL_TRADE_MODE_SHORTONLY: Final[int] 
SYMBOL_TRADE_MODE_CLOSEONLY: Final[int] 
SYMBOL_TRADE_MODE_FULL: Final[int] 

from typing import Final

# SYMBOL_TRADE_EXECUTION
SYMBOL_TRADE_EXECUTION_REQUEST: Final[int] 
SYMBOL_TRADE_EXECUTION_INSTANT: Final[int] 
SYMBOL_TRADE_EXECUTION_MARKET: Final[int] 
SYMBOL_TRADE_EXECUTION_EXCHANGE: Final[int] 

# SYMBOL_SWAP_MODE
SYMBOL_SWAP_MODE_DISABLED: Final[int] 
SYMBOL_SWAP_MODE_POINTS: Final[int] 
SYMBOL_SWAP_MODE_CURRENCY_SYMBOL: Final[int] 
SYMBOL_SWAP_MODE_CURRENCY_MARGIN: Final[int] 
SYMBOL_SWAP_MODE_CURRENCY_DEPOSIT: Final[int] 
SYMBOL_SWAP_MODE_INTEREST_CURRENT: Final[int] 
SYMBOL_SWAP_MODE_INTEREST_OPEN: Final[int] 
SYMBOL_SWAP_MODE_REOPEN_CURRENT: Final[int] 
SYMBOL_SWAP_MODE_REOPEN_BID: Final[int] 

# DAY_OF_WEEK
DAY_OF_WEEK_SUNDAY: Final[int] 
DAY_OF_WEEK_MONDAY: Final[int] 
DAY_OF_WEEK_TUESDAY: Final[int] 
DAY_OF_WEEK_WEDNESDAY: Final[int] 
DAY_OF_WEEK_THURSDAY: Final[int] 
DAY_OF_WEEK_FRIDAY: Final[int] 
DAY_OF_WEEK_SATURDAY: Final[int] 

# SYMBOL_ORDERS_GTC_MODE
SYMBOL_ORDERS_GTC: Final[int] 
SYMBOL_ORDERS_DAILY: Final[int] 
SYMBOL_ORDERS_DAILY_NO_STOPS: Final[int] 

# SYMBOL_OPTION_RIGHT
SYMBOL_OPTION_RIGHT_CALL: Final[int] 
SYMBOL_OPTION_RIGHT_PUT: Final[int] 

# SYMBOL_OPTION_MODE
SYMBOL_OPTION_MODE_EUROPEAN: Final[int] 
SYMBOL_OPTION_MODE_AMERICAN: Final[int] 

# ACCOUNT_TRADE_MODE
ACCOUNT_TRADE_MODE_DEMO: Final[int] 
ACCOUNT_TRADE_MODE_CONTEST: Final[int] 
ACCOUNT_TRADE_MODE_REAL: Final[int] 

# ACCOUNT_STOPOUT_MODE
ACCOUNT_STOPOUT_MODE_PERCENT: Final[int] 
ACCOUNT_STOPOUT_MODE_MONEY: Final[int] 

# ACCOUNT_MARGIN_MODE
ACCOUNT_MARGIN_MODE_RETAIL_NETTING: Final[int] 
ACCOUNT_MARGIN_MODE_EXCHANGE: Final[int] 
ACCOUNT_MARGIN_MODE_RETAIL_HEDGING: Final[int] 

# BOOK_TYPE
BOOK_TYPE_SELL: Final[int] 
BOOK_TYPE_BUY: Final[int] 
BOOK_TYPE_SELL_MARKET: Final[int] 
BOOK_TYPE_BUY_MARKET: Final[int] 

# TRADE_RETCODE
TRADE_RETCODE_REQUOTE: Final[int] 
TRADE_RETCODE_REJECT: Final[int] 
TRADE_RETCODE_CANCEL: Final[int] 
TRADE_RETCODE_PLACED: Final[int] 
TRADE_RETCODE_DONE: Final[int] 
TRADE_RETCODE_DONE_PARTIAL: Final[int] 
TRADE_RETCODE_ERROR: Final[int] 
TRADE_RETCODE_TIMEOUT: Final[int] 
TRADE_RETCODE_INVALID: Final[int] 
TRADE_RETCODE_INVALID_VOLUME: Final[int] 
TRADE_RETCODE_INVALID_PRICE: Final[int] 
TRADE_RETCODE_INVALID_STOPS: Final[int] 
TRADE_RETCODE_TRADE_DISABLED: Final[int] 
TRADE_RETCODE_MARKET_CLOSED: Final[int] 
TRADE_RETCODE_NO_MONEY: Final[int] 
TRADE_RETCODE_PRICE_CHANGED: Final[int] 
TRADE_RETCODE_PRICE_OFF: Final[int] 
TRADE_RETCODE_INVALID_EXPIRATION: Final[int] 
TRADE_RETCODE_ORDER_CHANGED: Final[int] 
TRADE_RETCODE_TOO_MANY_REQUESTS: Final[int] 
TRADE_RETCODE_NO_CHANGES: Final[int] 
TRADE_RETCODE_SERVER_DISABLES_AT: Final[int] 
TRADE_RETCODE_CLIENT_DISABLES_AT: Final[int] 
TRADE_RETCODE_LOCKED: Final[int] 
TRADE_RETCODE_FROZEN: Final[int] 
TRADE_RETCODE_INVALID_FILL: Final[int] 
TRADE_RETCODE_CONNECTION: Final[int] 
TRADE_RETCODE_ONLY_REAL: Final[int] 
TRADE_RETCODE_LIMIT_ORDERS: Final[int] 
TRADE_RETCODE_LIMIT_VOLUME: Final[int] 
TRADE_RETCODE_INVALID_ORDER: Final[int] 
TRADE_RETCODE_POSITION_CLOSED: Final[int] 
TRADE_RETCODE_INVALID_CLOSE_VOLUME: Final[int] 
TRADE_RETCODE_CLOSE_ORDER_EXIST: Final[int] 
TRADE_RETCODE_LIMIT_POSITIONS: Final[int] 
TRADE_RETCODE_REJECT_CANCEL: Final[int] 
TRADE_RETCODE_LONG_ONLY: Final[int] 
TRADE_RETCODE_SHORT_ONLY: Final[int] 
TRADE_RETCODE_CLOSE_ONLY: Final[int] 
TRADE_RETCODE_FIFO_CLOSE: Final[int] 

# functio error codes (RES_ codes)
RES_S_OK: Final[int]  # generic success
RES_E_FAIL: Final[int]   # generic fail
RES_E_INVALID_PARAMS: Final[int]   # invalid arguments/parameters
RES_E_NO_MEMORY: Final[int]   # no memory condition
RES_E_NOT_FOUND: Final[int]   # no history
RES_E_INVALID_VERSION: Final[int]   # invalid version
RES_E_AUTH_FAILED: Final[int]   # authorization failed
RES_E_UNSUPPORTED: Final[int]   # unsupported method
RES_E_AUTO_TRADING_DISABLED: Final[int]   # auto-trading disabled
RES_E_INTERNAL_FAIL: Final[int]   # internal IPC general error
RES_E_INTERNAL_FAIL_SEND: Final[int]   # internal IPC send failed
RES_E_INTERNAL_FAIL_RECEIVE: Final[int]   # internal IPC recv failed
RES_E_INTERNAL_FAIL_INIT: Final[int]   # internal IPC initialization fail
RES_E_INTERNAL_FAIL_CONNECT: Final[int]   # internal IPC no ipc
RES_E_INTERNAL_FAIL_TIMEOUT: Final[int]   # internal timeout
