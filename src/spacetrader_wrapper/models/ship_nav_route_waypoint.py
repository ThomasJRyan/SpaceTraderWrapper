from pydantic import BaseModel


class ShipNavRouteWaypoint(BaseModel):
    symbol: str
    type: str
    systemSymbol: str
    x: int
    y: int
