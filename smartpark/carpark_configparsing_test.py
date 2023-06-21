import unittest
import json
from simple_mqtt_carpark import CarPark
from config_parser import parse_config

class Test_ConfigParsing(unittest.TestCase):
    def test_parse_config(self):
        config_string = '''
        {
            "parking_lot": {
                "location": "Moondalup City Square Parking",
                "total_spaces": 192,
                "broker_host": "localhost",
                "broker_port": 1883
            }
        }
        '''
        # Parse the string
        data = json.loads(config_string)
        parking_lot = data["parking_lot"]

        self.assertEqual(parking_lot["location"], "Moondalup City Square Parking")
        self.assertEqual(parking_lot["total_spaces"], 192)
        self.assertEqual(parking_lot["broker_host"], "localhost")
        self.assertEqual(parking_lot["broker_port"], 1883)


if __name__ == '__main__':
    unittest.main()