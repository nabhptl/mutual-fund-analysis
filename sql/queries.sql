#Q1
SELECT
fund_house,
SUM(aum_crore)
FROM fact_performance
GROUP BY fund_house
ORDER BY SUM(aum_crore) DESC
LIMIT 5;

#Q2
SELECT
strftime('%Y-%m', nav_date),
AVG(nav)
FROM fact_nav
GROUP BY 1;

#Q3
SELECT
state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

#Q4
SELECT
scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

#Q5
SELECT
scheme_name,
expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;

#Q6
SELECT
category,
COUNT(*)
FROM dim_fund
GROUP BY category;

#Q7
SELECT
scheme_name,
return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;

#Q8
SELECT
AVG(amount_inr)
FROM fact_transactions
WHERE transaction_type='SIP';

#Q9
SELECT
state,
SUM(amount_inr)
FROM fact_transactions
GROUP BY state;

#Q10
SELECT
transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;