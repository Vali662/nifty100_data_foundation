import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.etl.normaliser import (
    normalize_year,
    normalize_ticker
)

print(normalize_year("2024"))
print(normalize_year(2024.0))

print(normalize_ticker(" tcs "))
print(normalize_ticker("infy"))