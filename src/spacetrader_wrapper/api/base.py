import requests

from spacetrader_wrapper.config import BaseConfig

def _get(endpoint, *args, config: BaseConfig, **kwargs):
    with requests.session() as s:
        res = s.get(
            *args, 
            url=f"{config.BASE_URL}/{endpoint}",
            headers=config.HEADER, 
            **kwargs)
    return res

def _post(endpoint, *args, config: BaseConfig, **kwargs):
    with requests.session() as s:
        res = s.post(
            *args, 
            url=f"{config.BASE_URL}/{endpoint}",
            headers=config.HEADER, 
            **kwargs)
    return res

def _patch(endpoint, *args, config: BaseConfig, **kwargs):
    with requests.session() as s:
        res = s.patch(
            *args, 
            url=f"{config.BASE_URL}/{endpoint}",
            headers=config.HEADER, 
            **kwargs)
    return res