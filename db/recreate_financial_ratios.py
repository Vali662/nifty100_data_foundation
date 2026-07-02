import sqlite3

conn = sqlite3.connect("data/nifty100.db")

cursor = conn.cursor()

# Delete old table
cursor.execute("DROP TABLE IF EXISTS financial_ratios")

# Create new table
cursor.execute("""
CREATE TABLE financial_ratios (

    company_id TEXT,
    year TEXT,

    net_profit_margin_pct REAL,
    operating_profit_margin_pct REAL,

    return_on_equity_pct REAL,
    return_on_capital_employed_pct REAL,
    return_on_assets_pct REAL,

    debt_to_equity REAL,
    interest_coverage REAL,
    asset_turnover REAL,

    free_cash_flow REAL,

    earnings_per_share REAL,
    book_value_per_share REAL,
    dividend_payout_ratio_pct REAL,

    total_debt_cr REAL,
    cash_from_operations_cr REAL,

    revenue_cagr_5yr REAL,
    pat_cagr_5yr REAL,
    eps_cagr_5yr REAL,

    composite_quality_score REAL
)
""")

conn.commit()

print("financial_ratios recreated successfully!")

conn.close()