from pydantic import BaseModel

class Delivery(BaseModel):
    shipSymbol: str
    tradeSymbol: str
    units: int