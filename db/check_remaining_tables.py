import sqlite3

conn = sqlite3.connect("data/nifty100.db")
cursor = conn.cursor()

tables = [
    "stock_prices",
    "market_cap",
    "sectors",
    "peer_groups"
]

for table in tables:
    print(f"\n=== {table} ===")

    cursor.execute(
        f"PRAGMA table_info({table})"
    )

    for row in cursor.fetchall():
        print(row)

conn.close()