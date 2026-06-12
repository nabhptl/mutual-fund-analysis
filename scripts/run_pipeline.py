import os

print("Running Data Ingestion...")
os.system("python scripts/data_ingestion.py")

print("Running Fund Analysis...")
os.system("python scripts/fund_analysis.py")

print("Running Live NAV Fetch...")
os.system("python scripts/live_nav_fetch.py")

print("Running Recommender...")
os.system("python scripts/recommender.py")

print("Pipeline Completed Successfully.")