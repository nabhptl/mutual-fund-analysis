# Mutual Fund Analytics Platform

## Data Dictionary

This document describes the datasets, columns, data types, and their meanings used in the Mutual Fund Analytics Platform project.


# 01_fund_master.csv

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | TEXT | Unique mutual fund scheme code |
| fund_house | TEXT | AMC name |
| scheme_name | TEXT | Official scheme name |
| category | TEXT | Equity, Debt, Hybrid |
| sub_category | TEXT | Large Cap, Mid Cap, Small Cap, etc. |
| plan | TEXT | Direct or Regular |
| launch_date | DATE | Fund launch date |
| benchmark | TEXT | Benchmark index |
| expense_ratio_pct | REAL | Expense ratio (%) |
| exit_load_pct | REAL | Exit load (%) |
| fund_manager | TEXT | Fund manager name |
| risk_category | TEXT | Risk category |
| sebi_category_code | TEXT | SEBI category code |


# 02_nav_history.csv

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | TEXT | Mutual fund scheme code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |


### Added During Cleaning

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| daily_return_pct | REAL | Daily percentage return calculated from NAV |


# 07_scheme_performance.csv

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| return_1yr_pct | REAL | 1-year return (%) |
| return_3yr_pct | REAL | 3-year CAGR (%) |
| return_5yr_pct | REAL | 5-year CAGR (%) |
| benchmark_3yr_pct | REAL | Benchmark return (%) |
| alpha | REAL | Excess return above benchmark |
| beta | REAL | Market sensitivity |
| sharpe_ratio | REAL | Risk-adjusted return |
| sortino_ratio | REAL | Downside risk-adjusted return |
| std_dev_ann_pct | REAL | Annualized volatility |
| max_drawdown_pct | REAL | Maximum loss from peak |
| morningstar_rating | INTEGER | Rating from 1–5 |


# 08_investor_transactions.csv

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| investor_id | TEXT | Investor unique ID |
| transaction_date | DATE | Transaction date |
| amfi_code | TEXT | Fund code |
| transaction_type | TEXT | SIP, Lumpsum, Redemption |
| amount_inr | INTEGER | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | T30 or B30 city |
| age_group | TEXT | Investor age group |
| gender | TEXT | Male or Female |
| annual_income_lakh | REAL | Annual income |
| payment_mode | TEXT | Payment method |
| kyc_status | TEXT | KYC verification status |



# Data Cleaning Rules Applied

## NAV Dataset
- Converted date to datetime
- Removed duplicate records
- Removed invalid NAV values
- Forward-filled missing NAV values
- Calculated daily returns

## Transactions Dataset
- Standardized transaction types
- Removed invalid transaction amounts
- Standardized KYC status values
- Removed duplicates

## Performance Dataset
- Converted return columns to numeric
- Validated expense ratio range
- Identified negative Sharpe ratios