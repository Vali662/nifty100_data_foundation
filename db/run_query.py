import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

with open("sql/queries/market_cap_dashboard.sql", "r") as f:
    query = f.read()

df = pd.read_sql(query, conn)

print(df)

df.to_csv(
    "data/processed/market_cap_dashboard.csv",
    index=False
)

print("\nCSV Created Successfully")

conn.close()