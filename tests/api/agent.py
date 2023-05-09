import unittest

from spacetrader_wrapper import Client
from spacetrader_wrapper.config import TestConfig

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.client = Client('', config=TestConfig)
    
    def test_agent_data(self):
        agent = self.client.agent
        self.assertEqual(agent.accountId, 'string')
        self.assertEqual(agent.symbol, 'string')
        self.assertEqual(agent.headquarters, 'string')
        self.assertEqual(agent.credits, 0)