import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")

query = """
SELECT
    fr.company_id,
    fr.year,
    fr.return_on_equity_pct,
    fr.return_on_capital_employed_pct,
    fr.net_profit_margin_pct,
    fr.debt_to_equity,
    fr.free_cash_flow,
    fr.pat_cagr_5yr,
    fr.revenue_cagr_5yr,
    fr.eps_cagr_5yr,
    fr.interest_coverage,
    fr.asset_turnover,
    pg.peer_group_name

FROM financial_ratios fr

LEFT JOIN peer_groups pg
ON fr.company_id = pg.company_id
"""

df = pd.read_sql(query, conn)

df = (
    df.sort_values("year")
      .groupby("company_id")
      .tail(1)
)

print(df.head())

print()

print(df["peer_group_name"].value_counts())

def calculate_percentile(group, metric, inverse=False):

    temp = group.copy()

    if inverse:
        temp["percentile_rank"] = (
            1 - temp[metric].rank(pct=True)
        ) * 100
    else:
        temp["percentile_rank"] = (
            temp[metric].rank(pct=True)
        ) * 100

    return temp

metrics = [

    "return_on_equity_pct",

    "return_on_capital_employed_pct",

    "net_profit_margin_pct",

    "debt_to_equity",

    "free_cash_flow",

    "pat_cagr_5yr",

    "revenue_cagr_5yr",

    "eps_cagr_5yr",

    "interest_coverage",

    "asset_turnover"

]
results = []

for metric in metrics:

    for peer_name, group in df.groupby("peer_group_name"):

        inverse = metric == "debt_to_equity"

        ranked = calculate_percentile(
            group,
            metric,
            inverse
        )

        ranked["metric"] = metric

        ranked["value"] = ranked[metric]

        results.append(
            ranked[
                [
                    "company_id",
                    "peer_group_name",
                    "metric",
                    "value",
                    "percentile_rank",
                    "year"
                ]
            ]
        )
        peer_percentiles = pd.concat(
    results,
    ignore_index=True
)
print(peer_percentiles.head(20))

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS peer_percentiles (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_id TEXT,

    peer_group_name TEXT,

    metric TEXT,

    value REAL,

    percentile_rank REAL,

    year TEXT

)
""")

conn.commit()

cursor.execute("DELETE FROM peer_percentiles")

conn.commit()

peer_percentiles.to_sql(

    "peer_percentiles",

    conn,

    if_exists="append",

    index=False

)
rows = pd.read_sql(

    "SELECT COUNT(*) AS total FROM peer_percentiles",

    conn

)

print(rows)

check = pd.read_sql("""

SELECT *

FROM peer_percentiles

WHERE peer_group_name='IT Services'

AND metric='return_on_equity_pct'

ORDER BY percentile_rank DESC

""", conn)

print(check)