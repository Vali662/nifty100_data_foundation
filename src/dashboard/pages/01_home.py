import streamlit as st
import plotly.express as px
from utils.db import (
    get_companies,
    get_ratios_by_year,
    get_market_by_year,
    get_sector_summary,
    get_top_quality_companies
)
# -------------------------------
# Page Title
# -------------------------------
st.title("📊 Nifty 100 Analytics Dashboard")

st.markdown("### Home Dashboard")

st.write(
    "Welcome to the Nifty 100 Financial Intelligence Platform."
)

st.divider()
# -------------------------------
# Sidebar - Year Selector
# -------------------------------
st.sidebar.header("Dashboard Filters")

selected_year = st.sidebar.selectbox(
    "Select Financial Year",
    ["2019", "2020", "2021", "2022", "2023", "2024"],
    index=5
)
db_year = f"Mar {selected_year}"

ratios = get_ratios_by_year(db_year)
average_roe = ratios["return_on_equity_pct"].mean()
median_de = ratios["debt_to_equity"].median()
median_revenue_cagr = ratios["revenue_cagr_5yr"].median()
debt_free_companies = (ratios["debt_to_equity"] == 0).sum()
top_quality = get_top_quality_companies(db_year)
market = get_market_by_year(selected_year)
average_pe = market["pe_ratio"].mean()
average_pb = market["pb_ratio"].mean()

st.subheader("📈 Market Valuation Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Average P/E",
        f"{average_pe:.2f}"
    )

with col2:
    st.metric(
        "Average P/B",
        f"{average_pb:.2f}"
    )
# -------------------------------
# Sector Summary
# -------------------------------
sector_data = get_sector_summary()

st.subheader("📊 Sector Breakdown")

fig = px.pie(
    sector_data,
    names="broad_sector",
    values="company_count",
    hole=0.5,
    title="Companies by Sector"
)

fig.update_traces(
    textposition="inside",
    textinfo="percent+label"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📈 Companies by Sector")

bar_fig = px.bar(
    sector_data,
    x="broad_sector",
    y="company_count",
    color="company_count",
    title="Sector-wise Company Count"
)

bar_fig.update_layout(
    xaxis_title="Sector",
    yaxis_title="Number of Companies"
)

st.plotly_chart(
    bar_fig,
    use_container_width=True
)

st.subheader("Top 5 Companies by Composite Quality Score")

st.dataframe(
    top_quality,
    use_container_width=True,
    hide_index=True
)

# -------------------------------
# Top 5 ROE Companies
# -------------------------------
st.subheader("🏆 Top 5 ROE Companies")

top_roe = ratios.nlargest(
    5,
    "return_on_equity_pct"
)[["company_id", "return_on_equity_pct"]]

st.dataframe(
    top_roe,
    use_container_width=True,
    hide_index=True
)

# -------------------------------
# Bottom 5 ROE Companies
# -------------------------------
st.subheader("📉 Bottom 5 ROE Companies")

bottom_roe = ratios.nsmallest(
    5,
    "return_on_equity_pct"
)[["company_id", "return_on_equity_pct"]]

st.dataframe(
    bottom_roe,
    use_container_width=True,
    hide_index=True
)

# -------------------------------
# Top 5 Revenue CAGR Companies
# -------------------------------
st.subheader("🚀 Top 5 Revenue CAGR (5Y) Companies")

top_cagr = ratios.nlargest(
    5,
    "revenue_cagr_5yr"
)[["company_id", "revenue_cagr_5yr"]]

st.dataframe(
    top_cagr,
    use_container_width=True,
    hide_index=True
)

# -------------------------------
# Top 5 Debt-Free Companies
# -------------------------------
st.subheader("💰 Debt-Free Companies")

debt_free = ratios[
    ratios["debt_to_equity"] == 0
][["company_id", "debt_to_equity"]]

st.dataframe(
    debt_free.head(5),
    use_container_width=True,
    hide_index=True
)

median_pe = market["pe_ratio"].median()

st.write(f"### Selected Year: {selected_year}")
# -------------------------------
# KPI 1 - Total Companies
# -------------------------------
companies = get_companies()

total_companies = len(companies)

st.subheader("Key Performance Indicators")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric(
        "Total Companies",
        total_companies
    )

with col2:
    st.metric(
        "Average ROE",
        f"{average_roe:.2f}%"
    )

with col3:
    st.metric(
        "Median P/E",
        f"{median_pe:.2f}"
    )

with col4:
    st.metric(
        "Median D/E",
        f"{median_de:.2f}"
    )

with col5:
    st.metric(
        "Median Revenue CAGR (5Y)",
        f"{median_revenue_cagr:.2f}%"
    )

with col6:
    st.metric(
        "Debt-Free Companies",
        debt_free_companies
    )

st.divider()

st.info(
    f"""
**Dashboard Summary ({selected_year})**

• Companies Analyzed: {total_companies}

• Average ROE: {average_roe:.2f}%

• Median P/E: {median_pe:.2f}

• Debt-Free Companies: {debt_free_companies}

• Top Quality Companies displayed above are ranked using Composite Quality Score.
"""
)