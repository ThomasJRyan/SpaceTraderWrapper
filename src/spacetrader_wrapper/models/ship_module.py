from pydantic import BaseModel, Field

from .ship_requirements import ShipRequirements

class ShipModule(BaseModel):
    symbol: str
    name: str
    description: str
    requirements: ShipRequirements
    capacity: int = Field(None, ge=0)
    range: int = Field(None, ge=0)