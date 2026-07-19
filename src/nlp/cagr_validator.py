from pathlib import Path
import sqlite3
import pandas as pd

DB_PATH = "data/nifty100.db"
PARSED_FILE = "output/analysis_parsed.csv"
OUTPUT_FILE = "output/cagr_divergence_review.csv"

# Mapping between parsed metric names and database columns
METRIC_MAP = {
    "compounded_sales_growth": "revenue_cagr_5yr",
    "compounded_profit_growth": "pat_cagr_5yr",
}


def main():
    parsed = pd.read_csv(PARSED_FILE)

    # Only validate the 5-year CAGR values
    parsed = parsed[parsed["period_years"] == 5]
    parsed = parsed[parsed["metric_type"].isin(METRIC_MAP.keys())]

    conn = sqlite3.connect(DB_PATH)

    ratios = pd.read_sql(
        """
        SELECT
            company_id,
            year,
            revenue_cagr_5yr,
            pat_cagr_5yr
        FROM financial_ratios
        """,
        conn,
    )

    conn.close()

    # Keep only the latest year for each company
    ratios = (
        ratios.sort_values("year")
        .groupby("company_id")
        .tail(1)
    )

    review_rows = []

    for _, row in parsed.iterrows():

        company = row["company_id"]
        metric = row["metric_type"]
        parsed_value = row["value_pct"]

        db_row = ratios[ratios["company_id"] == company]

        if db_row.empty:
            continue

        db_column = METRIC_MAP[metric]
        db_value = db_row.iloc[0][db_column]

        if pd.isna(db_value):
            continue

        difference = abs(parsed_value - db_value)

        if difference > 5:
            review_rows.append({
                "company_id": company,
                "metric_type": metric,
                "parsed_value": parsed_value,
                "ratio_engine_value": db_value,
                "difference_pct": round(difference, 2),
                "status": "Manual Review",
            })

    review_df = pd.DataFrame(review_rows)

    Path("output").mkdir(exist_ok=True)

    review_df.to_csv(
        OUTPUT_FILE,
        index=False,
    )

    print("=" * 60)
    print("CAGR Validation Complete")
    print("=" * 60)
    print(f"Companies flagged: {len(review_df)}")

    if not review_df.empty:
        print(review_df.head())


if __name__ == "__main__":
    main()