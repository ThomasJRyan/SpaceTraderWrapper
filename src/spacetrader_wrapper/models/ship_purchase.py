from pydantic import BaseModel

class ShipPurchase(BaseModel):
    shipType: str = None
    waypointSymbol: str = None