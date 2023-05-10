from typing import List, Optional, Any
from pydantic import parse_obj_as, BaseModel

from .base import _get, _post, _patch
from spacetrader_wrapper import models
from spacetrader_wrapper.config import BaseConfig

class FleetResponse(BaseModel):
    agent: Optional[models.Agent]
    ship: Optional[models.Ship]
    transaction: Optional[models.ShipyardTransaction]
    cargo: Optional[models.ShipCargo]
    cooldown: Optional[models.Cooldown]
    produced: List[dict[str, Any]]
    consumed: List[dict[str, Any]]
    chart: models.Chart
    waypoint: models.Waypoint
    surveys: List[models.Survey]
    extraction: models.Extraction
    nav: models.ShipNav
    fuel: models.ShipFuel
    systems: List[models.System]

def list_ships(config: BaseConfig):
    res = _get(
        '/my/ships',
        config=config,
    )
    return parse_obj_as(List[models.Ship], res.json()['data'])

def purchase_ship(config: BaseConfig, ship_purchase: models.ShipPurchase):
    res = _post(
        '/my/ships',
        config=config,
        json=ship_purchase.dict()
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def get_ship(config: BaseConfig, shipSymbol: str):
    res = _get(
        f'/my/ships/{shipSymbol}',
        config=config,
    )
    return parse_obj_as(models.Ship, res.json()['data'])

def get_ship_cargo(config: BaseConfig, shipSymbol: str):
    res = _get(
        f'/my/ships/{shipSymbol}/cargo',
        config=config,
    )
    return parse_obj_as(models.ShipCargo, res.json()['data'])

def orbit_ship(config: BaseConfig, shipSymbol: str):
    res = _post(
        f'/my/ships/{shipSymbol}/orbit',
        config=config,
    )
    return parse_obj_as(models.ShipNav, res.json()['data'])

def ship_refine(config: BaseConfig, shipSymbol: str, produce: models.constants.RawResource):
    res = _post(
        f'/my/ships/{shipSymbol}/refine',
        config=config,
        json={'produce': produce.resource}
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def create_chart(config: BaseConfig, shipSymbol: str):
    res = _post(
        f'/my/ships/{shipSymbol}/chart',
        config=config,
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def get_ship_cooldown(config: BaseConfig, shipSymbol: str):
    res = _get(
        f'/my/ships/{shipSymbol}/cooldown',
        config=config,
    )
    return parse_obj_as(models.Cooldown, res.json()['data'])

def dock_ship(config: BaseConfig, shipSymbol: str):
    res = _post(
        f'/my/ships/{shipSymbol}/dock',
        config=config,
    )
    return parse_obj_as(models.ShipNav, res.json()['data'])

def create_survey(config: BaseConfig, shipSymbol: str):
    res = _post(
        f'/my/ships/{shipSymbol}/survey',
        config=config,
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def extract_resources(config: BaseConfig, shipSymbol: str, survey: models.Survey):
    res = _post(
        f'/my/ships/{shipSymbol}/extract',
        config=config,
        json=survey.dict()
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def jettison_cargo(config: BaseConfig, shipSymbol: str, jettison: models.ExtractionYield):
    res = _post(
        f'/my/ships/{shipSymbol}/jettison',
        config=config,
        json=jettison.dict()
    )
    return parse_obj_as(models.ShipCargo, res.json()['data'])

def jump_ship(config: BaseConfig, shipSymbol: str, systemSymbol: str):
    res = _post(
        f'/my/ships/{shipSymbol}/jump',
        config=config,
        json={'systemSymbol': systemSymbol}
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def navigate_ship(config: BaseConfig, shipSymbol: str, waypointSymbol: str):
    res = _post(
        f'/my/ships/{shipSymbol}/navigate',
        config=config,
        json={'waypointSymbol': waypointSymbol}
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def patch_ship_nav(config: BaseConfig, shipSymbol: str, flightMode: str):
    res = _patch(
        f'/my/ships/{shipSymbol}/nav',
        config=config,
        json={'flightMode': flightMode}
    )
    return parse_obj_as(models.ShipNav, res.json()['data'])

def get_ship_nav(config: BaseConfig, shipSymbol: str):
    res = _get(
        f'/my/ships/{shipSymbol}/nav',
        config=config,
    )
    return parse_obj_as(models.ShipNav, res.json()['data'])

def warp_ship(config: BaseConfig, shipSymbol: str, waypointSymbol: str):
    res = _post(
        f'/my/ships/{shipSymbol}/warp',
        config=config,
        json={'waypointSymbol': waypointSymbol}
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def sell_cargo(config: BaseConfig, shipSymbol: str, cargo_sale: models.ExtractionYield):
    res = _post(
        f'/my/ships/{shipSymbol}/sell',
        config=config,
        json=cargo_sale.dict()
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def scan_systems(config: BaseConfig, shipSymbol: str):
    res = _post(
        f'/my/ships/{shipSymbol}/scan/systems',
        config=config,
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def scan_waypoints(config: BaseConfig, shipSymbol: str):
    res = _post(
        f'/my/ships/{shipSymbol}/scan/waypoints',
        config=config,
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def scan_ships(config: BaseConfig, shipSymbol: str):
    res = _post(
        f'/my/ships/{shipSymbol}/scan/ships',
        config=config,
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def refuel_ship(config: BaseConfig, shipSymbol: str):
    res = _post(
        f'/my/ships/{shipSymbol}/refuel',
        config=config,
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def purchase_cargo(config: BaseConfig, shipSymbol: str, cargo_purchase: models.ExtractionYield):
    res = _post(
        f'/my/ships/{shipSymbol}/purchase',
        config=config,
        json=cargo_purchase.dict()
    )
    return parse_obj_as(FleetResponse, res.json()['data'])

def transfer_cargo(config: BaseConfig, shipSymbol: str, cargo_transfer: models.Delivery):
    res = _post(
        f'/my/ships/{shipSymbol}/transfer',
        config=config,
        json=cargo_transfer.dict()
    )
    return parse_obj_as(FleetResponse, res.json()['data'])