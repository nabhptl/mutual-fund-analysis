"""
Data Ingestion Module

Loads raw mutual fund datasets,
performs initial validation,
and prepares data for analysis.
"""


import pandas as pd
import os

folder = "data/raw"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

for file in files:

    print("="*60)
    print("FILE:", file)

    df = pd.read_csv(os.path.join(folder,file))

    print("\nShape:")
    

    print("\nDtypes:")
    

    print("\nHead:")
    

    print("\nMissing Values:")
    print(df.isnull().sum())