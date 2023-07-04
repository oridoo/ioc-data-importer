import json
import os
import logging
from importlib import util as importlib_util
from typing import List, Dict


def valid_handlers(config: Dict[str, List[str]]) -> List[str]:
    """
    :param config: config dict
    :return: list of valid handlers from the config file
    """
    handlers = []
    for handler in config["handlers"]:
        if importlib_util.find_spec(f"src.handlers.{handler}"):
            handlers.append(handler)
            logging.debug(f"Found handler {handler}")
        else:
            logging.warning(f"Handler {handler} not found")
    return handlers


def default_config(path: str) -> Dict[str, Dict[str, str]]:
    base = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "user": "postgres",
            "password": "postgres",
            "database": "postgres"
        },
        "handlers": ["urlhaus", "openphish", "alienvault"]
    }
    with open(path, "w") as f:
        json.dump(base, f, indent=4)

    logging.info(f"Created default config file at {path}")
    return base


def read_config() -> Dict[str, Dict[str, str]]:
    path = os.path.join(os.path.dirname(__file__), os.pardir, "config.json")

    if not os.path.exists(path):
        logging.warning(f"Config file not found at {path}")
        return default_config(path)

    with open(path) as f:
        return json.load(f)


CONFIG = read_config()
