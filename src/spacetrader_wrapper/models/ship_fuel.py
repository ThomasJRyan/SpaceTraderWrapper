from pydantic import BaseModel

from .ship_fuel_consumption import ShipFuelConsumption

class ShipFuel(BaseModel):
    current: int
    capacity: int
    consumed: ShipFuelConsumption