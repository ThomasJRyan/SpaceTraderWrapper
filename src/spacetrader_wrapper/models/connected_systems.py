from pydantic import BaseModel, Field


class ConnectedSystems(BaseModel):
    symbol: str
    sectorSymbol: str
    type: str
    x: int
    y: int
    distance: int
    factionSymbol: str = None
