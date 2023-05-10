from pydantic import BaseModel


class WaypointTrait(BaseModel):
    symbol: str
    name: str
    description: str
