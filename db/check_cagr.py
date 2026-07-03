import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

df = pd.read_sql(
    """
    SELECT
        company_id,
        year,
        revenue_cagr_5yr,
        pat_cagr_5yr,
        eps_cagr_5yr
    FROM financial_ratios
    WHERE revenue_cagr_5yr IS NOT NULL
    ORDER BY company_id, year
    LIMIT 20
    """,
    conn,
)

print(df)

print("\nTotal Rows with CAGR:")
count = pd.read_sql(
    """
    SELECT COUNT(*) AS total
    FROM financial_ratios
    WHERE revenue_cagr_5yr IS NOT NULL
    """,
    conn,
)

print(count)

conn.close()