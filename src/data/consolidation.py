import pandas as pd
from src.data.clean_sources import clean_all_data
# orphan function
def my_merge_datasets(
        df1: pd.DataFrame,
        df2: pd.DataFrame,
        key: str = 'customer_id',
        how: str = 'left') -> pd. DataFrame:  
    return pd.merge(df1, df2, on = key, how = how)


def my_build_dataset(data: dict[str, pd.DataFrame]) -> pd.DataFrame:

    df = (
        data["contract"]
        .merge(data["personal"], on="customer_id", how="left")
        .merge(data["phone"],    on="customer_id",  how="left")
        .merge(data["internet"], on="customer_id", how="left")
    )
    return df

def my_prepare_dataset(data: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return my_build_dataset(clean_all_data(data))