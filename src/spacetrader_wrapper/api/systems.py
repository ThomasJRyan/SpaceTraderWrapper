from typing import List
from pydantic import parse_obj_as

from .base import _get, _post
from spacetrader_wrapper import models
from spacetrader_wrapper.config import BaseConfig


def list_systems(config: BaseConfig):
    res = _get(
        "/systems",
        config=config,
    )
    return parse_obj_as(List[models.System], res.json()["data"])


def get_system(config: BaseConfig, systemSymbol: str):
    res = _get(
        f"/systems/{systemSymbol}",
        config=config,
    )
    return parse_obj_as(models.System, res.json()["data"])


def list_waypoints(config: BaseConfig, systemSymbol: str):
    res = _get(
        f"/systems/{systemSymbol}/waypoints",
        config=config,
    )
    return parse_obj_as(List[models.Waypoint], res.json()["data"])


def get_waypoint(config: BaseConfig, systemSymbol: str, waypointSymbol: str):
    res = _get(
        f"/systems/{systemSymbol}/waypoints/{waypointSymbol}",
        config=config,
    )
    return parse_obj_as(models.Waypoint, res.json()["data"])


def get_market(config: BaseConfig, systemSymbol: str, waypointSymbol: str):
    res = _get(
        f"/systems/{systemSymbol}/waypoints/{waypointSymbol}/market",
        config=config,
    )
    return models.Market(**res.json()["data"])


def get_shipyard(config: BaseConfig, systemSymbol: str, waypointSymbol: str):
    res = _get(
        f"/systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard",
        config=config,
    )
    return models.Shipyard(**res.json()["data"])


def get_jump_gate(config: BaseConfig, systemSymbol: str, waypointSymbol: str):
    res = _get(
        f"/systems/{systemSymbol}/waypoints/{waypointSymbol}/jump-gate",
        config=config,
    )
    return models.JumpGate(**res.json()["data"])
