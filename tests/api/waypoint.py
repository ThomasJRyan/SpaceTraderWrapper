import unittest
import datetime

from spacetrader_wrapper import Client
from spacetrader_wrapper.config import TestConfig

class TestWaypoints(unittest.TestCase):
    def setUp(self):
        self.client = Client('', config=TestConfig)
    
    def test_list_waypoints(self):
        waypoints = self.client.list_waypoints('string')
        self.assertEqual(len(waypoints), 1)
        
        waypoint = waypoints[0]
        self.assertEqual(waypoint.dict(), {'symbol': 'string', 'type': 'PLANET', 'x': 0, 'y': 0, 'systemSymbol': 'string', 'orbitals': [{'symbol': 'string'}], 'faction': {'symbol': 'string', 'name': None, 'description': None, 'headquarters': None, 'traits': None}, 'traits': [{'symbol': 'UNCHARTED', 'name': 'string', 'description': 'string'}], 'chart': {'waypointSymbol': 'string', 'submittedBy': 'string', 'submittedOn': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}})
        
    def test_get_waypoint(self):
        waypoint = self.client.get_waypoint('string', 'string')
        self.assertEqual(waypoint.dict(), {'symbol': 'string', 'type': 'PLANET', 'x': 0, 'y': 0, 'systemSymbol': 'string', 'orbitals': [{'symbol': 'string'}], 'faction': {'symbol': 'string', 'name': None, 'description': None, 'headquarters': None, 'traits': None}, 'traits': [{'symbol': 'UNCHARTED', 'name': 'string', 'description': 'string'}], 'chart': {'waypointSymbol': 'string', 'submittedBy': 'string', 'submittedOn': datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc)}})