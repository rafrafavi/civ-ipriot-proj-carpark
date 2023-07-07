import json
import toml
import os


def convert_config_to_toml():
    """
    Converts the configuration from JSON to TOML format and writes it to the config.toml file.
    """
    # Check if the config.toml file already exists
    if not os.path.isfile('config.toml'):
        # If the file doesn't exist, create an empty one
        with open('config.toml', 'w') as f:
            f.write('')

    # Read the contents of the config.json file
    with open('config.json', 'r') as f:
        config_data = json.load(f)

    # Convert the JSON data to TOML format
    toml_data = toml.dumps(config_data)

    # Write the TOML data to the config.toml file, overwriting any existing content
    with open('config.toml', 'w') as f:
        f.write(toml_data)


# Call the function to convert the configuration to TOML format
convert_config_to_toml()
