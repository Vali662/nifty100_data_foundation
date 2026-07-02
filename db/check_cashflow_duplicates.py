import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

cf = pd.read_sql("SELECT * FROM cashflow", conn)

duplicates = cf.groupby(
    ["company_id", "year"]
).size()

duplicates = duplicates[duplicates > 1]

print(duplicates)

conn.close()