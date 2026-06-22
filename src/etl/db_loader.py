import pandas as pd
import sqlite3

conn = sqlite3.connect("data/nifty100.db")

profit = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    skiprows=1
)

profit.to_sql(
    "profitandloss",
    conn,
    if_exists="append",
    index=False
)

print("Profit Records Loaded:", len(profit))

conn.close()