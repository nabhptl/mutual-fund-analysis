"""
Live NAV Fetch Module

Fetches latest NAV information
from AMFI data sources.
"""



import requests
import pandas as pd

scheme_codes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in scheme_codes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            f"data/raw/{name}.csv",
            index=False
        )

        print(f"{name} saved successfully")
    else:
        print(f"Failed for {name}")