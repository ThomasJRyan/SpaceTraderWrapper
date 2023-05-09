from .base import _get, _post
from spacetrader_wrapper import models
from spacetrader_wrapper.config import BaseConfig

def post(data: models.Registration, config: BaseConfig):
    return _post(
        '/register',
        config=config,
        json=data.dict(),
    )