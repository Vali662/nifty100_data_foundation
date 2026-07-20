from pathlib import Path
import sqlite3
import pandas as pd

DB_PATH = "data/nifty100.db"


def load_pros_cons():
    return pd.read_csv("output/pros_cons_generated.csv")


def load_cashflow():
    return pd.read_csv("output/cashflow_intelligence.csv")


def load_financial_ratios():

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

def generate_narrative(
    pros_df,
    cashflow_df,
    ratios_df,
):

    companies = sorted(pros_df["company_id"].unique())

    narratives = []

    for company in companies:

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

        company_ratio = ratios_df[
            ratios_df["company_id"] == company
        ]

        narrative = (
            f"{company} demonstrates a notable financial profile. "
        )

        # ======================================================
        # Pros Section
        # ======================================================

        if len(company_pros) > 0:

            top_pros = company_pros.head(2)["text"].tolist()

            narrative += "Key strengths include "

            for i, pro in enumerate(top_pros):

                if i > 0:
                    narrative += "In addition, "

                narrative += pro.lower()

                if not pro.endswith("."):
                    narrative += ". "

        else:

            narrative += (
                "The available financial metrics indicate a balanced performance. "
            )

        # ======================================================
        # Cash Flow Section
        # ======================================================

        if len(company_cash) > 0:

            top_cash = company_cash.head(2)["message"].tolist()

            narrative += "Cash flow analysis indicates that "

            for i, msg in enumerate(top_cash):

                if i > 0:
                    narrative += "Additionally, "

                narrative += msg.lower()

                if not msg.endswith("."):
                    narrative += ". "

        # ======================================================
        # Financial Metrics
        # ======================================================

        if len(company_ratio) > 0:

            latest = (
                company_ratio
                .sort_values("year", ascending=False)
                .iloc[0]
            )

            roe = latest["return_on_equity_pct"]
            debt = latest["debt_to_equity"]
            cagr = latest["revenue_cagr_5yr"]
            quality = latest["composite_quality_score"]

            if pd.notna(roe):
                narrative += (
                    f"The company reported an ROE of {roe:.1f}%. "
                )

            if pd.notna(debt):
                narrative += (
                    f"Debt-to-equity ratio stands at {debt:.2f}. "
                )

            if pd.notna(cagr):
                narrative += (
                    f"Five-year revenue CAGR is {cagr:.1f}%. "
                )

            if pd.notna(quality):
                narrative += (
                    f"The composite quality score is {quality:.1f}. "
                )

        # ======================================================
        # Cons Section
        # ======================================================

        if len(company_cons) > 0:

            top_con = company_cons.iloc[0]["text"]

            narrative += (
                f"However, investors should note that {top_con.lower()}."
            )

        else:

            narrative += (
                "Overall, the company's financial indicators appear stable."
            )

        narratives.append(
            {
                "company_id": company,
                "narrative": narrative,
            }
        )

    return pd.DataFrame(narratives)

def save_output(df):

    Path("output").mkdir(exist_ok=True)

    output_path = Path("output/company_narratives.csv")

    df.to_csv(
        output_path,
        index=False,
    )

    print("=" * 60)
    print("Narratives Generated")
    print("=" * 60)
    print(df.head())

    print("\nCompanies :", len(df))
    print(f"\nOutput saved to: {output_path}")


def main():

    print("=" * 60)
    print("Loading Data")
    print("=" * 60)

    pros_df = load_pros_cons()
    cashflow_df = load_cashflow()
    ratios_df = load_financial_ratios()

    print(f"Pros/Cons Records      : {len(pros_df)}")
    print(f"Cash Flow Records      : {len(cashflow_df)}")
    print(f"Financial Ratio Records: {len(ratios_df)}")

    narratives = generate_narrative(
        pros_df,
        cashflow_df,
        ratios_df,
    )

    save_output(narratives)


if __name__ == "__main__":
    main()