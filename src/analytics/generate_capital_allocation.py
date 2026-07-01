import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import pandas as pd

from src.analytics.cashflow_kpis import capital_allocation_pattern

# Sample data (replace later with SQLite data)
data = [
    ["ABB", 2023, 500, -200, -100],
    ["TCS", 2023, 500, 100, -50],
    ["SBIN", 2023, -100, 200, 300],
    ["INFY", 2023, -100, -200, 300],
    ["ITC", 2023, 100, 200, 300],
]

df = pd.DataFrame(
    data,
    columns=[
        "company_id",
        "year",
        "operating_activity",
        "investing_activity",
        "financing_activity",
    ],
)

df["cfo_sign"] = df["operating_activity"].apply(
    lambda x: "+" if x >= 0 else "-"
)

df["cfi_sign"] = df["investing_activity"].apply(
    lambda x: "+" if x >= 0 else "-"
)

df["cff_sign"] = df["financing_activity"].apply(
    lambda x: "+" if x >= 0 else "-"
)

df["pattern_label"] = df.apply(
    lambda row: capital_allocation_pattern(
        row["operating_activity"],
        row["investing_activity"],
        row["financing_activity"],
    ),
    axis=1,
)

df.to_csv(
    "output/capital_allocation.csv",
    index=False,
)

print("capital_allocation.csv generated successfully!")
print(df)