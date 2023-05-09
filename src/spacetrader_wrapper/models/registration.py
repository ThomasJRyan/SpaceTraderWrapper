from typing import Literal
from pydantic import BaseModel

class Registration(BaseModel):
    symbol: str
    faction: Literal["COSMIC", "VOID", "GALACTIC", "QUANTUM", "DOMINION", "ASTRO", "CORSAIRS"]