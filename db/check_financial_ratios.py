import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

query = """
SELECT
    company_id,
    year,
    revenue_cagr_5yr,
    pat_cagr_5yr
FROM financial_ratios
LIMIT 10;
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()