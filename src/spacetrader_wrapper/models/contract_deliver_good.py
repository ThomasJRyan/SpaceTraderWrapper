from datetime import datetime

from pydantic import BaseModel


class ContractDeliverGood(BaseModel):
    tradeSymbol: str
    destinationSymbol: str
    unitsRequired: int
    unitsFulfilled: int
