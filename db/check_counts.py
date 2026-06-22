import sqlite3

conn = sqlite3.connect("data/nifty100.db")

cursor = conn.cursor()

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "documents",
    "stock_prices",
    "market_cap",
    "sectors",
    "peer_groups"
]

for table in tables:
    cursor.execute(
        f"SELECT COUNT(*) FROM {table}"
    )

    print(
        table,
        cursor.fetchone()[0]
    )

conn.close()