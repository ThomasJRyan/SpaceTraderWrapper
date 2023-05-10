from datetime import datetime

from pydantic import BaseModel

from .ship_nav_route_waypoint import ShipNavRouteWaypoint


class ShipNavRoute(BaseModel):
    destination: ShipNavRouteWaypoint
    departure: ShipNavRouteWaypoint
    departureTime: datetime
    arrival: datetime
