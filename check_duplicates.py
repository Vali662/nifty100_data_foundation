import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

query = """
SELECT
    company_id,
    year,
    COUNT(*) AS total_rows
FROM financial_ratios
GROUP BY company_id, year
HAVING COUNT(*) > 1
ORDER BY company_id, year;
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()

import sqlite3

conn = sqlite3.connect("data/nifty100.db")

count = conn.execute(
    "SELECT COUNT(*) FROM financial_ratios"
).fetchone()[0]

print(count)

conn.close()