import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

query = """
SELECT
    company_id,
    year
FROM financial_ratios
"""

df = pd.read_sql_query(query, conn)
conn.close()

latest = (
    df.sort_values("year")
      .groupby("company_id")
      .tail(1)
)

print("Rows:", len(latest))

duplicates = latest[latest.duplicated("company_id", keep=False)]

print("\nDuplicate latest records:")
print(duplicates)