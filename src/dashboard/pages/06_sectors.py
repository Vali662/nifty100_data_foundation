import streamlit as st
import pandas as pd

from utils.db import run_query

st.title("🏭 Sector Analysis")

# -------------------------
# Year Selection
# -------------------------

years = run_query("""
SELECT DISTINCT year
FROM financial_ratios
ORDER BY year DESC
""")

selected_year = st.selectbox(
    "Select Financial Year",
    years["year"]
)

# -------------------------
# Join Financial + Sector Data
# -------------------------

df = run_query("""
SELECT
    fr.company_id,
    s.broad_sector,
    s.sub_sector,
    fr.return_on_equity_pct,
    fr.return_on_capital_employed_pct,
    fr.net_profit_margin_pct,
    fr.debt_to_equity,
    fr.composite_quality_score
FROM financial_ratios fr
JOIN sectors s
ON fr.company_id = s.company_id
WHERE fr.year = ?
""", (selected_year,))

# -------------------------
# Sector Dropdown
# -------------------------

sector = st.selectbox(
    "Select Sector",
    sorted(df["broad_sector"].unique())
)

sector_df = df[df["broad_sector"] == sector]

st.success(f"Companies in {sector}: {len(sector_df)}")

# -------------------------
# Sector KPIs
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Companies",
        len(sector_df)
    )

with col2:
    st.metric(
        "Avg ROE",
        f"{sector_df['return_on_equity_pct'].mean():.2f}%"
    )

with col3:
    st.metric(
        "Avg ROCE",
        f"{sector_df['return_on_capital_employed_pct'].mean():.2f}%"
    )

with col4:
    st.metric(
        "Avg Quality Score",
        f"{sector_df['composite_quality_score'].mean():.2f}"
    )

st.dataframe(
    sector_df,
    use_container_width=True,
    hide_index=True
)

import plotly.express as px

st.subheader("ROE Comparison")

fig = px.bar(
    sector_df.sort_values(
        "return_on_equity_pct",
        ascending=False
    ),
    x="company_id",
    y="return_on_equity_pct",
    color="return_on_equity_pct",
    title=f"{sector} - Return on Equity"
)

st.plotly_chart(
    fig,
    use_container_width=True
)