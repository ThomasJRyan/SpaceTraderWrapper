from datetime import datetime

from pydantic import BaseModel


class ShipFuelConsumption(BaseModel):
    amount: int
    timestamp: datetime
