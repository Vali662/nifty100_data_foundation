import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

query = """
SELECT
    company_id,
    year,
    COUNT(*) AS total
FROM financial_ratios
GROUP BY company_id, year
HAVING COUNT(*) > 1
ORDER BY company_id, year;
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()