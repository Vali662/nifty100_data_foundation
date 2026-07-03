import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

# Read financial ratios
ratios = pd.read_sql("""
SELECT
    company_id,
    year,
    return_on_equity_pct,
    return_on_capital_employed_pct
FROM financial_ratios
""", conn)

companies = pd.read_sql("""
SELECT
    id AS company_id,
    company_name,
    roce_percentage,
    roe_percentage
FROM companies
""", conn)

# Merge
merged = pd.merge(
    ratios,
    companies,
    on="company_id",
    how="left"
)

# ROCE Difference
merged["roce_difference"] = (
    merged["return_on_capital_employed_pct"]
    - merged["roce_percentage"]
).abs()

# ROE Difference
merged["roe_difference"] = (
    merged["return_on_equity_pct"]
    - merged["roe_percentage"]
).abs()

print("Merged Rows:", len(merged))

print("\nSample:")
print(
    merged[
        [
            "company_id",
            "year",
            "return_on_equity_pct",
            "roe_percentage",
            "return_on_capital_employed_pct",
            "roce_percentage",
        ]
    ].head(10)
)

# Log anomalies
with open("output/ratio_edge_cases.log", "w") as f:

    f.write("=== ROCE / ROE EDGE CASE REPORT ===\n\n")

    for _, row in merged.iterrows():

        if pd.notna(row["roce_difference"]) and row["roce_difference"] > 5:

            if row["roce_difference"] > 20:
                category = "Data Source Issue"
            elif row["roce_difference"] > 10:
                category = "Version Difference"
            else:
                category = "Formula Discrepancy"

            f.write(
                f"{row['company_id']} | "
                f"{row['year']} | "
                f"ROCE Difference = {row['roce_difference']:.2f}% | "
                f"Category: {category}\n"
            )

        if pd.notna(row["roe_difference"]) and row["roe_difference"] > 5:

            if row["roe_difference"] > 20:
                category = "Data Source Issue"
            elif row["roe_difference"] > 10:
                category = "Version Difference"
            else:
                category = "Formula Discrepancy"

            f.write(
                f"{row['company_id']} | "
                f"{row['year']} | "
                f"ROE Difference = {row['roe_difference']:.2f}% | "
                f"Category: {category}\n"
            )

print("ratio_edge_cases.log created successfully!")
conn.close()