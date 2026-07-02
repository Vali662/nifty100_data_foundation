import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

df = pd.read_sql("""
SELECT
    company_id,
    year,
    revenue_cagr_5yr,
    pat_cagr_5yr,
    eps_cagr_5yr
FROM financial_ratios
LIMIT 15
""", conn)

print(df)

conn.close()