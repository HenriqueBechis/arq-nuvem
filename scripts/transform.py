import pandas as pd

def transform_data():
    df = pd.read_csv('data/sales.csv')
    print('Data transformed successfully')
    return df
