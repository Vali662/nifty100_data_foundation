import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

df = pd.read_sql(
    """
    SELECT
        company_id,
        broad_sector
    FROM sectors
    WHERE broad_sector = 'Financials'
    ORDER BY company_id
    """,
    conn,
)

print(df)

print("\nTotal Financial Companies:")
print(len(df))

conn.close()