import pandas as pd
def my_build_target (df: pd.DataFrame):
    df = df.copy()
    df["churn"] = (
        df["end_date"].notna()
    ).astype(int)
    return df
