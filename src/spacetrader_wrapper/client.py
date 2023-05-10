from spacetrader_wrapper import api, models
from spacetrader_wrapper.config import BaseConfig, ProdConfig


class Client:
    def __init__(self, token: str, config: BaseConfig = ProdConfig()):
        self.token = token
        self.config = config
        self.config.HEADER.update({"Authorization": f"Bearer {token}"})

    # ---------------------------
    #     Agent
    # ---------------------------

    @classmethod
    def register(cls, symbol: str, faction: str, config: BaseConfig = ProdConfig()):
        data = models.Registration(symbol=symbol, faction=faction)
        res = api.agent.register_agent(data, config)
        assert res.status_code == 201, "Registration did not succeed"
        return cls(res.json()["data"]["token"])

    @property
    def agent(self) -> models.Agent:
        return api.agent.get_agent(self.config)

    # ---------------------------
    #     Systems
    # ---------------------------

    def list_systems(self) -> list[models.System]:
        return api.systems.list_systems(self.config)

    def get_system(self, systemSymbol: str) -> models.System:
        return api.systems.get_system(self.config, systemSymbol)

    def list_waypoints(self, systemSymbol: str) -> list[models.Waypoint]:
        return api.systems.list_waypoints(self.config, systemSymbol)

    def get_waypoint(self, systemSymbol: str, waypointSymbol: str) -> models.Waypoint:
        return api.systems.get_waypoint(self.config, systemSymbol, waypointSymbol)

    def get_market(self, systemSymbol: str, waypointSymbol: str) -> models.Market:
        return api.systems.get_market(self.config, systemSymbol, waypointSymbol)

    def get_shipyard(self, systemSymbol: str, waypointSymbol: str) -> models.Shipyard:
        return api.systems.get_shipyard(self.config, systemSymbol, waypointSymbol)

    def get_jump_gate(self, systemSymbol: str, waypointSymbol: str) -> models.JumpGate:
        return api.systems.get_jump_gate(self.config, systemSymbol, waypointSymbol)

    # ---------------------------
    #     Factions
    # ---------------------------

    def list_factions(self) -> list[models.Faction]:
        return api.factions.list(self.config)

    def get_faction(self, factionSymbol: str) -> list[models.Faction]:
        return api.factions.get_agent(self.config, factionSymbol)

    # ---------------------------
    #     Contracts
    # ---------------------------

    def list_contracts(self) -> list[models.Contract]:
        return api.contracts.list(self.config)

    def get_contract(self, contractSymbol: str) -> models.Contract:
        return api.contracts.get_agent(self.config, contractSymbol)

    def accept_contract(self, contractSymbol: str) -> api.contracts.ContractResponse:
        return api.contracts.accept(self.config, contractSymbol)

    def deliver_contract(
        self, contractSymbol: str, shipSymbol: str, tradeSymbol: str, units: int
    ) -> api.contracts.ContractResponse:
        delivery = models.Delivery(
            shipSymbol=shipSymbol,
            tradeSymbol=tradeSymbol,
            units=units,
        )
        return api.contracts.deliver(self.config, contractSymbol, delivery)

    def fulfill_contract(self, contractSymbol: str) -> api.contracts.ContractResponse:
        return api.contracts.fulfill(self.config, contractSymbol)

    # ---------------------------
    #     Fleet
    # ---------------------------

    def list_ships(self):
        return api.fleet.list_ships(self.config)

    def purchase_ship(self, shipType: str, waypointSymbol: str):
        ship_purchase = models.ShipPurchase(
            shipType=shipType,
            waypointSymbol=waypointSymbol,
        )
        return api.fleet.purchase_ship(self.config, ship_purchase)

    def get_ship(self, shipSymbol: str):
        return api.fleet.get_ship(self.config, shipSymbol)

    def get_ship_cargo(self, shipSymbol: str):
        return api.fleet.get_ship_cargo(self.config, shipSymbol)

    def orbit_ship(self, shipSymbol: str):
        return api.fleet.orbit_ship(self.config, shipSymbol)

    def ship_refine(self, shipSymbol: str, raw_resource: str):
        resource = models.constants.RawResource(resource=raw_resource)
        return api.fleet.ship_refine(self.config, shipSymbol, resource)

    def create_chart(self, shipSymbol: str):
        return api.fleet.create_chart(self.config, shipSymbol)

    def get_ship_cooldown(self, shipSymbol: str):
        return api.fleet.get_ship_cooldown(self.config, shipSymbol)

    def dock_ship(self, shipSymbol: str):
        return api.fleet.dock_ship(self.config, shipSymbol)

    def create_survey(self, shipSymbol: str):
        return api.fleet.create_survey(self.config, shipSymbol)

    def extract_resources(self, shipSymbol: str, survey: models.Survey):
        return api.fleet.extract_resources(self.config, shipSymbol, survey)

    def jettison_cargo(self, shipSymbol: str, symbol: str, units: int):
        jettison = models.ExtractionYield(symbol=symbol, units=units)
        return api.fleet.jettison_cargo(self.config, shipSymbol, jettison)

    def jump_ship(self, shipSymbol: str, systemSymbol: str):
        return api.fleet.jump_ship(self.config, shipSymbol, systemSymbol)

    def navigate_ship(self, shipSymbol: str, waypointSymbol: str):
        return api.fleet.navigate_ship(self.config, shipSymbol, waypointSymbol)

    def patch_ship_nav(self, shipSymbol: str, flightMode: str):
        return api.fleet.patch_ship_nav(self.config, shipSymbol, flightMode)

    def get_ship_nav(self, shipSymbol: str):
        return api.fleet.get_ship_nav(self.config, shipSymbol)

    def warp_ship(self, shipSymbol: str, waypointSymbol: str):
        return api.fleet.warp_ship(self.config, shipSymbol, waypointSymbol)

    def sell_cargo(self, shipSymbol: str, symbol: str, units: int):
        cargo_sale = models.ExtractionYield(symbol=symbol, units=units)
        return api.fleet.sell_cargo(self.config, shipSymbol, cargo_sale)

    def scan_systems(self, shipSymbol: str):
        return api.fleet.scan_systems(self.config, shipSymbol)

    def scan_waypoints(self, shipSymbol: str):
        return api.fleet.scan_waypoints(self.config, shipSymbol)

    def scan_ships(self, shipSymbol: str):
        return api.fleet.scan_ships(self.config, shipSymbol)

    def refuel_ship(self, shipSymbol: str):
        return api.fleet.refuel_ship(self.config, shipSymbol)

    def purchase_cargo(self, shipSymbol: str, symbol: str, units: int):
        cargo_purchase = models.ExtractionYield(symbol=symbol, units=units)
        return api.fleet.purchase_cargo(self.config, shipSymbol, cargo_purchase)

    def transfer_cargo(
        self, shipSymbol: str, shipSymbolTo: str, tradeSymbol: str, units: int
    ):
        cargo_transfer = models.Delivery(
            shipSymbolTo=shipSymbolTo,
            tradeSymbol=tradeSymbol,
            units=units,
        )
        return api.fleet.transfer_cargo(self.config, shipSymbol, cargo_transfer)
