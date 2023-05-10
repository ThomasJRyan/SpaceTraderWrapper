from pydantic import BaseModel


class ShipType(BaseModel):
    type: str = None
