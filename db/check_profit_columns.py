import pandas as pd

df = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    skiprows=1
)

print(df.columns.tolist())

print("\nRows:")
print(len(df))