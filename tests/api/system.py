import unittest

from spacetrader_wrapper import Client
from spacetrader_wrapper.config import TestConfig

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.client = Client('', config=TestConfig)
    
    def test_list_systems(self):
        systems = self.client.list_systems()
        self.assertEqual(len(systems), 1)
        
        system = systems[0]
        self.assertEqual(system.dict(), {'symbol': 'string', 'sectorSymbol': 'string', 'type': 'NEUTRON_STAR', 'x': 0, 'y': 0, 'waypoints': [{'symbol': 'string', 'type': 'PLANET', 'x': 0, 'y': 0, 'systemSymbol': None, 'orbitals': None, 'faction': None, 'traits': None, 'chart': None}], 'factions': [{'symbol': 'string', 'name': None, 'description': None, 'headquarters': None, 'traits': None}]})
        
    def test_get_system(self):
        system = self.client.get_system('string')
        self.assertEqual(system.dict(), {'symbol': 'string', 'sectorSymbol': 'string', 'type': 'NEUTRON_STAR', 'x': 0, 'y': 0, 'waypoints': [{'symbol': 'string', 'type': 'PLANET', 'x': 0, 'y': 0, 'systemSymbol': None, 'orbitals': None, 'faction': None, 'traits': None, 'chart': None}], 'factions': [{'symbol': 'string', 'name': None, 'description': None, 'headquarters': None, 'traits': None}]})