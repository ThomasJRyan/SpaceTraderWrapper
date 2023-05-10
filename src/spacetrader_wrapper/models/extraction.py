from pydantic import BaseModel, Field

from .extraction_yield import ExtractionYield


class Extraction(BaseModel):
    shipSymbol: str
    _yield: ExtractionYield = Field(alias="yield")
