from datetime import datetime

from pydantic import BaseModel

from .contract_terms import ContractTerms


class Contract(BaseModel):
    id: str
    factionSymbol: str
    type: str
    terms: ContractTerms
    accepted: bool
    fulfilled: bool
    expiration: datetime
