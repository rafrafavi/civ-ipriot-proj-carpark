import toml


def parse_config():
    with open('config.toml', 'r') as read_config:
        config = toml.load(read_config)
        return config

# Test 1: extracts data from 'config.toml' and returns config as dictionary.

# print(parse_config())
