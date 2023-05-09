from pydantic import BaseModel

class ShipCargoItem(BaseModel):
    symbol: str
    name: str
    description: str
    units: int