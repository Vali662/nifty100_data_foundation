import sqlite3

conn = sqlite3.connect("data/nifty100.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM financial_ratios")

conn.commit()

print("financial_ratios table cleared successfully!")

conn.close()