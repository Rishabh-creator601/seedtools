import os
import json
from pathlib import Path

CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".seedtools")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def _load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def _save_config(data):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)

def return_data_path():
    config = _load_config()
    return config.get("DATA_PATH")

def configure_data_path(new_path, create_new_path=True):
    if os.path.exists(new_path):
        _save_config({"DATA_PATH": new_path})
        print(f"Path set to: {new_path}")

    elif not os.path.exists(new_path) and create_new_path:
        Path(new_path).mkdir(parents=True, exist_ok=True)
        _save_config({"DATA_PATH": new_path})
        print(f"Path set to: {new_path}")

    else:
        print("Path not found ... please create that path first")

def reset_path():
    """Resets to default path in user's home directory."""
    default_path = os.path.join(os.path.expanduser("~"), ".data")
    configure_data_path(default_path)
