from pydantic import BaseModel

class Agent(BaseModel):
    accountId: str
    symbol: str
    headquarters: str
    credits: int