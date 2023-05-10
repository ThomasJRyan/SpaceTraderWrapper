from pydantic import BaseModel


class ShipCrew(BaseModel):
    current: int
    required: int
    capacity: int
    rotation: str
    morale: int
    wages: int
