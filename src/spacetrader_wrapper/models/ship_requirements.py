from pydantic import BaseModel

class ShipRequirements(BaseModel):
    power: int
    crew: int
    slots: int