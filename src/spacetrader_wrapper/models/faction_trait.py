from pydantic import BaseModel

class FactionTrait(BaseModel):
    symbol: str
    name: str
    description: str