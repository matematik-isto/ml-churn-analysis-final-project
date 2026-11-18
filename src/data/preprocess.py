import pandas as pd

def my_preprocess_data(df: pd.DataFrame, target_col: str = 'churn') -> pd.DataFrame:

    # drop ids if present
    drop_cols = ['customer_id','customerid','monthly_charges'] # monthly charges and total_charges have a high correlation
    df = df.drop(columns= drop_cols, errors = 'ignore')

    # define Churn column 
    # target to 0/1 if it's Yes/No
    if target_col in df.columns and df[target_col].dtype == "object":
        df[target_col] = df[target_col].str.strip().map({"No": 0, "Yes": 1})
    # TotalCharges often has blanks in this dataset -> coerce to float
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Selecting columns with missing values because of no service hired
    missing_internet = [
    'internet_service',
        'online_security',
        'online_backup',
        'device_protection',
        'tech_support',
        'streaming_tv',
        'streaming_movies',
    ]
    missing_phone = ['multiple_lines']

    # Replacing NA with a description
    for column in missing_internet:
        df[column]=df[column].fillna('No internet service')
    for column in missing_phone:
        df[column]=df[column].fillna('No phone service')

    return df


