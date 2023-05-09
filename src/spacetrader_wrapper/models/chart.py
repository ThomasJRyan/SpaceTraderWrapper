from datetime import datetime
from pydantic import BaseModel

class Chart(BaseModel):
    waypointSymbol: str = None
    submittedBy: str = None
    submittedOn: datetime = None