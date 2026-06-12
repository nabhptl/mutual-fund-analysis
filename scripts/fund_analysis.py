"""
Fund Analysis Module

Calculates performance metrics,
risk measures, and generates reports.
"""



import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("========== FUND HOUSES ==========")
print(df["fund_house"].unique())

print("\n========== CATEGORIES ==========")
print(df["category"].unique())

print("\n========== SUB-CATEGORIES ==========")
print(df["sub_category"].unique())

print("\n========== RISK CATEGORIES ==========")
print(df["risk_category"].unique())

print("\n========== COUNTS ==========")
print("Fund Houses:", df["fund_house"].nunique())
print("Categories:", df["category"].nunique())
print("Sub-Categories:", df["sub_category"].nunique())
print("Risk Categories:", df["risk_category"].nunique())