from pydantic import BaseModel

from .waypoint import Waypoint
from .faction import Faction

class System(BaseModel):
    symbol: str
    sectorSymbol: str
    type: str
    x: int
    y: int
    waypoints: list[Waypoint]
    factions: list[Faction]