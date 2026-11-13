import pandas as pd
import os

def my_load_csv(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    return pd.read_csv(file_path)

# src/data/load_data.py

from pathlib import Path
import pandas as pd


def my_load_data(data_dir: str | Path) -> dict[str, pd.DataFrame]:
    """Load CSV files needed for the pipeline."""

    data_dir = Path(data_dir)

    files = {
        "internet": "internet.csv",
        "phone": "phone.csv",
        "personal": "personal.csv",
        "contract": "contract.csv",
    }

    data = {}

    for name, filename in files.items():
        file_path = data_dir / filename
        data[name] = my_load_csv(file_path)
    return data