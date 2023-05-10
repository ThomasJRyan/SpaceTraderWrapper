from pydantic import BaseModel

from .ship_requirements import ShipRequirements


class ShipMount(BaseModel):
    symbol: str
    name: str
    description: str
    strength: int
    deposits: list[str]
    requirements: ShipRequirements
