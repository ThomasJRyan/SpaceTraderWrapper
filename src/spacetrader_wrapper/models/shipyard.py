from pydantic import BaseModel

from .ship_type import ShipType
from .shipyard_transaction import ShipyardTransaction
from .ship import Ship


class Shipyard(BaseModel):
    symbol: str
    shipTypes: list[ShipType] = None
    transactions: list[ShipyardTransaction] = None
    ships: list[Ship] = None
