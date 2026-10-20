import pandas as pd
import os

def my_load_csv(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    return pd.read_csv(file_path)