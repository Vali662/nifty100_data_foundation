from pathlib import Path
import pandas as pd

possible_paths = [
    Path("data/raw/analysis.xlsx"),
    Path("data/analysis.xlsx"),
]

file_path = None

for path in possible_paths:
    if path.exists():
        file_path = path
        break

if file_path is None:
    raise FileNotFoundError("analysis.xlsx not found.")

df = pd.read_excel(file_path)

print("=" * 80)
print("FILE:", file_path)
print("=" * 80)

print("\nColumns:\n")
print(df.columns.tolist())

print("\nFirst 5 rows:\n")
print(df.head())