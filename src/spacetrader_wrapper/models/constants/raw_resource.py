from typing import Literal
from pydantic import BaseModel

class RawResource(BaseModel):
    resource: Literal["IRON" ,"COPPER" ,"SILVER" ,"GOLD" ,"ALUMINUM" ,"PLATINUM" ,"URANITE" ,"MERITIUM" ,"FUEL"]