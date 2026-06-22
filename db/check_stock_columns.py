import pandas as pd

df = pd.read_excel(
    "data/raw/stock_prices.xlsx"
)

print("Columns:")
print(df.columns.tolist())

print("\nRows:")
print(len(df))

print("\nFirst 5 Rows:")
print(df.head())