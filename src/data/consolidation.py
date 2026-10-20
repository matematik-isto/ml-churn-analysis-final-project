import pandas as pd
def my_merge_datasets(
        df1: pd.DataFrame,
        df2: pd.DataFrame,
        key: str = 'customer_id',
        how: str = 'outer') -> pd. DataFrame:
    
    return pd.merge(df1, df1, on = key, how = how)
