from pathlib import Path
from .data_path_settings import return_data_path
from .mini_utils import *
from .seed_file import *

# Constants
DATA_PATH = Path(return_data_path())
CSV, DIR, ALL = "csv", "dir", "all"
SEED_OK, SEED_FAIL = "✔", "❌"
SEED_MISSING = "SEED X"

def show_all_datasets(file_type=CSV, show=True, wise="shape"):
    datasets = []

    for obj in DATA_PATH.iterdir():
        if file_type == CSV and obj.suffix == ".csv":
            seed_status = SEED_OK if check_data_mini(obj.name) else SEED_FAIL
            try:
                shape, cls, desc = (
                    read_seed_extended(obj.name) if seed_status == SEED_OK else ("?", "?", "?")
                )
            except Exception as e:
                shape, cls, desc = "?", "?", "?"
                print(f"Error reading seed for {obj.name}: {e}")

            item_data = {"shape": shape, "columns": cls, "cls": cls, "desc": desc}
            if seed_status == SEED_FAIL:
                item_data[wise] = SEED_MISSING
            item_data["seed"] = seed_status
            datasets.append(f"{obj.name} -: {item_data[wise]}")

        elif file_type == DIR and obj.is_dir():
            datasets.append(obj.name)
        elif file_type == ALL:
            datasets.append(obj.name)

    return display_recursive(datasets) if show else datasets


def get_all_exts():
    exts = {".folder" if not Path(f).suffix else Path(f).suffix for f in DATA_PATH.iterdir()}
    return list(exts)


def count_files():
    exts = get_all_exts()
    ext_count = {ext.lstrip("."): 0 for ext in exts}

    for obj in DATA_PATH.iterdir():
        ext = ".folder" if not obj.suffix else obj.suffix
        if ext in exts:
            ext_count[ext.lstrip(".")] += 1

    for ext, count in ext_count.items():
        print(f"{ext} - {count}")


def list_all_files(file_type="csv", connected=True):
    files = []
    for obj in DATA_PATH.iterdir():
        name = connect(obj.name) if connected else obj.name
        if file_type == CSV and obj.suffix == ".csv":
            files.append(name)
        elif file_type == DIR and obj.is_dir():
            files.append(name)
        elif file_type == ALL:
            files.append(name)
    return files
