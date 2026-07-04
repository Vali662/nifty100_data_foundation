import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

df = pd.read_sql("""
SELECT DISTINCT
company_id
FROM financial_ratios
WHERE
return_on_equity_pct > 15
AND debt_to_equity < 1
ORDER BY company_id;
""", conn)

print(df)

print("\nTotal Companies Found:")
print(len(df))

conn.close()