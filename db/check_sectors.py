import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

df = pd.read_sql(
    "SELECT * FROM sectors LIMIT 10",
    conn
)

print("Columns:")
print(df.columns.tolist())

print("\nData:")
print(df)

conn.close()