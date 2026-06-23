import sqlite3

conn = sqlite3.connect("data/nifty100.db")

rows = conn.execute(
    "PRAGMA foreign_key_check;"
).fetchall()

print(rows)

conn.close()