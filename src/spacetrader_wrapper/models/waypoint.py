from pydantic import BaseModel

from .chart import Chart
from .faction import Faction
from .waypoint_trait import WaypointTrait
from .waypoint_orbital import WaypointOrbital


class Waypoint(BaseModel):
    symbol: str
    type: str
    x: int
    y: int
    systemSymbol: str = None
    orbitals: list[WaypointOrbital] = None
    faction: Faction = None
    traits: list[WaypointTrait] = None
    chart: Chart = None
