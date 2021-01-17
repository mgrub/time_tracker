import json


def get_config():
    """Read config file config.json

    Returns
    -------
    dict
        key-value pairs contained in config.json
    """
    with open("config.json", "r") as f:
        return json.load(f)
