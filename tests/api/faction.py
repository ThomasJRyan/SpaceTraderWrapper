import unittest
import datetime

from spacetrader_wrapper import Client
from spacetrader_wrapper.config import TestConfig

class TestFactions(unittest.TestCase):
    def setUp(self):
        self.client = Client('', config=TestConfig)
    
    def test_list_factions(self):
        factions = self.client.list_factions()
        self.assertEqual(len(factions), 1)
        
        faction = factions[0]
        self.assertEqual(faction.dict(), {'symbol': 'string', 'name': 'string', 'description': 'string', 'headquarters': 'string', 'traits': [{'symbol': 'BUREAUCRATIC', 'name': 'string', 'description': 'string'}]})
        
    def test_get_faction(self):
        faction = self.client.get_faction('string')
        self.assertEqual(faction.dict(), {'symbol': 'string', 'name': 'string', 'description': 'string', 'headquarters': 'string', 'traits': [{'symbol': 'BUREAUCRATIC', 'name': 'string', 'description': 'string'}]})