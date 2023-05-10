from pydantic import BaseModel


class ExtractionYield(BaseModel):
    symbol: str
    units: int
