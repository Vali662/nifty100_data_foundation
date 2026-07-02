import sqlite3

conn = sqlite3.connect("data/nifty100.db")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM financial_ratios")

rows = cursor.fetchone()[0]

print("Rows in financial_ratios:", rows)

conn.close()
