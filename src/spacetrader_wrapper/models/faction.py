from pydantic import BaseModel

from .faction_trait import FactionTrait

class Faction(BaseModel):
    symbol: str
    name: str = None
    description: str = None
    headquarters: str = None
    traits: list[FactionTrait] = None