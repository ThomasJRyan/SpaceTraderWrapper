from datetime import datetime

from pydantic import BaseModel

class Cooldown(BaseModel):
    shipSymbol: str
    totalSeconds: int
    remainingSeconds: int
    expiration: datetime