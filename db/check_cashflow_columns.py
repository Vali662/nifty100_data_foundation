import pandas as pd

df = pd.read_excel(
    "data/raw/cashflow.xlsx",
    skiprows=1
)

print("Columns:")
print(df.columns.tolist())

print("\nRows:")
print(len(df))