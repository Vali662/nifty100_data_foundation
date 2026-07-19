from pathlib import Path
import sqlite3
import pandas as pd

DB_PATH = "data/nifty100.db"

pros = []
cons = []


def load_financial_ratios():
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql(
        """
        SELECT *
        FROM financial_ratios
        """,
        conn,
    )

    conn.close()

    df = (
        df.sort_values("year")
          .groupby("company_id")
          .tail(1)
          .reset_index(drop=True)
    )

    return df

def add_pro(company, rule_id, text, confidence):
    if confidence > 60:
        pros.append({
            "company_id": company,
            "type": "pro",
            "rule_id": rule_id,
            "text": text,
            "confidence_pct": confidence,
        })


def add_con(company, rule_id, text, confidence):
    if confidence > 60:
        #print(f"CON -> {company} | {rule_id}")

        cons.append({
            "company_id": company,
            "type": "con",
            "rule_id": rule_id,
            "text": text,
            "confidence_pct": confidence,
        })


def apply_rules(df):

    for _, row in df.iterrows():

        company = row["company_id"]

        # =====================================================
        # PRO RULE 1
        # =====================================================
        if row["return_on_equity_pct"] > 20:
            add_pro(
                company,
                "PRO_01",
                "Consistently high return on equity above 20% demonstrates exceptional capital efficiency.",
                95,
            )

        # =====================================================
        # PRO RULE 2
        # =====================================================
        if pd.notna(row["free_cash_flow"]) and row["free_cash_flow"] > 0:
            add_pro(
                company,
                "PRO_02",
                "Strong free cash flow generation signals healthy business fundamentals.",
                90,
            )

        # =====================================================
        # PRO RULE 3
        # =====================================================
        if pd.notna(row["debt_to_equity"]) and row["debt_to_equity"] <= 0.05:
            add_pro(
                company,
                "PRO_03",
                "Debt-free balance sheet provides financial flexibility and eliminates interest burden.",
                95,
            )

        # =====================================================
        # PRO RULE 4
        # =====================================================
        if pd.notna(row["revenue_cagr_5yr"]) and row["revenue_cagr_5yr"] > 15:
            add_pro(
                company,
                "PRO_04",
                "Revenue growing at above 15% CAGR over 5 years reflects strong business momentum.",
                90,
            )

        # =====================================================
        # PRO RULE 5
        # =====================================================
        if (
            pd.notna(row["operating_profit_margin_pct"])
            and row["operating_profit_margin_pct"] > 25
        ):
            add_pro(
                company,
                "PRO_05",
                "Operating profit margin above 25% indicates strong pricing power and cost discipline.",
                90,
            )

        # =====================================================
        # PRO RULE 6
        # =====================================================
        if pd.notna(row["pat_cagr_5yr"]) and row["pat_cagr_5yr"] > 20:
            add_pro(
                company,
                "PRO_06",
                "Net profit compounding above 20% over 5 years creates significant shareholder value.",
                95,
            )

        # =====================================================
        # PRO RULE 7
        # =====================================================
        if (
            (pd.notna(row["interest_coverage"]) and row["interest_coverage"] > 10)
            or (pd.notna(row["debt_to_equity"]) and row["debt_to_equity"] <= 0.05)
        ):
            add_pro(
                company,
                "PRO_07",
                "Very high interest coverage reflects negligible financial stress from debt servicing.",
                90,
            )

        # =====================================================
        # PRO RULE 8
        # =====================================================
        
        if (
                "dividend_yield_pct" in row.index
                and pd.notna(row["dividend_yield_pct"])
                and row["dividend_payout_ratio_pct"] > 2
                and pd.notna(row["free_cash_flow"])
                and row["free_cash_flow"] > 0
        ):
            add_pro(
                company,
                "PRO_08",
                "Consistent dividend yield above 2% backed by positive free cash flow.",
                85,
            
            )
        # =====================================================
        # PRO RULE 9
        # =====================================================
        if pd.notna(row["eps_cagr_5yr"]) and row["eps_cagr_5yr"] > 15:
            add_pro(
                company,
                "PRO_09",
                "Earnings per share growing above 15% CAGR indicates strong earnings quality and compounding.",
                90,
            )

        # =====================================================
        # PRO RULE 10
        # =====================================================
        if (
            pd.notna(row["composite_quality_score"])
            and row["composite_quality_score"] > 20
        ):
            add_pro(
                company,
                "PRO_10",
                "Business quality metrics have strengthened consistently over recent years.",
                80,
            )

        # =====================================================
        # PRO RULE 11
        # =====================================================
        if (
            pd.notna(row["revenue_cagr_5yr"])
            and pd.notna(row["pat_cagr_5yr"])
            and row["pat_cagr_5yr"] > row["revenue_cagr_5yr"]
        ):
            add_pro(
                company,
                "PRO_11",
                "Profit growth outpacing revenue reflects improving operating leverage and scale benefits.",
                85,
            )

        # =====================================================
        # PRO RULE 12
        # =====================================================
        if (
            pd.notna(row["asset_turnover"])
            and row["asset_turnover"] > 1
        ):
            add_pro(
                company,
                "PRO_12",
                "Efficient utilization of assets supports sustainable business growth.",
                80,
            )

        # =====================================================
        # CON RULE 1
        # =====================================================
        if (
            pd.notna(row["debt_to_equity"])
            and row["debt_to_equity"] > 2
        ):
            add_con(
                company,
                "CON_01",
                f"Debt-to-equity ratio of {row['debt_to_equity']:.2f} is elevated and warrants monitoring.",
                95,
            )

        # =====================================================
        # CON RULE 2
        # =====================================================
        if (
            pd.notna(row["free_cash_flow"])
            and row["free_cash_flow"] < 0
        ):
            add_con(
                company,
                "CON_02",
                "Negative free cash flow raises concern about cash generation quality.",
                90,
            )

        # =====================================================
        # CON RULE 3
        # =====================================================
        if (
            pd.notna(row["operating_profit_margin_pct"])
            and row["operating_profit_margin_pct"] < 10
        ):
            add_con(
                company,
                "CON_03",
                "Operating profit margin is low, indicating pricing pressure or weak operating efficiency.",
                80,
            )

        # =====================================================
        # CON RULE 4
        # =====================================================
        if (
            pd.notna(row["net_profit_margin_pct"])
            and row["net_profit_margin_pct"] < 0
        ):
            add_con(
                company,
                "CON_04",
                "Company reported a negative net profit margin in the latest financial year.",
                95,
            )

        # =====================================================
        # CON RULE 5
        # =====================================================
        if (
            pd.notna(row["revenue_cagr_5yr"])
            and row["revenue_cagr_5yr"] < 5
        ):
            add_con(
                company,
                "CON_05",
                "Revenue growth below 5% over five years suggests weak business momentum.",
                85,
            )

        # =====================================================
        # CON RULE 6
        # =====================================================
        if (
            pd.notna(row["interest_coverage"])
            and row["interest_coverage"] < 1.5
        ):
            add_con(
                company,
                "CON_06",
                "Low interest coverage indicates elevated debt servicing risk.",
                95,
            )
        # =====================================================
        # CON RULE 7
        # ROE < 10%
        # =====================================================
        if (
            pd.notna(row["return_on_equity_pct"])
            and row["return_on_equity_pct"] < 10
        ):
            add_con(
                company,
                "CON_07",
                "Return on equity below 10% indicates weak shareholder returns.",
                85,
            )


        # =====================================================
        # CON RULE 8
        # PAT CAGR < 5%
        # =====================================================
        if (
            pd.notna(row["pat_cagr_5yr"])
            and row["pat_cagr_5yr"] < 5
        ):
            add_con(
                company,
                "CON_08",
                "Profit growth has remained below 5% CAGR over the past five years.",
                85,
            )


        # =====================================================
        # CON RULE 9
        # EPS CAGR < 5%
        # =====================================================
        if (
            pd.notna(row["eps_cagr_5yr"])
            and row["eps_cagr_5yr"] < 5
        ):
            add_con(
                company,
                "CON_09",
                "Weak earnings-per-share growth limits long-term shareholder value creation.",
                80,
            )


        # =====================================================
        # CON RULE 10
        # Asset Turnover < 0.5
        # =====================================================
        if (
            pd.notna(row["asset_turnover"])
            and row["asset_turnover"] < 0.5
        ):
            add_con(
                company,
                "CON_10",
                "Low asset turnover indicates inefficient utilization of company assets.",
                80,
            )


        # =====================================================
        # CON RULE 11
        # =====================================================
        if (
            pd.notna(row["cash_from_operations_cr"])
            and pd.notna(row["free_cash_flow"])
            and row["free_cash_flow"] < row["cash_from_operations_cr"] * 0.5
        ):
            add_con(
                company,
                "CON_11",
                "Free cash flow is significantly lower than operating cash flow, indicating heavy capital expenditure.",
                85,
            )


        # =====================================================
        # CON RULE 12
        # Book Value Per Share < EPS
        # =====================================================
        if (
            pd.notna(row["book_value_per_share"])
            and pd.notna(row["earnings_per_share"])
            and row["book_value_per_share"] < row["earnings_per_share"]
        ):
            add_con(
                company,
                "CON_12",
                "Book value per share is relatively low compared with earnings per share.",
                75,
            )

def save_output():

    output = (
    pd.DataFrame(pros + cons)
    .sort_values(["company_id", "type", "rule_id"])
    .reset_index(drop=True)
)

    Path("output").mkdir(exist_ok=True)

    output.to_csv(
        "output/pros_cons_generated.csv",
        index=False,
    )

    print("=" * 60)
    print("Generation Complete")
    print("=" * 60)
    print(output.head())
    print(f"\nTotal Statements : {len(output)}")


def main():

    df = load_financial_ratios()

    apply_rules(df)

    save_output()


if __name__ == "__main__":
    main()