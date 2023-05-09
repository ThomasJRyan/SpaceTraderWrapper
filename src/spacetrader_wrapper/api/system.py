from typing import List
from pydantic import parse_obj_as

from .base import _get, _post
from spacetrader_wrapper import models
from spacetrader_wrapper.config import BaseConfig

def list(config: BaseConfig):
    res = _get(
        '/systems',
        config=config,
    )
    return parse_obj_as(List[models.System], res.json()['data'])

def get(config: BaseConfig, systemSymbol: str):
    res = _get(
        f'/systems/{systemSymbol}',
        config=config,
    )
    return parse_obj_as(models.System, res.json()['data'])