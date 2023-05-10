from pydantic import BaseModel


class ContractPayment(BaseModel):
    onAccepted: int
    onFulfilled: int
