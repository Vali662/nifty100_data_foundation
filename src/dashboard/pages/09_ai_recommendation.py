import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="AI Investment Recommendations")

st.title("🤖 AI Investment Recommendations")

score_file = Path("output/company_scores.csv")

if not score_file.exists():

    st.error("company_scores.csv not found.")

    st.stop()

df = pd.read_csv(score_file)

st.success(f"{len(df)} Companies Loaded")

st.sidebar.header("Filters")

rating = st.sidebar.selectbox(
    "Rating",
    ["All"] + sorted(df["rating"].unique().tolist())
)

recommendation = st.sidebar.selectbox(
    "Recommendation",
    ["All"] + sorted(df["recommendation"].unique().tolist())
)

filtered = df.copy()

total_companies = len(filtered)

strong_buy = len(
    filtered[
        filtered["recommendation"] == "Strong Buy"
    ]
)

avg_score = round(
    filtered["investment_score"].mean(),
    2
)

top_score = filtered["investment_score"].max()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Companies", total_companies)
col2.metric("Strong Buy", strong_buy)
col3.metric("Average Score", avg_score)
col4.metric("Top Score", top_score)

if rating != "All":
    filtered = filtered[filtered["rating"] == rating]

if recommendation != "All":
    filtered = filtered[
        filtered["recommendation"] == recommendation
    ]

st.subheader("🏆 Investment Recommendations")

st.dataframe(
    filtered,
    use_container_width=True
)

st.success(f"{len(df)} Companies Loaded")

st.subheader("🏆 Top 10 Investment Picks")

st.subheader("📊 Top 10 Investment Scores")

top10 = filtered.head(10).set_index("company_id")

st.bar_chart(top10["investment_score"])

st.dataframe(df.head(10), use_container_width=True)

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Recommendations",
    data=csv,
    file_name="filtered_company_recommendations.csv",
    mime="text/csv",
)