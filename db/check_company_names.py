import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

companies = pd.read_sql("""
SELECT
    id,
    company_name
FROM companies
LIMIT 20
""", conn)

print(companies)

conn.close()