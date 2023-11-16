import unittest

import tomli  # you can use toml, json,yaml, or ryo for your config file

import smartpark.config_parser as cp

from smartpark import carpark


with open("config.toml", "r") as file:
    config_string = file.read()

config = tomli.loads(config_string)


class TestConfigParsing(unittest.TestCase):
    def test_config_parser_has_correct_location_and_spaces(self):
        config_string = '''
        [parking_lot]
        location = "Moondalup City Square Parking"
        total_spaces = 192
        broker_host = "localhost"
        broker_port = 1883
        '''
        config = tomli.loads(config_string)
        parking_lot = cp.parse_config(config)
        self.assertEqual(parking_lot['location'], "Moondalup City Square Parking")
        self.assertEqual(parking_lot['total_spaces'], 192)

    def test_no_negative_spaces(self):
        parking_lot = simple_mqtt_carpark("Test Location", 2, "localhost", 1883)
        parking_lot.available_spaces = 0
        parking_lot.enter()
        parking_lot.enter()
        self.assertEqual(parking_lot.available_spaces, 0)
        parking_lot.exit()
        parking_lot.exit()
        parking_lot.exit()
        self.assertEqual(parking_lot.available_spaces, 1)
