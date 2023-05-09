from pydantic import BaseModel

from .trade_good import TradeGood
from .market_trade_good import MarketTradeGood
from .market_transaction import MarketTransaction

class Market(BaseModel):
    symbol: str
    exports: list[TradeGood]
    imports: list[TradeGood]
    exchange: list[TradeGood]
    transactions: list[MarketTransaction] = None
    tradeGoods: list[MarketTradeGood] = None