import sqlite3

conn = sqlite3.connect("data/nifty100.db")
cursor = conn.cursor()

cursor.execute("""
DELETE FROM financial_ratios
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM financial_ratios
    GROUP BY
        company_id,
        year
);
""")

conn.commit()

count = cursor.execute(
    "SELECT COUNT(*) FROM financial_ratios"
).fetchone()[0]

print("Rows after cleanup:", count)

conn.close()