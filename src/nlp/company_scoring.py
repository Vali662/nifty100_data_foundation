from pathlib import Path
import sqlite3
import pandas as pd

DB_PATH = "data/nifty100.db"

def load_ratios():

    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT
        company_id,
        year,
        return_on_equity_pct,
        debt_to_equity,
        revenue_cagr_5yr,
        composite_quality_score
    FROM financial_ratios
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

def load_pros_cons():

    return pd.read_csv(
        "output/pros_cons_generated.csv"
    )

def load_cashflow():

    return pd.read_csv(
        "output/cashflow_intelligence.csv"
    )

def calculate_scores(
    ratios_df,
    pros_df,
    cashflow_df,
):

    companies = sorted(
        ratios_df["company_id"].unique()
    )

    scores = []

    for company in companies:

        company_ratio = ratios_df[
            ratios_df["company_id"] == company
        ].sort_values(
            "year",
            ascending=False
        )

        company_pros = pros_df[
            (pros_df["company_id"] == company)
            & (pros_df["type"] == "pro")
        ]

        company_cons = pros_df[
            (pros_df["company_id"] == company)
            & (pros_df["type"] == "con")
        ]

        company_cash = cashflow_df[
            cashflow_df["company_id"] == company
        ]

        score = 50

        if len(company_ratio) > 0:

            latest = company_ratio.iloc[0]

            roe = latest["return_on_equity_pct"]
            debt = latest["debt_to_equity"]
            cagr = latest["revenue_cagr_5yr"]
            quality = latest["composite_quality_score"]

            if pd.notna(roe):

                if roe >= 20:
                    score += 15
                elif roe >= 15:
                    score += 10
                elif roe >= 10:
                    score += 5

            if pd.notna(debt):

                if debt <= 0.5:
                    score += 10
                elif debt <= 1:
                    score += 5

            if pd.notna(cagr):

                if cagr >= 15:
                    score += 10
                elif cagr >= 10:
                    score += 5

            if pd.notna(quality):

                score += min(quality / 10, 10)

        score += min(len(company_pros), 10)

        score -= min(len(company_cons), 10)

        score += min(len(company_cash), 10)

        score = max(0, min(100, round(score)))

        if score >= 85:
            rating = "Excellent"
            recommendation = "Strong Buy"

        elif score >= 70:
            rating = "Very Good"
            recommendation = "Buy"

        elif score >= 55:
            rating = "Good"
            recommendation = "Hold"

        elif score >= 40:
            rating = "Average"
            recommendation = "Watch"

        else:
            rating = "Weak"
            recommendation = "Avoid"

        scores.append(
            {
                "company_id": company,
                "investment_score": score,
                "rating": rating,
                "recommendation": recommendation,
            }
        )

    return pd.DataFrame(scores)

    companies = sorted(
        ratios_df["company_id"].unique()
    )

    scores = []

    for company in companies:

        scores.append({
            "company_id": company,
            "investment_score": 0,
            "rating": ""
        })

    return pd.DataFrame(scores)

def save_output(df):

    Path("output").mkdir(exist_ok=True)

    df = df.sort_values(
        by="investment_score",
        ascending=False
    ).reset_index(drop=True)

    df.insert(0, "rank", range(1, len(df) + 1))

    df.to_csv(
        "output/company_scores.csv",
        index=False,
    )

    print("=" * 60)
    print("Company Scores Generated")
    print("=" * 60)

    print(df.head(10)[
    [
        "rank",
        "company_id",
        "investment_score",
        "rating",
        "recommendation",
    ]
])

    print("\nCompanies :", len(df))

def main():

    ratios_df = load_ratios()
    pros_df = load_pros_cons()
    cashflow_df = load_cashflow()

    scores = calculate_scores(
        ratios_df,
        pros_df,
        cashflow_df,
    )

    save_output(scores)


if __name__ == "__main__":
    main()