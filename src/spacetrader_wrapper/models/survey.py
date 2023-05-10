from datetime import datetime

from pydantic import BaseModel

from .survey_deposit import SurveyDeposit

class Survey(BaseModel):
    signature: str
    symbol: str
    deposits: list[SurveyDeposit]
    expiration: datetime
    size: str