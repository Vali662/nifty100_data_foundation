import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

conn = sqlite3.connect("data/nifty100.db")

query = """
SELECT

fr.company_id,

fr.return_on_equity_pct,

fr.return_on_capital_employed_pct,

fr.net_profit_margin_pct,

fr.debt_to_equity,

fr.free_cash_flow,

fr.pat_cagr_5yr,

fr.revenue_cagr_5yr,

fr.composite_quality_score,

pg.peer_group_name

FROM financial_ratios fr

LEFT JOIN peer_groups pg

ON fr.company_id = pg.company_id

"""

df = pd.read_sql(query, conn)

df = (
    df.sort_values("company_id")
      .groupby("company_id")
      .tail(1)
)
print(df.head())

print()

print(df["peer_group_name"].value_counts())

metrics = [
    "return_on_equity_pct",
    "return_on_capital_employed_pct",
    "net_profit_margin_pct",
    "debt_to_equity",
    "free_cash_flow",
    "pat_cagr_5yr",
    "revenue_cagr_5yr",
    "composite_quality_score"
]
for _, company_data in df.iterrows():

    if pd.isna(company_data["peer_group_name"]):
        continue

    company = company_data["company_id"]

    peer = company_data["peer_group_name"]

    peer_data = df[df["peer_group_name"] == peer]

    company_values = company_data[metrics].fillna(0).values

    peer_values = (
        peer_data[metrics]
        .mean()
        .fillna(0)
        .values
    )

    labels = metrics

    angles = np.linspace(
        0,
        2*np.pi,
        len(labels),
        endpoint=False
    )

    company_values = np.concatenate(
        (company_values,[company_values[0]])
    )

    peer_values = np.concatenate(
        (peer_values,[peer_values[0]])
    )

    angles = np.concatenate(
        (angles,[angles[0]])
    )

    plt.figure(figsize=(8,8))

    ax = plt.subplot(111, polar=True)

    ax.plot(
        angles,
        company_values,
        linewidth=2,
        label=company
    )

    ax.fill(
        angles,
        company_values,
        alpha=0.25
    )

    ax.plot(
        angles,
        peer_values,
        linestyle="--",
        linewidth=2,
        label="Peer Average"
    )

    ax.set_xticks(angles[:-1])

    ax.set_xticklabels(labels)

    plt.legend()

    plt.title(company)

    os.makedirs(
        "reports/radar_charts",
        exist_ok=True
    )

    plt.savefig(
        f"reports/radar_charts/{company}_radar.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"{company} radar chart created.")

print("\nAll radar charts generated successfully!")