import streamlit as st
import plotly.express as px

from utils.db import (
    get_companies,
    get_ratios
)

st.title("📈 Trend Analysis")

st.write(
    "Analyze a company's financial metrics over the last 10 years."
)

# -----------------------
# Company Selection
# -----------------------

companies = get_companies()

company = st.selectbox(
    "Select Company",
    companies["company_name"]
)

company_id = companies.loc[
    companies["company_name"] == company,
    "id"
].iloc[0]

st.success(f"Selected Company: {company}")

# -----------------------
# Load Financial Data
# -----------------------

ratios = get_ratios(company_id)

st.write("Financial Data")

st.dataframe(
    ratios,
    use_container_width=True,
    hide_index=True
)

st.subheader("Select Metrics")

metric_options = {
    "ROE": "return_on_equity_pct",
    "ROCE": "return_on_capital_employed_pct",
    "Net Profit Margin": "net_profit_margin_pct",
    "Revenue CAGR (5Y)": "revenue_cagr_5yr",
    "PAT CAGR (5Y)": "pat_cagr_5yr",
    "Debt to Equity": "debt_to_equity",
    "Quality Score": "composite_quality_score"
}

selected_metrics = st.multiselect(
    "Choose up to 3 metrics",
    list(metric_options.keys()),
    default=["ROE"]
)

# Limit to 3 metrics
selected_metrics = selected_metrics[:3]

if selected_metrics:

    chart_data = ratios.copy()

    fig = px.line(
        chart_data,
        x="year",
        y=[metric_options[m] for m in selected_metrics],
        markers=True,
        title=f"{company} - Financial Trend"
    )

    fig.update_layout(
        xaxis_title="Financial Year",
        yaxis_title="Value",
        legend_title="Metrics"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.subheader("📈 Year-over-Year (%) Change")

yoy_data = ratios.copy()

for metric in selected_metrics:
    column = metric_options[metric]
    yoy_data[f"{metric} YoY %"] = (
        yoy_data[column]
        .pct_change()
        * 100
    ).round(2)

display_columns = ["year"] + [
    f"{metric} YoY %"
    for metric in selected_metrics
]

st.dataframe(
    yoy_data[display_columns],
    use_container_width=True,
    hide_index=True
)