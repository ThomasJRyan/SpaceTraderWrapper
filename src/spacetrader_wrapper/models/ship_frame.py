from pydantic import BaseModel

from .ship_requirements import ShipRequirements


class ShipFrame(BaseModel):
    symbol: str
    name: str = None
    description: str = None
    condition: int = None
    moduleSlots: int = None
    mountingPoints: int = None
    fuelCapacity: int = None
    requirements: ShipRequirements = None
