import unittest
import datetime

from spacetrader_wrapper import Client
from spacetrader_wrapper.config import TestConfig
from spacetrader_wrapper import models


class TestFleet(unittest.TestCase):
    def setUp(self):
        self.client = Client("", config=TestConfig)

    def test_list_ships(self):
        ret_obj = self.client.list_ships()[0]
        self.assertEqual(ret_obj.dict(), {'symbol': 'string', 'registration': {'name': 'string', 'role': 'FABRICATOR', 'factionSymbol': 'string'}, 'nav': {'systemSymbol': 'string', 'waypointSymbol': 'string', 'route': {'destination': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departure': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departureTime': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc), 'arrival': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'status': 'IN_TRANSIT', 'flightMode': 'CRUISE'}, 'crew': {'current': 0, 'required': 0, 'capacity': 0, 'rotation': 'STRICT', 'morale': 0, 'wages': 0}, 'frame': {'symbol': 'FRAME_PROBE', 'name': 'string', 'description': 'string', 'condition': 0, 'moduleSlots': 0, 'mountingPoints': 0, 'fuelCapacity': 0, 'requirements': {'power': 0, 'crew': 0, 'slots': 0}}, 'reactor': {'symbol': 'REACTOR_SOLAR_I', 'name': 'string', 'description': 'string', 'powerOutput': 1, 'requirements': {'power': 0, 'crew': 0, 'slots': 0}, 'condition': 0}, 'engine': {'symbol': 'ENGINE_IMPULSE_DRIVE_I', 'name': 'string', 'description': 'string', 'requirements': {'power': 0, 'crew': 0, 'slots': 0}, 'speed': 1, 'condition': 0}, 'modules': [{'symbol': 'MODULE_MINERAL_PROCESSOR_I', 'name': 'string', 'description': 'string', 'requirements': {'power': 0, 'crew': 0, 'slots': 0}, 'capacity': 0, 'range': 0}], 'mounts': [{'symbol': 'MOUNT_GAS_SIPHON_I', 'name': 'string', 'description': 'string', 'strength': 0, 'deposits': ['QUARTZ_SAND'], 'requirements': {'power': 0, 'crew': 0, 'slots': 0}}], 'cargo': {'capacity': 0, 'units': 0, 'inventory': [{'symbol': 'string', 'name': 'string', 'description': 'string', 'units': 1}]}, 'fuel': {'current': 0, 'capacity': 0, 'consumed': {'amount': 0, 'timestamp': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}}})

    def test_purchase_ship(self):
        ret_obj = self.client.purchase_ship('SHIP_PROBE', 'string')
        self.assertEqual(ret_obj.dict(), {'agent': {'accountId': 'string', 'symbol': 'string', 'headquarters': 'string', 'credits': 0}, 'ship': {'symbol': 'string', 'registration': {'name': 'string', 'role': 'FABRICATOR', 'factionSymbol': 'string'}, 'nav': {'systemSymbol': 'string', 'waypointSymbol': 'string', 'route': {'destination': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departure': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departureTime': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc), 'arrival': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'status': 'IN_TRANSIT', 'flightMode': 'CRUISE'}, 'crew': {'current': 0, 'required': 0, 'capacity': 0, 'rotation': 'STRICT', 'morale': 0, 'wages': 0}, 'frame': {'symbol': 'FRAME_PROBE', 'name': 'string', 'description': 'string', 'condition': 0, 'moduleSlots': 0, 'mountingPoints': 0, 'fuelCapacity': 0, 'requirements': {'power': 0, 'crew': 0, 'slots': 0}}, 'reactor': {'symbol': 'REACTOR_SOLAR_I', 'name': 'string', 'description': 'string', 'powerOutput': 1, 'requirements': {'power': 0, 'crew': 0, 'slots': 0}, 'condition': 0}, 'engine': {'symbol': 'ENGINE_IMPULSE_DRIVE_I', 'name': 'string', 'description': 'string', 'requirements': {'power': 0, 'crew': 0, 'slots': 0}, 'speed': 1, 'condition': 0}, 'modules': [{'symbol': 'MODULE_MINERAL_PROCESSOR_I', 'name': 'string', 'description': 'string', 'requirements': {'power': 0, 'crew': 0, 'slots': 0}, 'capacity': 0, 'range': 0}], 'mounts': [{'symbol': 'MOUNT_GAS_SIPHON_I', 'name': 'string', 'description': 'string', 'strength': 0, 'deposits': ['QUARTZ_SAND'], 'requirements': {'power': 0, 'crew': 0, 'slots': 0}}], 'cargo': {'capacity': 0, 'units': 0, 'inventory': [{'symbol': 'string', 'name': 'string', 'description': 'string', 'units': 1}]}, 'fuel': {'current': 0, 'capacity': 0, 'consumed': {'amount': 0, 'timestamp': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}}}, 'transaction': {'waypointSymbol': 'string', 'shipSymbol': 'string', 'price': 1, 'agentSymbol': 'string', 'timestamp': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}})

    def test_get_ship(self):
        ret_obj = self.client.get_ship('string')
        self.assertEqual(ret_obj.dict(), {'symbol': 'string', 'registration': {'name': 'string', 'role': 'FABRICATOR', 'factionSymbol': 'string'}, 'nav': {'systemSymbol': 'string', 'waypointSymbol': 'string', 'route': {'destination': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departure': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departureTime': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc), 'arrival': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'status': 'IN_TRANSIT', 'flightMode': 'CRUISE'}, 'crew': {'current': 0, 'required': 0, 'capacity': 0, 'rotation': 'STRICT', 'morale': 0, 'wages': 0}, 'frame': {'symbol': 'FRAME_PROBE', 'name': 'string', 'description': 'string', 'condition': 0, 'moduleSlots': 0, 'mountingPoints': 0, 'fuelCapacity': 0, 'requirements': {'power': 0, 'crew': 0, 'slots': 0}}, 'reactor': {'symbol': 'REACTOR_SOLAR_I', 'name': 'string', 'description': 'string', 'powerOutput': 1, 'requirements': {'power': 0, 'crew': 0, 'slots': 0}, 'condition': 0}, 'engine': {'symbol': 'ENGINE_IMPULSE_DRIVE_I', 'name': 'string', 'description': 'string', 'requirements': {'power': 0, 'crew': 0, 'slots': 0}, 'speed': 1, 'condition': 0}, 'modules': [{'symbol': 'MODULE_MINERAL_PROCESSOR_I', 'name': 'string', 'description': 'string', 'requirements': {'power': 0, 'crew': 0, 'slots': 0}, 'capacity': 0, 'range': 0}], 'mounts': [{'symbol': 'MOUNT_GAS_SIPHON_I', 'name': 'string', 'description': 'string', 'strength': 0, 'deposits': ['QUARTZ_SAND'], 'requirements': {'power': 0, 'crew': 0, 'slots': 0}}], 'cargo': {'capacity': 0, 'units': 0, 'inventory': [{'symbol': 'string', 'name': 'string', 'description': 'string', 'units': 1}]}, 'fuel': {'current': 0, 'capacity': 0, 'consumed': {'amount': 0, 'timestamp': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}}})

    def test_get_ship_cargo(self):
        ret_obj = self.client.get_ship_cargo('string')
        self.assertEqual(ret_obj.dict(), {'capacity': 0, 'units': 0, 'inventory': [{'symbol': 'string', 'name': 'string', 'description': 'string', 'units': 1}]})

    def test_orbit_ship(self):
        ret_obj = self.client.orbit_ship('string')
        self.assertEqual(ret_obj.dict(), {'nav': {'systemSymbol': 'string', 'waypointSymbol': 'string', 'route': {'destination': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departure': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departureTime': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc), 'arrival': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'status': 'IN_TRANSIT', 'flightMode': 'CRUISE'}})

    def test_ship_refine(self):
        ret_obj = self.client.ship_refine('string', 'IRON')
        self.assertEqual(ret_obj.dict(), {'cargo': {'capacity': 0, 'units': 0, 'inventory': [{'symbol': 'string', 'name': 'string', 'description': 'string', 'units': 1}]}, 'cooldown': {'shipSymbol': 'string', 'totalSeconds': 0, 'remainingSeconds': 0, 'expiration': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'produced': [{'tradeSymbol': 'string', 'units': 0}], 'consumed': [{'tradeSymbol': 'string', 'units': 0}]})

    def test_create_chart(self):
        ret_obj = self.client.create_chart('string')
        self.assertEqual(ret_obj.dict(), {'chart': {'waypointSymbol': 'string', 'submittedBy': 'string', 'submittedOn': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'waypoint': {'symbol': 'string', 'type': 'PLANET', 'x': 0, 'y': 0, 'systemSymbol': 'string', 'orbitals': [{'symbol': 'string'}], 'faction': {'symbol': 'string', 'name': None, 'description': None, 'headquarters': None, 'traits': None}, 'traits': [{'symbol': 'UNCHARTED', 'name': 'string', 'description': 'string'}], 'chart': {'waypointSymbol': 'string', 'submittedBy': 'string', 'submittedOn': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}}})

    def test_get_ship_cooldown(self):
        ret_obj = self.client.get_ship_cooldown('string')
        self.assertEqual(ret_obj.dict(), {'shipSymbol': 'string', 'totalSeconds': 0, 'remainingSeconds': 0, 'expiration': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)})

    def test_dock_ship(self):
        ret_obj = self.client.dock_ship('string')        
        self.assertEqual(ret_obj.dict(), {'nav': {'systemSymbol': 'string', 'waypointSymbol': 'string', 'route': {'destination': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departure': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departureTime': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc), 'arrival': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'status': 'IN_TRANSIT', 'flightMode': 'CRUISE'}})

    def test_create_survey(self):
        ret_obj = self.client.create_survey('string')
        self.assertEqual(ret_obj.dict(), {'cooldown': {'shipSymbol': 'string', 'totalSeconds': 0, 'remainingSeconds': 0, 'expiration': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'surveys': [{'signature': 'string', 'symbol': 'string', 'deposits': [{'symbol': 'string'}], 'expiration': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc), 'size': 'SMALL'}]})

    def test_extract_resources(self):
        survey = models.Survey(**{
                "signature": "string",
                "symbol": "string",
                "deposits": [
                {
                    "symbol": "string"
                }
                ],
                "expiration": "2019-08-24T14:15:22Z",
                "size": "SMALL"
            })
        ret_obj = self.client.extract_resources('string', survey)
        self.assertEqual(ret_obj.dict(), {'cargo': {'capacity': 0, 'units': 0, 'inventory': [{'symbol': 'string', 'name': 'string', 'description': 'string', 'units': 1}]}, 'cooldown': {'shipSymbol': 'string', 'totalSeconds': 0, 'remainingSeconds': 0, 'expiration': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'extraction': {'shipSymbol': 'string'}})

    def test_jettison_cargo(self):
        ret_obj = self.client.jettison_cargo('string', 'string', 1)
        self.assertEqual(ret_obj.dict(), {'cargo': {'capacity': 0, 'units': 0, 'inventory': [{'symbol': 'string', 'name': 'string', 'description': 'string', 'units': 1}]}})

    def test_jump_ship(self):
        ret_obj = self.client.jump_ship('string', 'string')
        self.assertEqual(ret_obj.dict(), {'cooldown': {'shipSymbol': 'string', 'totalSeconds': 0, 'remainingSeconds': 0, 'expiration': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'nav': {'systemSymbol': 'string', 'waypointSymbol': 'string', 'route': {'destination': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departure': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departureTime': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc), 'arrival': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'status': 'IN_TRANSIT', 'flightMode': 'CRUISE'}})

    def test_navigate_ship(self):
        ret_obj = self.client.navigate_ship('string', 'string')
        self.assertEqual(ret_obj.dict(), {'nav': {'systemSymbol': 'string', 'waypointSymbol': 'string', 'route': {'destination': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departure': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departureTime': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc), 'arrival': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'status': 'IN_TRANSIT', 'flightMode': 'CRUISE'}, 'fuel': {'current': 0, 'capacity': 0, 'consumed': {'amount': 0, 'timestamp': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}}})

    def test_patch_ship_nav(self):
        ret_obj = self.client.patch_ship_nav('string', 'CRUISE')
        self.assertEqual(ret_obj.dict(), {'systemSymbol': 'string', 'waypointSymbol': 'string', 'route': {'destination': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departure': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departureTime': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc), 'arrival': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'status': 'IN_TRANSIT', 'flightMode': 'CRUISE'})

    def test_get_ship_nav(self):
        ret_obj = self.client.get_ship_nav('string')
        self.assertEqual(ret_obj.dict(), {'systemSymbol': 'string', 'waypointSymbol': 'string', 'route': {'destination': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departure': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departureTime': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc), 'arrival': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'status': 'IN_TRANSIT', 'flightMode': 'CRUISE'})

    def test_warp_ship(self):
        ret_obj = self.client.warp_ship('string', 'string')
        self.assertEqual(ret_obj.dict(), {'nav': {'systemSymbol': 'string', 'waypointSymbol': 'string', 'route': {'destination': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departure': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departureTime': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc), 'arrival': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'status': 'IN_TRANSIT', 'flightMode': 'CRUISE'}, 'fuel': {'current': 0, 'capacity': 0, 'consumed': {'amount': 0, 'timestamp': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}}})

    def test_sell_cargo(self):
        ret_obj = self.client.sell_cargo('string', 'string', 0)
        self.assertEqual(ret_obj.dict(), {'agent': {'accountId': 'string', 'symbol': 'string', 'headquarters': 'string', 'credits': 0}, 'transaction': {'waypointSymbol': 'string', 'shipSymbol': 'string', 'tradeSymbol': 'string', 'type': 'PURCHASE', 'units': 1, 'pricePerUnit': 1, 'totalPrice': 1, 'timestamp': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'cargo': {'capacity': 0, 'units': 0, 'inventory': [{'symbol': 'string', 'name': 'string', 'description': 'string', 'units': 1}]}})

    def test_scan_systems(self):
        ret_obj = self.client.scan_systems('string')
        self.assertEqual(ret_obj.dict(), {'cooldown': {'shipSymbol': 'string', 'totalSeconds': 0, 'remainingSeconds': 0, 'expiration': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'systems': [{'symbol': 'string', 'sectorSymbol': 'string', 'type': 'NEUTRON_STAR', 'x': 0, 'y': 0, 'distance': 0, 'factionSymbol': None}]})

    def test_scan_waypoints(self):
        ret_obj = self.client.scan_waypoints('string')
        self.assertEqual(ret_obj.dict(), {'cooldown': {'shipSymbol': 'string', 'totalSeconds': 0, 'remainingSeconds': 0, 'expiration': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'waypoints': [{'symbol': 'string', 'type': 'PLANET', 'x': 0, 'y': 0, 'systemSymbol': 'string', 'orbitals': [{'symbol': 'string'}], 'faction': {'symbol': 'string', 'name': None, 'description': None, 'headquarters': None, 'traits': None}, 'traits': [{'symbol': 'UNCHARTED', 'name': 'string', 'description': 'string'}], 'chart': {'waypointSymbol': 'string', 'submittedBy': 'string', 'submittedOn': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}}]})

    def test_scan_ships(self):
        ret_obj = self.client.scan_ships('string')
        self.assertEqual(ret_obj.dict(), {'ships': [{'symbol': 'string', 'registration': {'name': 'string', 'role': 'FABRICATOR', 'factionSymbol': 'string'}, 'nav': {'systemSymbol': 'string', 'waypointSymbol': 'string', 'route': {'destination': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departure': {'symbol': 'string', 'type': 'PLANET', 'systemSymbol': 'string', 'x': 0, 'y': 0}, 'departureTime': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc), 'arrival': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'status': 'IN_TRANSIT', 'flightMode': 'CRUISE'}, 'crew': None, 'frame': {'symbol': 'string', 'name': None, 'description': None, 'condition': None, 'moduleSlots': None, 'mountingPoints': None, 'fuelCapacity': None, 'requirements': None}, 'reactor': {'symbol': 'string', 'name': None, 'description': None, 'powerOutput': None, 'requirements': None, 'condition': None}, 'engine': {'symbol': 'string', 'name': None, 'description': None, 'requirements': None, 'speed': 1, 'condition': 0}, 'modules': None, 'mounts': [{'symbol': 'string', 'name': None, 'description': None, 'strength': None, 'deposits': None, 'requirements': None}], 'cargo': None, 'fuel': None}], 'cooldown': {'shipSymbol': 'string', 'totalSeconds': 0, 'remainingSeconds': 0, 'expiration': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}})

    def test_refuel_ship(self):
        ret_obj = self.client.refuel_ship('string')
        self.assertEqual(ret_obj.dict(), {'agent': {'accountId': 'string', 'symbol': 'string', 'headquarters': 'string', 'credits': 0}, 'fuel': {'current': 0, 'capacity': 0, 'consumed': {'amount': 0, 'timestamp': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}}})

    def test_purchase_cargo(self):
        ret_obj = self.client.purchase_cargo('string', 'string', 0)
        self.assertEqual(ret_obj.dict(), {'agent': {'accountId': 'string', 'symbol': 'string', 'headquarters': 'string', 'credits': 0}, 'transaction': {'waypointSymbol': 'string', 'shipSymbol': 'string', 'tradeSymbol': 'string', 'type': 'PURCHASE', 'units': 1, 'pricePerUnit': 1, 'totalPrice': 1, 'timestamp': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}, 'cargo': {'capacity': 0, 'units': 0, 'inventory': [{'symbol': 'string', 'name': 'string', 'description': 'string', 'units': 1}]}})

    def test_transfer_cargo(self):
        ret_obj = self.client.transfer_cargo('string', 'string', 'string', 0)
        self.assertEqual(ret_obj.dict(), {'cargo': {'capacity': 0, 'units': 0, 'inventory': [{'symbol': 'string', 'name': 'string', 'description': 'string', 'units': 1}]}})
