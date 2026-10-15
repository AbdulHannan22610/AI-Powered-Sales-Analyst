import pandas as pd

def clean_data(df):
    df["total_sales"] = df["quantity"] * df["unit_price"] * (1 - df["discount"]/100)
    return df