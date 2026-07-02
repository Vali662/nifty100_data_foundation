import sqlite3

conn = sqlite3.connect("data/nifty100.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS financial_ratios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    year INTEGER,

    net_profit_margin_pct REAL,
    operating_profit_margin_pct REAL,
    return_on_equity_pct REAL,
    return_on_capital_employed_pct REAL,
    return_on_assets_pct REAL,

    debt_to_equity REAL,
    interest_coverage REAL,
    asset_turnover REAL,

    free_cash_flow REAL,
    capex_intensity_pct REAL,
    fcf_conversion_rate_pct REAL,

    revenue_cagr_5yr REAL,
    pat_cagr_5yr REAL,
    eps_cagr_5yr REAL,

    composite_quality_score REAL,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
);
""")

conn.commit()

print("financial_ratios table created successfully!")

conn.close()