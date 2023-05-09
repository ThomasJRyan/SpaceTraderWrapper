from .base import _get, _post
from spacetrader_wrapper import models
from spacetrader_wrapper.config import BaseConfig

def get(config: BaseConfig, systemSymbol: str, waypointSymbol: str):
    res = _get(
        f'/systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard',
        config=config,
    )
    return models.Shipyard(**res.json()['data'])