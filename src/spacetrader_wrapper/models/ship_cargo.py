from pydantic import BaseModel

from .ship_cargo_item import ShipCargoItem


class ShipCargo(BaseModel):
    capacity: int
    units: int
    inventory: list[ShipCargoItem]
