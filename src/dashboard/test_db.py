from utils.db import get_valuation

print("Loading ABB Valuation...\n")

df = get_valuation("ABB")

print(df.head())

print()

print("Rows:", len(df))