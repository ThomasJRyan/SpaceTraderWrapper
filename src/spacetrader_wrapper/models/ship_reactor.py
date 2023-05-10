from pydantic import BaseModel

from .ship_requirements import ShipRequirements


class ShipReactor(BaseModel):
    symbol: str
    name: str
    description: str
    powerOutput: int
    requirements: ShipRequirements
    condition: int = None
