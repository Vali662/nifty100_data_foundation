import sqlite3

conn = sqlite3.connect("data/nifty100.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM profitandloss"
)

print(cursor.fetchone()[0])

conn.close()