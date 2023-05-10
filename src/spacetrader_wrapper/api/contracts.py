from typing import List, Optional
from pydantic import parse_obj_as, BaseModel

from .base import _get, _post
from spacetrader_wrapper import models
from spacetrader_wrapper.config import BaseConfig


class ContractResponse(BaseModel):
    agent: Optional[models.Agent]
    contract: Optional[models.Contract]
    cargo: Optional[models.ShipCargo]


def list(config: BaseConfig):
    res = _get(
        "/my/contracts",
        config=config,
    )
    return parse_obj_as(List[models.Contract], res.json()["data"])


def get_agent(config: BaseConfig, contractSymbol: str):
    res = _get(
        f"/my/contracts/{contractSymbol}",
        config=config,
    )
    return parse_obj_as(models.Contract, res.json()["data"])


def accept(config: BaseConfig, contractSymbol: str):
    res = _post(
        f"/my/contracts/{contractSymbol}/accept",
        config=config,
    )
    return parse_obj_as(ContractResponse, res.json()["data"])


def deliver(config: BaseConfig, contractSymbol: str, delivery: models.Delivery):
    res = _post(
        f"/my/contracts/{contractSymbol}/deliver", config=config, json=delivery.dict()
    )
    return parse_obj_as(ContractResponse, res.json()["data"])


def fulfill(config: BaseConfig, contractSymbol: str):
    res = _post(
        f"/my/contracts/{contractSymbol}/fulfill",
        config=config,
    )
    return parse_obj_as(ContractResponse, res.json()["data"])
