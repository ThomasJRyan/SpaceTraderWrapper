from pydantic import BaseModel

class ShipRegistration(BaseModel):
    name: str
    role: str
    factionSymbol: str = None