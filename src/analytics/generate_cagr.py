import sqlite3
import pandas as pd

from src.analytics.cagr import (
    revenue_cagr,
    pat_cagr,
    eps_cagr,
)

# Connect to database
conn = sqlite3.connect("data/nifty100.db")

# Read Profit & Loss
pl = pd.read_sql(
    "SELECT company_id, year, sales, net_profit, eps FROM profitandloss",
    conn
)

# Extract 4-digit year
pl["year_numeric"] = pd.to_numeric(
    pl["year"].str.extract(r"(\d{4})")[0],
    errors="coerce"
)

# Show invalid rows
invalid_rows = pl[pl["year_numeric"].isna()]

print("\nInvalid Year Rows:")
print(invalid_rows[["company_id", "year"]])

# Remove invalid rows
pl = pl.dropna(subset=["year_numeric"])

# Convert to integer
pl["year_numeric"] = pl["year_numeric"].astype(int)

# Sort data
pl = pl.sort_values(
    ["company_id", "year_numeric"]
)

# Default columns
pl["revenue_cagr_5yr"] = None
pl["pat_cagr_5yr"] = None
pl["eps_cagr_5yr"] = None

# Calculate CAGR
for company in pl["company_id"].unique():

    company_df = pl[
        pl["company_id"] == company
    ].copy()

    company_df = company_df.sort_values("year_numeric")

    company_df = company_df.reset_index()

for i in range(5, len(company_df)):

    current = company_df.loc[i]

    old = company_df.loc[i - 5]

    revenue, _ = revenue_cagr(
    old["sales"],
    current["sales"],
    5
)

pat, _ = pat_cagr(
    old["net_profit"],
    current["net_profit"],
    5
)

eps, _ = eps_cagr(
    old["eps"],
    current["eps"],
    5
)
original_index = current["index"]

pl.loc[original_index, "revenue_cagr_5yr"] = revenue
pl.loc[original_index, "pat_cagr_5yr"] = pat
pl.loc[original_index, "eps_cagr_5yr"] = eps

print(
    pl[
        pl["revenue_cagr_5yr"].notna()
    ][
        [
            "company_id",
            "year",
            "revenue_cagr_5yr",
            "pat_cagr_5yr",
            "eps_cagr_5yr",
        ]
    ].head(20)
)

conn.close()