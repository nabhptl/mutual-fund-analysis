# Mutual Fund Analysis & Performance Dashboard

## Project Overview

This project was developed as part of the Bluestock Fintech Data Analytics Capstone Program.

The objective of this project is to perform end-to-end analysis of Indian Mutual Fund data using Python, SQL, SQLite, and Power BI. The project covers data ingestion, data cleaning, exploratory data analysis, performance analytics, advanced risk analysis, fund recommendation, and interactive dashboard development.

---

## Business Objectives

* Analyze mutual fund industry trends and growth.
* Compare fund performance across multiple schemes.
* Measure risk-adjusted returns using financial metrics.
* Evaluate fund performance against benchmark indices.
* Understand investor behavior and SIP patterns.
* Build a fund recommendation system.
* Create an interactive Power BI dashboard for business users.

---

## Dataset Description

The project uses multiple datasets related to the Indian Mutual Fund industry.

### Datasets

| File                         | Description                    |
| ---------------------------- | ------------------------------ |
| 01_fund_master.csv           | Mutual fund master information |
| 02_nav_history.csv           | Historical NAV data            |
| 03_aum_by_fund_house.csv     | Assets Under Management by AMC |
| 04_monthly_sip_inflows.csv   | Monthly SIP inflow data        |
| 05_category_inflows.csv      | Category-wise inflows          |
| 06_industry_folio_count.csv  | Industry folio statistics      |
| 07_scheme_performance.csv    | Fund performance metrics       |
| 08_investor_transactions.csv | Investor transaction data      |
| 09_portfolio_holdings.csv    | Fund portfolio holdings        |
| 10_benchmark_indices.csv     | Benchmark index data           |

---

## Technology Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQLite
* SQL
* Power BI
* Git & GitHub

---

## Project Structure

```text
mutual-fund-analysis/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── data_ingestion.py
│   ├── fund_analysis.py
│   ├── live_nav_fetch.py
│   ├── recommender.py
│   └── run_pipeline.py
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── Final_Report.pdf
│   └── Bluestock_MF_Presentation.pptx
│
└── README.md
```

---

## Key Performance Metrics

The following metrics were calculated:

* Daily Returns
* CAGR (1 Year, 3 Year, 5 Year)
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Tracking Error
* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-Day Sharpe Ratio
* Herfindahl-Hirschman Index (HHI)

---

## Power BI Dashboard Pages

### Page 1 – Industry Overview

* Total AUM
* SIP Inflows
* Total Folios
* Total Schemes
* Industry AUM Trend
* AUM by AMC

### Page 2 – Fund Performance

* Return vs Risk Analysis
* Fund Scorecard
* Benchmark Comparison
* NAV Trend Analysis

### Page 3 – Investor Analytics

* State-wise Investments
* SIP/Lumpsum/Redemption Analysis
* Age Group Analysis
* Transaction Trends

### Page 4 – SIP & Market Trends

* SIP vs NIFTY Trend
* Category Inflow Heatmap
* Top Categories by Net Inflow

---

## Advanced Analytics

### Risk Analysis

* Historical VaR
* CVaR
* Rolling Sharpe Ratio

### Investor Analysis

* Cohort Analysis
* SIP Continuity Analysis
* At-Risk Investor Detection

### Portfolio Analysis

* Sector Concentration
* HHI Score

### Recommendation Engine

* Risk-based Mutual Fund Recommendation System

---

## Key Insights

* Equity funds generated higher long-term returns compared to debt funds.
* SIP inflows showed consistent growth during the analysis period.
* Large-cap and flexi-cap categories attracted significant investor interest.
* Funds with higher Sharpe Ratios delivered better risk-adjusted performance.
* Certain investors displayed irregular SIP patterns and were identified as at-risk.
* Portfolio concentration varied significantly across funds based on HHI scores.

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/nabhptl/mutual-fund-analysis.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Complete Pipeline

```bash
python scripts/run_pipeline.py
```

### Launch Dashboard

Open:

```text
dashboard/bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

---

## Project Deliverables

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx
* Power BI Dashboard (.pbix)
* Fund Scorecard
* Risk Analytics Reports
* Fund Recommendation Engine
* GitHub Repository

---

## Author

**Nabh Patel**

Bluestock Fintech Capstone Project

Data Analytics | Python | SQL | Power BI
