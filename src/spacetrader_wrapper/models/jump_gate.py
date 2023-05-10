from pydantic import BaseModel

from .connected_systems import ConnectedSystems


class JumpGate(BaseModel):
    jumpRange: int
    factionSymbol: str
    connectedSystems: list[ConnectedSystems]
