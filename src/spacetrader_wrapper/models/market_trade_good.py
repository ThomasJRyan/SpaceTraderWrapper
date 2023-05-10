from pydantic import BaseModel


class MarketTradeGood(BaseModel):
    symbol: str
    tradeVolume: int
    supply: str
    purchasePrice: int
    sellPrice: int
