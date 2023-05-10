from pydantic import BaseModel


class SurveyDeposit(BaseModel):
    symbol: str
