from datetime import datetime

from pydantic import BaseModel

from .contract_payment import ContractPayment
from .contract_deliver_good import ContractDeliverGood

class ContractTerms(BaseModel):
    deadline: datetime
    payment: ContractPayment
    deliver: list[ContractDeliverGood]