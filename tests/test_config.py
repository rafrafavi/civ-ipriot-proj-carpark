
import unittest
import tomli
from parking_lot import parse_config

class TestConfigParsing(unittest.TestCase):
    def test_parse_config(self):
        config_string = '''
        [parking_lot]
        location = "Moondalup City Square Parking"
        total_spaces = 192
        broker_host = "localhost"
        broker_port = 1883
        '''
        config = tomli.loads(config_string)
        parking_lot = parse_config(config)
        self.assertEqual(parking_lot.location, "Moondalup City Square Parking")
        self.assertEqual(parking_lot.total_spaces, 192)