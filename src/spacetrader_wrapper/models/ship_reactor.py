from pydantic import BaseModel

from .ship_requirements import ShipRequirements


class ShipReactor(BaseModel):
    symbol: str
    name: str = None
    description: str = None
    powerOutput: int = None
    requirements: ShipRequirements = None
    condition: int = None
