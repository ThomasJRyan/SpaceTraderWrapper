from pydantic import BaseModel

from .ship_nav_route import ShipNavRoute


class ShipNav(BaseModel):
    systemSymbol: str
    waypointSymbol: str
    route: ShipNavRoute
    status: str
    flightMode: str
