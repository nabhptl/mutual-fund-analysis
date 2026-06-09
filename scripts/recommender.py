import pandas as pd
import os

# Get project root directory
base_dir = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Read scorecard file
file_path = os.path.join(
    base_dir,
    'reports',
    'fund_scorecard.csv'
)

scorecard = pd.read_csv(file_path)

# Create risk grade based on Sharpe Ratio
scorecard['risk_grade'] = pd.cut(
    scorecard['sharpe_ratio'],
    bins=[-999, 0.8, 1.2, 999],
    labels=['Low', 'Moderate', 'High']
)

# Select desired risk appetite
risk = "High"      # Change to Low / Moderate / High

# Generate recommendations
recommendations = (
    scorecard[
        scorecard['risk_grade'].astype(str) == risk
    ]
    .sort_values(
        by='sharpe_ratio',
        ascending=False
    )
    .head(3)
)

print("\n===================================")
print(f"Top 3 Recommended Funds ({risk} Risk)")
print("===================================\n")

print(
    recommendations[
        [
            'amfi_code',
            'sharpe_ratio',
            'fund_score'
        ]
    ]
)

# Optional: Save recommendations
recommendations.to_csv(
    os.path.join(
        base_dir,
        'reports',
        'fund_recommendations.csv'
    ),
    index=False
)

print("\nRecommendations saved successfully.")