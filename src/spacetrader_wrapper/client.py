from spacetrader_wrapper import api, models
from spacetrader_wrapper.config import BaseConfig, ProdConfig


class Client():
    def __init__(self, token: str, config: BaseConfig = ProdConfig()):
        self.config = config
        self.config.HEADER.update({
            "Authorization": f"Bearer {token}"
        })
    
    @classmethod
    def register(cls, symbol: str, faction: str, config: BaseConfig = ProdConfig()):
        data = models.Registration(symbol=symbol, faction=faction)
        res = api.register.post(data, config)
        assert res.status_code == 201, "Registration did not succeed"
        return cls(res.content['data']['token'])
        
    @property
    def agent(self) -> models.Agent:
        return api.agent.get(self.config)
    
    #---------------------------
    #     System
    #---------------------------
    
    def list_systems(self) -> list[models.System]:
        return api.system.list(self.config)
    
    def get_system(self, systemSymbol: str) -> models.System:
        return api.system.get(self.config, systemSymbol)
    
    #---------------------------
    #     Waypoint
    #---------------------------
    
    def list_waypoints(self, systemSymbol: str) -> list[models.Waypoint]:
        return api.waypoint.list(self.config, systemSymbol)
    
    def get_waypoint(self, systemSymbol: str, waypointSymbol: str) -> models.Waypoint:
        return api.waypoint.get(self.config, systemSymbol, waypointSymbol)
    
    #---------------------------
    #     Orbitals
    #---------------------------
    
    def get_market(self, systemSymbol: str, waypointSymbol: str) -> models.Market:
        return api.market.get(self.config, systemSymbol, waypointSymbol)
    
    def get_shipyard(self, systemSymbol: str, waypointSymbol: str) -> models.Shipyard:
        return api.shipyard.get(self.config, systemSymbol, waypointSymbol)
    
    def get_jump_gate(self, systemSymbol: str, waypointSymbol: str) -> models.JumpGate:
        return api.jump_gate.get(self.config, systemSymbol, waypointSymbol)
    
    #---------------------------
    #     Factions
    #---------------------------
    
    def list_factions(self) -> list[models.Faction]:
        return api.faction.list(self.config)
    
    def get_faction(self, factionSymbol: str) -> list[models.Faction]:
        return api.faction.get(self.config, factionSymbol)
    
    #---------------------------
    #     Contracts
    #---------------------------
    
    def list_contracts(self) -> list[models.Contract]:
        return api.contract.list(self.config)
    
    def get_contract(self, contractSymbol: str) -> models.Contract:
        return api.contract.get(self.config, contractSymbol)
    
    def accept_contract(self, contractSymbol: str) -> api.contract.ContractResponse:
        return api.contract.accept(self.config, contractSymbol)
    
    def deliver_contract(self, contractSymbol: str, shipSymbol: str, tradeSymbol: str, units: int) -> api.contract.ContractResponse:
        delivery = models.Delivery(
            shipSymbol=shipSymbol,
            tradeSymbol=tradeSymbol,
            units=units,
        )
        return api.contract.deliver(self.config, contractSymbol, delivery)
        
    def fulfill_contract(self, contractSymbol: str) -> api.contract.ContractResponse:
        return api.contract.fulfill(self.config, contractSymbol)
    
    