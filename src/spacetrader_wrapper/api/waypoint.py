from typing import List
from pydantic import parse_obj_as

from .base import _get, _post
from spacetrader_wrapper import models
from spacetrader_wrapper.config import BaseConfig

def list(config: BaseConfig, systemSymbol: str):
    res = _get(
        f'/systems/{systemSymbol}/waypoints',
        config=config,
    )
    return parse_obj_as(List[models.Waypoint], res.json()['data'])

def get(config: BaseConfig, systemSymbol: str, waypointSymbol: str):
    res = _get(
        f'/systems/{systemSymbol}/waypoints/{waypointSymbol}',
        config=config,
    )
    return parse_obj_as(models.Waypoint, res.json()['data'])