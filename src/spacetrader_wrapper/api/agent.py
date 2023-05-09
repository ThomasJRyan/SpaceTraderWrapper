from .base import _get, _post
from spacetrader_wrapper import models
from spacetrader_wrapper.config import BaseConfig

def get(config: BaseConfig):
    res = _get(
        '/my/agent',
        config=config,
    )
    return models.Agent(**res.json()['data'])