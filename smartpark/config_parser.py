"""A class or function to parse the config file and return the values as a dictionary.

The config file itself can be any of the following formats:

- ryo: means 'roll your own' and is a simple text file with key-value pairs separated by an equals sign. For example:
```
location = "Moondalup City Square Parking"
number_of_spaces = 192
```
**you** read the file and parse it into a dictionary.
- json: a json file with key-value pairs. For example:
```json
{location: "Moondalup City Square Parking", number_of_spaces: 192}
```
json is built in to python, so you can use the json module to parse it into a dictionary.
- toml: a toml file with key-value pairs. For example:
```toml
[location]
name = "Moondalup City Square Parking"
spaces = 192
```
toml is part of the standard library in python 3.11, otherwise you need to install tomli to parse it into a dictionary.
```bash
python -m pip install tomli
```
see [realpython.com](https://realpython.com/python-toml/) for more info.

Finally, you can use `yaml` if you prefer.

"""
import json


def parse_config(config_file):
    """Parse the config file and return the values as a dictionary"""
    with open(config_file) as file:
        config_data = json.load(file)

    parsed_config = {}

    # Parsing the carpark information
    parsed_config['CarParks'] = []
    for car_park in config_data['CarParks']:
        car_park_info = {}
        car_park_info['name'] = car_park['name']
        car_park_info['total-spaces'] = car_park['total-spaces']
        car_park_info['total-cars'] = car_park['total-cars']
        car_park_info['location'] = car_park['location']
        car_park_info['broker'] = car_park['broker']
        car_park_info['port'] = car_park['port']

        # Parsing the info for sensors inside the carpark
        car_park_info['Sensors'] = []
        for sensor in car_park['Sensors']:
            sensor_info = {}
            sensor_info['name'] = sensor['name']
            sensor_info['type'] = sensor['type']
            car_park_info['Sensors'].append(sensor_info)

        # Parsing the display info inside the carpark
        car_park_info['Displays'] = []
        for display in car_park['Displays']:
            display_info = {}
            display_info['name'] = display['name']
            car_park_info['Displays'].append(display_info)

        parsed_config['CarParks'].append(car_park_info)

    return parsed_config


config_file = "config.json"
parsed_config = parse_config(config_file)

print(parsed_config)