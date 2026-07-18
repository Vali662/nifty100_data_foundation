import streamlit as st
from utils.db import run_query

st.title("💰 Capital Analysis")

# -------------------------
# Load Market Cap Data
# -------------------------

df = run_query("""
SELECT
    c.company_name,
    s.market_cap_category,
    s.index_weight_pct
FROM sectors s
JOIN companies c
ON s.company_id = c.id
ORDER BY c.company_name
""")

# -------------------------
# Capital Category Selection
# -------------------------

categories = sorted(df["market_cap_category"].dropna().unique())

selected_category = st.selectbox(
    "Select Market Cap Category",
    categories
)

capital_df = df[
    df["market_cap_category"] == selected_category
]

st.success(
    f"Companies in {selected_category}: {len(capital_df)}"
)

# -------------------------
# KPI Cards
# -------------------------

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Companies",
        len(capital_df)
    )

with col2:
    st.metric(
        "Average Index Weight (%)",
        f"{capital_df['index_weight_pct'].mean():.2f}"
    )

st.dataframe(
    capital_df,
    use_container_width=True,
    hide_index=True
)

import plotly.express as px

st.subheader("Index Weight Comparison")

chart_df = capital_df.sort_values(
    "index_weight_pct",
    ascending=False
)

fig = px.bar(
    chart_df,
    x="company_name",
    y="index_weight_pct",
    color="index_weight_pct",
    title=f"{selected_category} Companies"
)

fig.update_layout(
    xaxis_title="Company",
    yaxis_title="Index Weight (%)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("🏆 Top 5 Companies by Index Weight")

top5 = chart_df.head(5)

st.dataframe(
    top5,
    use_container_width=True,
    hide_index=True
)