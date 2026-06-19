import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.etl.loader import load_excel

df = load_excel(
    "data/raw/profitandloss.xlsx"
)

print(df.shape)
print(df.head())