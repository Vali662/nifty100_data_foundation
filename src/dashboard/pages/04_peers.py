import streamlit as st
import plotly.graph_objects as go

from utils.db import (
    get_companies,
    get_company_peer_group,
    get_peer_comparison,
)

st.title("📊 Peer Comparison")
st.write("Compare a company against its peer group.")

companies = get_companies()

company = st.selectbox(
    "Select Company",
    companies["company_name"]
)

company_id = companies.loc[
    companies["company_name"] == company,
    "id"
].iloc[0]

peer_group = get_company_peer_group(company_id)

if not peer_group.empty:

    group_name = peer_group.iloc[0]["peer_group_name"]

    st.success(f"Peer Group: {group_name}")

    comparison = get_peer_comparison(group_name)

    st.subheader("Peer Comparison")

    # Highlight benchmark
    def highlight_benchmark(row):
        if row["is_benchmark"] == 1:
            return ["background-color: lightgreen"] * len(row)
        return [""] * len(row)

    styled_df = comparison.style.apply(highlight_benchmark, axis=1)

    st.dataframe(styled_df)

    # ----------------------------
    # Radar Chart
    # ----------------------------
    selected_data = comparison[
        comparison["company_name"] == company
    ]

    if not selected_data.empty:

        metrics = [
            "return_on_equity_pct",
            "return_on_capital_employed_pct",
            "net_profit_margin_pct",
            "revenue_cagr_5yr",
            "pat_cagr_5yr",
            "composite_quality_score"
        ]

        values = selected_data.iloc[0][metrics].fillna(0).tolist()
        peer_average = (
    comparison[metrics]
    .mean()
    .fillna(0)
    .tolist()
)

        fig = go.Figure()

        fig.add_trace(
            go.Scatterpolar(
                r=values,
                theta=[
                    "ROE",
                    "ROCE",
                    "NPM",
                    "Revenue CAGR",
                    "PAT CAGR",
                    "Quality Score"
                ],
                fill="toself",
                name=company
            )
        )

        fig.add_trace(
    go.Scatterpolar(
        r=peer_average,
        theta=[
            "ROE",
            "ROCE",
            "NPM",
            "Revenue CAGR",
            "PAT CAGR",
            "Quality Score"
        ],
        fill="toself",
        name="Peer Average"
    )
)

        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True)
            ),
            showlegend=True,
            title="Financial Radar"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Download CSV
    # ----------------------------
    csv = comparison.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Peer Comparison CSV",
        data=csv,
        file_name="peer_comparison.csv",
        mime="text/csv"
    )

else:
    st.warning("Peer group not found.")