from pathlib import Path
import re
import pandas as pd

# ==========================================================
# Regex Pattern
# Supports:
# TTM: 43%
# Last Year: 12%
# 1 Year: 10%
# 3 Years: 18%
# 5 Years: 20%
# 10 Years: 21%
# ==========================================================

PATTERN = re.compile(
    r"(TTM|Last|\d+)\s*(?:Years?)?\s*:?\s*(-?[\d.]+)%",
    re.IGNORECASE,
)

TARGET_COLUMNS = [
    "compounded_sales_growth",
    "compounded_profit_growth",
    "stock_price_cagr",
    "roe",
]


# ==========================================================
# Load Excel
# ==========================================================

def load_analysis():
    file_path = Path("data/raw/analysis.xlsx")

    if not file_path.exists():
        raise FileNotFoundError(file_path)

    # Skip the title row
    return pd.read_excel(file_path, header=1)


# ==========================================================
# Parse Text
# ==========================================================

def parse_text(text):
    if pd.isna(text):
        return None

    text = str(text).strip()

    match = PATTERN.search(text)

    if not match:
        return None

    period = match.group(1).strip()
    value = float(match.group(2))

    if period.lower() == "ttm":
        period = 0
    elif period.lower() == "last":
        period = 1
    else:
        period = int(period)

    return period, value


# ==========================================================
# Main
# ==========================================================

def main():

    df = load_analysis()

    parsed_rows = []
    failures = []

    for _, row in df.iterrows():

        company = row["company_id"]

        for metric in TARGET_COLUMNS:

            result = parse_text(row[metric])

            if result is not None:

                period, value = result

                parsed_rows.append(
                    {
                        "company_id": company,
                        "metric_type": metric,
                        "period_years": period,
                        "value_pct": value,
                    }
                )

            else:

                failures.append(
                    {
                        "company_id": company,
                        "metric_type": metric,
                        "raw_text": row[metric],
                        "reason": "Pattern not matched",
                    }
                )

    parsed_df = pd.DataFrame(parsed_rows)
    failures_df = pd.DataFrame(failures)

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    parsed_df.to_csv(
        output_dir / "analysis_parsed.csv",
        index=False,
    )

    failures_df.to_csv(
        output_dir / "parse_failures.csv",
        index=False,
    )

    print("=" * 60)
    print("Parsing Complete")
    print("=" * 60)
    print(f"Parsed Records : {len(parsed_df)}")
    print(f"Failures       : {len(failures_df)}")

    print("\nFirst 10 Parsed Rows:\n")
    print(parsed_df.head(10))

    if len(failures_df) > 0:
        print("\nParse Failures:\n")
        print(failures_df)


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    main()