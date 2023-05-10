from .base import _get, _post
from spacetrader_wrapper import models
from spacetrader_wrapper.config import BaseConfig


def get_agent(config: BaseConfig):
    res = _get(
        "/my/agent",
        config=config,
    )
    return models.Agent(**res.json()["data"])


def register_agent(data: models.Registration, config: BaseConfig):
    return _post(
        "/register",
        config=config,
        json=data.dict(),
    )
