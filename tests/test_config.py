import logging
import unittest

import tomli  # you can use toml, json,yaml, or ryo for your config file

import smartpark.parse_config as pc


class TestConfigParsing(unittest.TestCase):
    def test_parse_config_has_correct_location_and_spaces(self):
        # configuration string to use in test
        config_string = '''
        [parking_lot]
        location = "Moondalup City Square Parking"
        total_spaces = 192
        broker_host = "localhost"
        broker_port = 1883
        '''
        config = tomli.loads(config_string)  # converts config_string to a dictionary
        config_section = config["parking_lot"]  # get the (parking_lot) key's values
        parking_lot = pc.parse_config(config_section)  # parse the values into desired format

        # assert the tests
        self.assertEqual(parking_lot['location'], "Moondalup City Square Parking")
        self.assertEqual(parking_lot['total_spaces'], 192)

    def test_load_config_has_correct_location_and_spaces(self):
        filename = "../config.toml"
        config = pc.load_config(filename, "parking_lot")
        parking_lot = pc.parse_config(config)
        self.assertEqual(parking_lot['location'], "Moondalup City Square Parking")
        self.assertEqual(parking_lot['total_spaces'], 192)
