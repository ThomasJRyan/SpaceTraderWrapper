from pydantic import BaseModel

from .ship_requirements import ShipRequirements

class ShipFrame(BaseModel):
    symbol: str
    name: str
    description: str
    condition: int = None
    moduleSlots: int
    mountingPoints: int
    fuelCapacity: int
    requirements: ShipRequirements