from datetime import datetime

from pydantic import BaseModel


class ShipyardTransaction(BaseModel):
    waypointSymbol: str
    shipSymbol: str
    price: int
    agentSymbol: str
    timestamp: datetime
