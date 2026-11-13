import pandas as pd
# orphan function
def my_merge_datasets(
        df1: pd.DataFrame,
        df2: pd.DataFrame,
        key: str = 'customer_id',
        how: str = 'left') -> pd. DataFrame:
    
    return pd.merge(df1, df2, on = key, how = how)



def my_build_dataset(
    data: dict[str, pd.DataFrame],
) -> pd.DataFrame:

    contract = data["contract"]
    personal = data["personal"]
    phone = data["phone"]
    internet = data["internet"]

    df = (
        contract
        .merge(personal, on="customer_id", how="left")
        .merge(phone, on="product_id", how="left")
        .merge(internet, on="customer_id", how="left")
    )

    return df