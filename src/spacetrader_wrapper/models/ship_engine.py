from pydantic import BaseModel, Field

from .ship_requirements import ShipRequirements


class ShipEngine(BaseModel):
    symbol: str
    name: str = None
    description: str = None
    requirements: ShipRequirements = None
    speed: int = Field(1, ge=1)
    condition: int = Field(0, ge=0, le=100)
