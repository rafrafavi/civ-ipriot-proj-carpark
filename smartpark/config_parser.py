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


def parse_config(file_path: str) -> dict:
    """Parse the config file and return the values as a dictionary"""
    with open(config_file) as file:
        config_data = json.load(file)

    carpark_config = config_data["CarParks"][0]

    # Parsing the carpark information
    parsed_config = {
        'name': carpark_config['name'],
        'total-spaces': carpark_config['total-spaces'],
        'total-cars': carpark_config['total-cars'],
        'location': carpark_config['location'],
        'topic-root': carpark_config['topic-root'],
        'topic-qualifier': carpark_config['topic-qualifier'],
        'broker': carpark_config['broker'],
        'port': carpark_config['port'],
        'Sensors': carpark_config['Sensors'],
        'Displays': carpark_config['Displays'],
    }

    return parsed_config


config_file = "config.json"
parsed_config = parse_config(config_file)

print(parsed_config)