import unittest

import tomli  # you can use toml, json,yaml, or ryo for your config file
#from parking_lot  import parse_config
import smartpark.parse_config as pc


class TestConfigParsing(unittest.TestCase):
    def test_parse_config_has_correct_location_and_spaces(self):
        config_string = '''
        [parking_lot]
        location = "Moondalup City Square Parking"
        total_spaces = 192
        broker_host = "localhost"
        broker_port = 1883
        '''
        config = tomli.loads(config_string)
        parking_lot = pc.parse_config(config)
        self.assertEqual(parking_lot['location'], "Moondalup City Square Parking")
        self.assertEqual(parking_lot['total_spaces'], 192)