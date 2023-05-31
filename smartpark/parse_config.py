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
import tomli
from pathlib import Path


def parse_config(config: dict) -> dict:
    """Parse the config file and return the values as a dictionary"""
    # Returns the configuration data in the format we want
    return {
        'location': config['location'],
        'total_spaces': config['total_spaces'],
        'broker_host': config['broker_host'],
        'broker_port': config['broker_port']
    }


def load_config(filename: str, section_name: str = "default") -> dict:
    # get actual file path, and load (ASCII-8) data from file
    file_data = Path(f"{filename}").read_text(encoding="utf-8")
    # convert TOML data from file into a dictionary
    config_dict = tomli.loads(file_data)
    # return the parsed data back from the TOML section: "section_name"
    return parse_config(config_dict[section_name])
