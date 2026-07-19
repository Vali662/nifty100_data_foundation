from pathlib import Path
import sqlite3
import pandas as pd

DB_PATH = "data/nifty100.db"
cashflow_insights = []
cashflow_scores = []

def add_score(company, score):

    cashflow_scores.append({
        "company_id": company,
        "cashflow_health_score": score
    })

def add_insight(company, insight_type, message, confidence):

    cashflow_insights.append({
        "company_id": company,
        "type": insight_type,
        "message": message,
        "confidence_pct": confidence,
    })

def load_cashflow():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql(
        """
        SELECT *
        FROM cashflow
        """,
        conn,
    )

    conn.close()

    return df

def latest_cashflow(df):

    df = (
        df.sort_values("year")
          .groupby("company_id")
          .tail(1)
          .reset_index(drop=True)
    )

    return df

def analyze_cashflow(df):

    for _, row in df.iterrows():

        company = row["company_id"]

        ocf = row["operating_activity"]
        icf = row["investing_activity"]
        fcf = row["financing_activity"]
        net = row["net_cash_flow"]

        # -----------------------------------------
        # Cash Flow Health Score
        # -----------------------------------------

        score = 50

        if pd.notna(ocf) and ocf > 0:
            score += 20

        if pd.notna(icf) and icf < 0:
            score += 10

        if pd.notna(net) and net > 0:
            score += 10

        if pd.notna(fcf) and fcf < 0:
            score += 10

        score = min(score, 100)

        add_score(company, score)

        # -----------------------------------------
        # Rule 1 - Positive Operating Cash Flow
        # -----------------------------------------
        if pd.notna(ocf) and ocf > 0:
            add_insight(
                company,
                "Positive OCF",
                "Business generates positive operating cash flow from core operations.",
                95,
            )

        # -----------------------------------------
        # Rule 2 - Negative Operating Cash Flow
        # -----------------------------------------
        if pd.notna(ocf) and ocf < 0:
            add_insight(
                company,
                "Negative OCF",
                "Negative operating cash flow may indicate pressure on core business operations.",
                95,
            )

        # -----------------------------------------
        # Rule 3 - Heavy Capital Investment
        # -----------------------------------------
        if pd.notna(icf) and icf < 0:
            add_insight(
                company,
                "Capital Investment",
                "Company is investing cash into long-term assets or business expansion.",
                90,
            )

        # -----------------------------------------
        # Rule 4 - Financing Dependency
        # -----------------------------------------
        if pd.notna(fcf) and fcf > 0:
            add_insight(
                company,
                "Financing Inflow",
                "Company received positive cash from financing activities.",
                85,
            )

        # -----------------------------------------
        # Rule 5 - Positive Net Cash Flow
        # -----------------------------------------
        if pd.notna(net) and net > 0:
            add_insight(
                company,
                "Positive Net Cash",
                "Overall cash position improved during the year.",
                90,
            )

        # -----------------------------------------
        # Rule 6 - Strong Operating Cash Flow
        # -----------------------------------------
        if pd.notna(ocf) and ocf > 1000:
            add_insight(
                company,
                "Strong OCF",
                "Operating cash flow is strong, indicating excellent cash generation capability.",
                95,
            )

        # -----------------------------------------
        # Rule 7 - Heavy Investment Phase
        # -----------------------------------------
        if (
            pd.notna(icf)
            and icf < -1000
        ):
            add_insight(
                company,
                "Expansion Phase",
                "Large investing cash outflow suggests expansion or significant capital expenditure.",
                90,
            )

        # -----------------------------------------
        # Rule 8 - Debt/Funding Raised
        # -----------------------------------------
        if (
            pd.notna(fcf)
            and fcf > 1000
        ):
            add_insight(
                company,
                "External Funding",
                "Large financing inflow indicates debt or equity funding.",
                85,
            )

        # -----------------------------------------
        # Rule 9 - Cash Burn
        # -----------------------------------------
        if (
            pd.notna(net)
            and net < 0
        ):
            add_insight(
                company,
                "Cash Burn",
                "Net cash flow is negative, indicating a reduction in cash reserves.",
                90,
            )

        # -----------------------------------------
        # Rule 10 - Healthy Cash Flow Pattern
        # -----------------------------------------
        if (
            pd.notna(ocf)
            and pd.notna(icf)
            and ocf > 0
            and icf < 0
        ):
            add_insight(
                company,
                "Healthy Cash Flow",
                "Positive operating cash flow combined with investment in assets reflects a healthy business pattern.",
                95,
            )

def save_output():

    output = pd.DataFrame(cashflow_insights)

    Path("output").mkdir(exist_ok=True)

    output.to_csv(
        "output/cashflow_intelligence.csv",
        index=False,
    )

    # -----------------------------
    # Save Cash Flow Health Scores
    # -----------------------------
    score_df = pd.DataFrame(cashflow_scores)

    score_df.to_csv(
        "output/cashflow_health_score.csv",
        index=False,
    )

    print("=" * 60)
    print("Cash Flow Intelligence Generated")
    print("=" * 60)
    print(output.head())

    print(f"\nTotal Insights : {len(output)}")
    print(f"Cash Flow Scores Generated : {len(score_df)}")


def main():

    df = load_cashflow()
    df = latest_cashflow(df)

    print("=" * 60)
    print("Latest Cash Flow")
    print("=" * 60)

    analyze_cashflow(df)
    save_output()

if __name__ == "__main__":
    main()