import json
import sys
import os
import unittest

# Add the parent directory to sys.path to recognise import
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from displays.config_parser import ConfigParser
class TestConfigParser(unittest.TestCase):
    def test_convert_json_to_toml(self):
        # Test case for converting JSON to TOML
        json_data = {
            "CarParks": [
                {
                    "name": "raf-park-international",
                    "total-spaces": 130,
                    "total-cars": 0,
                    "location": "moondalup",
                    "broker": "localhost",
                    "port": 1883,
                    "Sensors": [
                        {
                            "name": "sensor1",
                            "type": "entry"
                        },
                        {
                            "name": "sensor2",
                            "type": "exit"
                        }
                    ],
                    "Displays": [
                        {
                            "name": "display1"
                        }
                    ]
                }
            ]
        }

        # Write the JSON data to the config.json file
        with open('config.json', 'w') as f:
            json.dump(json_data, f)

        # Convert JSON to TOML
        ConfigParser.parse_config()

        # Verify if the config.toml file exists and has valid TOML format
        self.assertTrue(os.path.isfile('config.toml'))
        with open('config.toml', 'r') as f:
            toml_data = f.read()
            # Check if the toml_data is properly formatted TOML
            self.assertTrue(toml_data.startswith('[[CarParks]]'))


if __name__ == '__main__':
    unittest.main()
