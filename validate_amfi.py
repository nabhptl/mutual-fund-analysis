import pandas as pd

master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

master_codes = set(master["amfi_code"])
nav_codes = set(nav["amfi_code"])

missing = master_codes - nav_codes

print("Missing Codes:", len(missing))
print(missing)