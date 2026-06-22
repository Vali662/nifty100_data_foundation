import pandas as pd

df = pd.read_excel(
    "data/raw/documents.xlsx",
    skiprows=1
)

print("Columns:")
print(df.columns.tolist())

print("\nRows:")
print(len(df))

print("\nFirst 5 Rows:")
print(df.head())