import unittest
import datetime

from spacetrader_wrapper import Client
from spacetrader_wrapper.config import TestConfig


class TestSystems(unittest.TestCase):
    def setUp(self):
        self.client = Client("", config=TestConfig)

    def test_list_systems(self):
        systems = self.client.list_systems()
        self.assertEqual(len(systems), 1)

        system = systems[0]
        self.assertEqual(
            system.dict(),
            {
                "symbol": "string",
                "sectorSymbol": "string",
                "type": "NEUTRON_STAR",
                "x": 0,
                "y": 0,
                "waypoints": [
                    {
                        "symbol": "string",
                        "type": "PLANET",
                        "x": 0,
                        "y": 0,
                        "systemSymbol": None,
                        "orbitals": None,
                        "faction": None,
                        "traits": None,
                        "chart": None,
                    }
                ],
                "factions": [
                    {
                        "symbol": "string",
                        "name": None,
                        "description": None,
                        "headquarters": None,
                        "traits": None,
                    }
                ],
            },
        )

    def test_get_system(self):
        system = self.client.get_system("string")
        self.assertEqual(
            system.dict(),
            {
                "symbol": "string",
                "sectorSymbol": "string",
                "type": "NEUTRON_STAR",
                "x": 0,
                "y": 0,
                "waypoints": [
                    {
                        "symbol": "string",
                        "type": "PLANET",
                        "x": 0,
                        "y": 0,
                        "systemSymbol": None,
                        "orbitals": None,
                        "faction": None,
                        "traits": None,
                        "chart": None,
                    }
                ],
                "factions": [
                    {
                        "symbol": "string",
                        "name": None,
                        "description": None,
                        "headquarters": None,
                        "traits": None,
                    }
                ],
            },
        )

    def test_list_waypoints(self):
        waypoints = self.client.list_waypoints("string")
        self.assertEqual(len(waypoints), 1)

        waypoint = waypoints[0]
        self.assertEqual(
            waypoint.dict(),
            {
                "symbol": "string",
                "type": "PLANET",
                "x": 0,
                "y": 0,
                "systemSymbol": "string",
                "orbitals": [{"symbol": "string"}],
                "faction": {
                    "symbol": "string",
                    "name": None,
                    "description": None,
                    "headquarters": None,
                    "traits": None,
                },
                "traits": [
                    {"symbol": "UNCHARTED", "name": "string", "description": "string"}
                ],
                "chart": {
                    "waypointSymbol": "string",
                    "submittedBy": "string",
                    "submittedOn": datetime.datetime(
                        2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                    ),
                },
            },
        )

    def test_get_waypoint(self):
        waypoint = self.client.get_waypoint("string", "string")
        self.assertEqual(
            waypoint.dict(),
            {
                "symbol": "string",
                "type": "PLANET",
                "x": 0,
                "y": 0,
                "systemSymbol": "string",
                "orbitals": [{"symbol": "string"}],
                "faction": {
                    "symbol": "string",
                    "name": None,
                    "description": None,
                    "headquarters": None,
                    "traits": None,
                },
                "traits": [
                    {"symbol": "UNCHARTED", "name": "string", "description": "string"}
                ],
                "chart": {
                    "waypointSymbol": "string",
                    "submittedBy": "string",
                    "submittedOn": datetime.datetime(
                        2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                    ),
                },
            },
        )

    def test_get_market(self):
        market = self.client.get_market("string", "string")
        self.assertEqual(
            market.dict(),
            {
                "symbol": "string",
                "exports": [
                    {
                        "symbol": "PRECIOUS_STONES",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "imports": [
                    {
                        "symbol": "PRECIOUS_STONES",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "exchange": [
                    {
                        "symbol": "PRECIOUS_STONES",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "transactions": [
                    {
                        "waypointSymbol": "string",
                        "shipSymbol": "string",
                        "tradeSymbol": "string",
                        "type": "PURCHASE",
                        "units": 1,
                        "pricePerUnit": 1,
                        "totalPrice": 1,
                        "timestamp": datetime.datetime(
                            2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                        ),
                    }
                ],
                "tradeGoods": [
                    {
                        "symbol": "string",
                        "tradeVolume": 1,
                        "supply": "SCARCE",
                        "purchasePrice": 0,
                        "sellPrice": 0,
                    }
                ],
            },
        )

    def test_get_shipyard(self):
        shipyard = self.client.get_shipyard("string", "string")
        self.assertEqual(
            shipyard.dict(),
            {
                "symbol": "string",
                "shipTypes": [{"type": "SHIP_PROBE"}],
                "transactions": [
                    {
                        "waypointSymbol": "string",
                        "shipSymbol": "string",
                        "price": 1,
                        "agentSymbol": "string",
                        "timestamp": datetime.datetime(
                            2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                        ),
                    }
                ],
                "ships": [
                    {
                        "symbol": None,
                        "registration": None,
                        "nav": None,
                        "crew": None,
                        "frame": {
                            "symbol": "FRAME_PROBE",
                            "name": "string",
                            "description": "string",
                            "condition": 0,
                            "moduleSlots": 0,
                            "mountingPoints": 0,
                            "fuelCapacity": 0,
                            "requirements": {"power": 0, "crew": 0, "slots": 0},
                        },
                        "reactor": {
                            "symbol": "REACTOR_SOLAR_I",
                            "name": "string",
                            "description": "string",
                            "powerOutput": 1,
                            "requirements": {"power": 0, "crew": 0, "slots": 0},
                            "condition": 0,
                        },
                        "engine": {
                            "symbol": "ENGINE_IMPULSE_DRIVE_I",
                            "name": "string",
                            "description": "string",
                            "requirements": {"power": 0, "crew": 0, "slots": 0},
                            "speed": 1,
                            "condition": 0,
                        },
                        "modules": [
                            {
                                "symbol": "MODULE_MINERAL_PROCESSOR_I",
                                "name": "string",
                                "description": "string",
                                "requirements": {"power": 0, "crew": 0, "slots": 0},
                                "capacity": 0,
                                "range": 0,
                            }
                        ],
                        "mounts": [
                            {
                                "symbol": "MOUNT_GAS_SIPHON_I",
                                "name": "string",
                                "description": "string",
                                "strength": 0,
                                "deposits": ["QUARTZ_SAND"],
                                "requirements": {"power": 0, "crew": 0, "slots": 0},
                            }
                        ],
                        "cargo": None,
                        "fuel": None,
                    }
                ],
            },
        )

    def test_get_jump_gate(self):
        jump_gate = self.client.get_jump_gate("string", "string")
        self.assertEqual(
            jump_gate.dict(),
            {
                "jumpRange": 0,
                "factionSymbol": "string",
                "connectedSystems": [
                    {
                        "symbol": "string",
                        "sectorSymbol": "string",
                        "type": "NEUTRON_STAR",
                        "x": 0,
                        "y": 0,
                        "distance": 0,
                        "factionSymbol": "string",
                    }
                ],
            },
        )
