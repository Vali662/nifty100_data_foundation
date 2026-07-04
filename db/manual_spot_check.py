import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

df = pd.read_sql("""
SELECT
    company_id,
    year,
    return_on_equity_pct,
    revenue_cagr_5yr
FROM financial_ratios
WHERE company_id IN (
    'ABB',
    'TCS',
    'HDFCBANK'
)
ORDER BY company_id, year
""", conn)

print(df)

conn.close()