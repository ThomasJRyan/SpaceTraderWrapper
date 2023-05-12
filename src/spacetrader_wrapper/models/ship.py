from pydantic import BaseModel

from .ship_registration import ShipRegistration
from .ship_nav import ShipNav
from .ship_crew import ShipCrew
from .ship_frame import ShipFrame
from .ship_reactor import ShipReactor
from .ship_engine import ShipEngine
from .ship_module import ShipModule
from .ship_mount import ShipMount
from .ship_cargo import ShipCargo
from .ship_fuel import ShipFuel


class Ship(BaseModel):
    symbol: str = None
    registration: ShipRegistration = None
    nav: ShipNav = None
    crew: ShipCrew = None
    frame: ShipFrame
    reactor: ShipReactor
    engine: ShipEngine
    modules: list[ShipModule] = None
    mounts: list[ShipMount]
    cargo: ShipCargo = None
    fuel: ShipFuel = None
