from pydantic import BaseModel

from .ship_requirements import ShipRequirements


class ShipMount(BaseModel):
    symbol: str
    name: str = None
    description: str = None
    strength: int = None
    deposits: list[str] = None
    requirements: ShipRequirements = None
