import pandas as pd

file_path = "data/raw/stock_prices.xlsx"


xls = pd.ExcelFile(file_path)

print("Sheets:")
print(xls.sheet_names)

df = pd.read_excel(file_path)

print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())
print(df.columns.tolist())
print(df.head(10))