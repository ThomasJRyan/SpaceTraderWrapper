from typing import List
from pydantic import parse_obj_as

from .base import _get, _post
from spacetrader_wrapper import models
from spacetrader_wrapper.config import BaseConfig


def list(config: BaseConfig):
    res = _get(
        f"/factions",
        config=config,
    )
    return parse_obj_as(List[models.Faction], res.json()["data"])


def get_agent(config: BaseConfig, factionSymbol: str):
    res = _get(
        f"/factions/{factionSymbol}",
        config=config,
    )
    return parse_obj_as(models.Faction, res.json()["data"])
