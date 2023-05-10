from pydantic import BaseModel


class TradeGood(BaseModel):
    symbol: str
    name: str
    description: str
