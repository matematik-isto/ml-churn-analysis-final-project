import pandas as pd
from datetime import datetime
from src.utils.utils import my_normalize_string

def clean_contract(df:pd.DataFrame, future_date: datetime = datetime(2099, 1, 1) ):
    df = df.copy()
    colnames = [my_normalize_string(col) for col in df.columns]
    df.columns = colnames

#    df['begin_date'] = df['begin_date'].str.strip().str.lower().replace() -- add any business rule about unexpected values
    df['begin_date'] = pd.to_datetime(df['begin_date'], errors="coerce")
        
    df['end_date'] = df['end_date'].str.strip().str.lower().replace({"no":future_date, "yes":""})
    df['end_date'] = pd.to_datetime(df['end_date'], errors="coerce")
    df=df.drop_duplicates()
# Future improvement: impute missing values
    max_date = df['end_date'].max()
    # Total charges is blank when it is a new contract, likely. Replace by zero
    df.loc[ (df['total_charges'].str.strip()=='') & (df["end_date"]==max_date) ,'total_charges'] = '0' 
    df['total_charges']=pd.to_numeric(df['total_charges'], errors='coerce')
    return df

def clean_personal(df):
    df = df.copy()
    colnames = [my_normalize_string(col) for col in df.columns]
    df.columns = colnames
    df=df.drop_duplicates()
    return df

def clean_phone(df):
    df = df.copy()
    colnames = [my_normalize_string(col) for col in df.columns]
    df.columns = colnames
    df=df.drop_duplicates()
    return df

def clean_internet(df):
    df = df.copy()
    colnames = [my_normalize_string(col) for col in df.columns]
    df.columns = colnames
    df=df.drop_duplicates()
    return df

def clean_all_data(data: dict[str, pd.DataFrame] ):
    result = {}
    result["contract"] = clean_contract(data["contract"])
    result["personal"] = clean_personal(data["personal"])
    result["phone"] = clean_phone(data["phone"])
    result["internet"] = clean_internet(data["internet"])

    return result