import sqlite3
import pandas as pd
from src.analytics.cashflow_kpis import (
    free_cash_flow,
)

from src.analytics.cagr import (
    revenue_cagr,
    pat_cagr,
    eps_cagr,
)
from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    debt_to_equity,
    interest_coverage_ratio,
    asset_turnover,
)
from src.analytics.cashflow_kpis import (
    free_cash_flow,
)

from src.analytics.cagr import (
    revenue_cagr,
    pat_cagr,
    eps_cagr,
    calculate_company_cagr,
)

# Connect to database
conn = sqlite3.connect("data/nifty100.db")

# Read tables
pl = pd.read_sql("SELECT * FROM profitandloss", conn)
pl = pl.drop_duplicates(
    subset=["company_id", "year"],
    keep="first"
)
bs = pd.read_sql("SELECT * FROM balancesheet", conn)
bs = bs.drop_duplicates(
    subset=["company_id", "year"],
    keep="first"
)

# Merge on company_id and year
merged = pd.merge(
    pl,
    bs,
    on=["company_id", "year"],
    how="inner",
)

# Read Cash Flow table
cf = pd.read_sql(
    "SELECT * FROM cashflow",
    conn
)
# Remove duplicate company-year records
cf = cf.drop_duplicates(
    subset=["company_id", "year"],
    keep="first"
)

# Merge Cash Flow
merged = pd.merge(
    merged,
    cf,
    on=["company_id", "year"],
    how="left",
)
# Read sectors table
sectors = pd.read_sql(
    "SELECT company_id, broad_sector FROM sectors",
    conn
)
# Merge sectors
merged = pd.merge(
    merged,
    sectors,
    on="company_id",
    how="left",
)
# Convert year like "Mar 2015" -> 2015
"""merged["year_numeric"] = (
    merged["year"]
    .str.extract(r"(\d{4})")
    .astype(int)
)"""
pl["year_numeric"] = pl["year"].str.extract(r"(\d{4})")

print("Rows with invalid year:")
print(pl[pl["year_numeric"].isna()][["company_id", "year"]])

# Calculate Net Profit Margin
merged["net_profit_margin_pct"] = merged.apply(
    lambda row: net_profit_margin(
        row["net_profit"],
        row["sales"]
    ),
    axis=1
)
merged["operating_profit_margin_pct"] = merged.apply(
    lambda row: operating_profit_margin(
        row["operating_profit"],
        row["sales"],
    ),
    axis=1,
)

# Calculate ROE
merged["return_on_equity_pct"] = merged.apply(
    lambda row: return_on_equity(
        row["net_profit"],
        row["equity_capital"],
        row["reserves"]
    ),
    axis=1
)

# Calculate Debt-to-Equity
merged["debt_to_equity"] = merged.apply(
    lambda row: debt_to_equity(
        row["borrowings"],
        row["equity_capital"],
        row["reserves"]
    ),
    axis=1
)
# High Leverage Flag
merged["high_leverage_flag"] = (
    (merged["debt_to_equity"] > 5)
    &
    (merged["broad_sector"] != "Financials")
)

merged["return_on_capital_employed_pct"] = merged.apply(
    lambda row: return_on_capital_employed(
        row["operating_profit"],
        row["equity_capital"],
        row["reserves"],
        row["borrowings"],
    ),
    axis=1
)

merged["return_on_assets_pct"] = merged.apply(
    lambda row: return_on_assets(
        row["net_profit"],
        row["total_assets"],
    ),
    axis=1
)

merged["interest_coverage"] = merged.apply(
    lambda row: interest_coverage_ratio(
        row["operating_profit"],
        row["other_income"],
        row["interest"],
    ),
    axis=1
)

merged["asset_turnover"] = merged.apply(
    lambda row: asset_turnover(
        row["sales"],
        row["total_assets"],
    ),
    axis=1
)
merged["free_cash_flow"] = merged.apply(
    lambda row: free_cash_flow(
        row["operating_activity"],
        row["investing_activity"],
    ),
    axis=1,
)

# Earnings Per Share
merged["earnings_per_share"] = merged["eps"]

# Dividend Payout Ratio
merged["dividend_payout_ratio_pct"] = merged["dividend_payout"]

# Total Debt
merged["total_debt_cr"] = merged["borrowings"]

# Cash From Operations
merged["cash_from_operations_cr"] = merged["operating_activity"]

# Book Value Per Share
merged["book_value_per_share"] = merged.apply(
    lambda row: (
        (row["equity_capital"] + row["reserves"])
        / row["equity_capital"]
    )
    if row["equity_capital"] > 0
    else None,
    axis=1,
)

# Composite Quality Score
merged["composite_quality_score"] = (
    merged["return_on_equity_pct"].fillna(0)
    + merged["net_profit_margin_pct"].fillna(0)
    + merged["return_on_assets_pct"].fillna(0)
) / 3

# ======================================
# Calculate 5-Year CAGR for each company
# ======================================

# Select only required KPI columns
ratios_df = merged[
    [
        "company_id",
        "year",
        "net_profit_margin_pct",
        "operating_profit_margin_pct",
        "return_on_equity_pct",
        "return_on_capital_employed_pct",
        "return_on_assets_pct",
        "debt_to_equity",
        "interest_coverage",
        "asset_turnover",
        "free_cash_flow",
        "earnings_per_share",
        "book_value_per_share",
        "dividend_payout_ratio_pct",
        "total_debt_cr",
        "cash_from_operations_cr",
        "composite_quality_score",
    ]
].copy()

print("\nRows to Insert:", len(ratios_df))

# Save ratios into SQLite
ratios_df.to_sql(
    "financial_ratios",
    conn,
    if_exists="append",
    index=False,
)

print("financial_ratios table populated successfully!")
conn.close()

print("Merged Rows:", len(merged))

print("\nMerged Columns:")
print(merged.columns.tolist())

print("\nFirst 5 Records:")
print(
    merged[
        [
            "company_id",
            "year",
            "net_profit_margin_pct",
            "return_on_equity_pct",
            "return_on_capital_employed_pct",
            "return_on_assets_pct",
            "debt_to_equity",
            "interest_coverage",
            "asset_turnover",
        ]
    ].head()
)

