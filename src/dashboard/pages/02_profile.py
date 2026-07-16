import plotly.express as px
import streamlit as st

from utils.db import (
    get_companies,
    get_company_profile,
    get_ratios,
    get_pl
)

st.title("🏢 Company Profile")

st.write("Search and analyze a company.")

# -------------------------------
# Load Companies
# -------------------------------

companies = get_companies()

company_names = companies["id"].tolist()

selected_company = st.selectbox(
    "Select Company",
    company_names
)
profile = get_company_profile(selected_company)
ratios = get_ratios(selected_company)
pl = get_pl(selected_company)

if ratios.empty:
    st.warning("Financial ratio data is not available for this company.")
    st.stop()

latest = ratios.iloc[-1]
# -------------------------------
# Company Profile Card
# -------------------------------
if not profile.empty:

    company = profile.iloc[0]

    st.subheader(company["company_name"])

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(company["company_logo"], width=120)

    with col2:
        st.write(f"**Ticker:** {company['id']}")
        st.write(f"**ROE:** {company['roe_percentage']}%")
        st.write(f"**ROCE:** {company['roce_percentage']}%")

        if company["website"]:
            st.write(f"**Website:** {company['website']}")

    st.markdown("### About Company")

    st.write(company["about_company"])

else:
    st.error("Ticker not found. Please try another.")

# -------------------------------
# Revenue & Net Profit Trend
# -------------------------------

st.subheader("📊 Revenue & Net Profit Trend")

chart_df = pl[["year", "sales", "net_profit"]].copy()

chart_df = chart_df.sort_values("year")

fig = px.bar(
    chart_df,
    x="year",
    y=["sales", "net_profit"],
    barmode="group",
    title="Revenue vs Net Profit"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("📈 ROE & ROCE Trend")

trend_df = ratios[[
    "year",
    "return_on_equity_pct",
    "return_on_capital_employed_pct"
]].copy()

trend_df = trend_df.sort_values("year")
fig = px.line(
    trend_df,
    x="year",
    y=[
        "return_on_equity_pct",
        "return_on_capital_employed_pct"
    ],
    markers=True,
    title="ROE & ROCE Trend"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Pros & Cons")

st.info("Pros & Cons data is not available in the current database.")

st.divider()

st.subheader("📈 Key Financial Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("ROE", f"{latest['return_on_equity_pct']:.2f}%")

with col2:
    st.metric("ROCE", f"{latest['return_on_capital_employed_pct']:.2f}%")

with col3:
    st.metric("Net Profit Margin", f"{latest['net_profit_margin_pct']:.2f}%")

col4, col5, col6 = st.columns(3)

with col4:
    st.metric("Debt / Equity", f"{latest['debt_to_equity']:.2f}")

with col5:
    revenue_cagr = latest["revenue_cagr_5yr"]

if revenue_cagr == revenue_cagr:
    value = f"{revenue_cagr:.2f}%"
else:
    value = "N/A"

st.metric("Revenue CAGR (5Y)", value)

with col6:
    st.metric("Free Cash Flow", f"{latest['free_cash_flow']:.2f}")