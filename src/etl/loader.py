import sqlite3

conn = sqlite3.connect("data/nifty100.db")

with open("sql/schema.sql", "r") as f:
    schema = f.read()

conn.executescript(schema)

print("Tables Created")

conn.close()