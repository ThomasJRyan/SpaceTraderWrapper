import unittest

from spacetrader_wrapper import Client
from spacetrader_wrapper.config import TestConfig

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.client = Client('', config=TestConfig)
    
    def test_get_agent(self):
        agent = self.client.agent
        self.assertEqual(agent.accountId, 'string')
        self.assertEqual(agent.symbol, 'string')
        self.assertEqual(agent.headquarters, 'string')
        self.assertEqual(agent.credits, 0)
        
    def test_register_agent(self):
        client = Client.register("string", "COSMIC", TestConfig())
        self.assertIsInstance(client, Client)