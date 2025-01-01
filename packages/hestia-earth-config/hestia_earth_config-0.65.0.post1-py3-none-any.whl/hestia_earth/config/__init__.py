import os
import json
from typing import Union
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_config(node_type: Union[str]):
    try:
        with open(os.path.join(CURRENT_DIR, f"{node_type}.json"), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise Exception(f"Invalid type {node_type}.")
