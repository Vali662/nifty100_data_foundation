import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

tables = [
    "profitandloss",
    "balancesheet",
    "cashflow"
]

for table in tables:
    print(f"\n===== {table.upper()} =====")

    df = pd.read_sql(f"""
    SELECT
        company_id,
        year,
        COUNT(*) AS total
    FROM {table}
    GROUP BY company_id, year
    HAVING COUNT(*) > 1
    ORDER BY company_id, year;
    """, conn)

    print(df)

conn.close()