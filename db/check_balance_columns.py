import pandas as pd

df = pd.read_excel(
    "data/raw/balancesheet.xlsx",
    skiprows=1
)

print("Columns:")
print(df.columns.tolist())

print("\nRows:")
print(len(df))