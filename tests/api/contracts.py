import unittest
import datetime

from spacetrader_wrapper import Client
from spacetrader_wrapper.config import TestConfig


class TestContracts(unittest.TestCase):
    def setUp(self):
        self.client = Client("", config=TestConfig)

    def test_list_contracts(self):
        contracts = self.client.list_contracts()
        self.assertEqual(len(contracts), 1)
        contract = contracts[0]
        self.assertEqual(
            contract.dict(),
            {
                "id": "string",
                "factionSymbol": "string",
                "type": "PROCUREMENT",
                "terms": {
                    "deadline": datetime.datetime(
                        2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                    ),
                    "payment": {"onAccepted": 0, "onFulfilled": 0},
                    "deliver": [
                        {
                            "tradeSymbol": "string",
                            "destinationSymbol": "string",
                            "unitsRequired": 0,
                            "unitsFulfilled": 0,
                        }
                    ],
                },
                "accepted": False,
                "fulfilled": False,
                "expiration": datetime.datetime(
                    2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                ),
            },
        )

    def test_get_contract(self):
        contract = self.client.get_contract("string")
        self.assertEqual(
            contract.dict(),
            {
                "id": "string",
                "factionSymbol": "string",
                "type": "PROCUREMENT",
                "terms": {
                    "deadline": datetime.datetime(
                        2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                    ),
                    "payment": {"onAccepted": 0, "onFulfilled": 0},
                    "deliver": [
                        {
                            "tradeSymbol": "string",
                            "destinationSymbol": "string",
                            "unitsRequired": 0,
                            "unitsFulfilled": 0,
                        }
                    ],
                },
                "accepted": False,
                "fulfilled": False,
                "expiration": datetime.datetime(
                    2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                ),
            },
        )

    def test_accept_contract(self):
        contract = self.client.accept_contract("string")
        self.assertEqual(
            contract.dict(),
            {
                "agent": {
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": 0,
                },
                "contract": {
                    "id": "string",
                    "factionSymbol": "string",
                    "type": "PROCUREMENT",
                    "terms": {
                        "deadline": datetime.datetime(
                            2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                        ),
                        "payment": {"onAccepted": 0, "onFulfilled": 0},
                        "deliver": [
                            {
                                "tradeSymbol": "string",
                                "destinationSymbol": "string",
                                "unitsRequired": 0,
                                "unitsFulfilled": 0,
                            }
                        ],
                    },
                    "accepted": False,
                    "fulfilled": False,
                    "expiration": datetime.datetime(
                        2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                    ),
                },
                "cargo": None,
            },
        )

    def test_deliver_contract(self):
        contract = self.client.deliver_contract("string", "string", "string", 0)
        self.assertEqual(
            contract.dict(),
            {
                "agent": None,
                "contract": {
                    "id": "string",
                    "factionSymbol": "string",
                    "type": "PROCUREMENT",
                    "terms": {
                        "deadline": datetime.datetime(
                            2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                        ),
                        "payment": {"onAccepted": 0, "onFulfilled": 0},
                        "deliver": [
                            {
                                "tradeSymbol": "string",
                                "destinationSymbol": "string",
                                "unitsRequired": 0,
                                "unitsFulfilled": 0,
                            }
                        ],
                    },
                    "accepted": False,
                    "fulfilled": False,
                    "expiration": datetime.datetime(
                        2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                    ),
                },
                "cargo": {
                    "capacity": 0,
                    "units": 0,
                    "inventory": [
                        {
                            "symbol": "string",
                            "name": "string",
                            "description": "string",
                            "units": 1,
                        }
                    ],
                },
            },
        )

    def test_fulfill_contract(self):
        contract = self.client.fulfill_contract("string")
        self.assertEqual(
            contract.dict(),
            {
                "agent": {
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": 0,
                },
                "contract": {
                    "id": "string",
                    "factionSymbol": "string",
                    "type": "PROCUREMENT",
                    "terms": {
                        "deadline": datetime.datetime(
                            2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                        ),
                        "payment": {"onAccepted": 0, "onFulfilled": 0},
                        "deliver": [
                            {
                                "tradeSymbol": "string",
                                "destinationSymbol": "string",
                                "unitsRequired": 0,
                                "unitsFulfilled": 0,
                            }
                        ],
                    },
                    "accepted": False,
                    "fulfilled": False,
                    "expiration": datetime.datetime(
                        2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
                    ),
                },
                "cargo": None,
            },
        )
