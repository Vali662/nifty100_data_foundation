import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Company Recommendation")

st.title("🏢 Company Recommendation")

score_file = Path("output/company_scores.csv")
narrative_file = Path("output/company_narratives.csv")

if not score_file.exists():
    st.error("company_scores.csv not found")
    st.stop()

if not narrative_file.exists():
    st.error("company_narratives.csv not found")
    st.stop()

scores = pd.read_csv(score_file)
narratives = pd.read_csv(narrative_file)

company_list = sorted(scores["company_id"].unique())

search = st.text_input(
    "🔍 Search Company",
    ""
)

filtered_companies = [
    c for c in company_list
    if search.upper() in c.upper()
]

if not filtered_companies:
    st.warning("No matching company found.")
    st.stop()

company = st.selectbox(
    "Select Company",
    filtered_companies
)

company_score = scores[
    scores["company_id"] == company
].iloc[0]

st.subheader("📊 Investment Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Investment Score",
    company_score["investment_score"]
)

col2.metric(
    "Rating",
    company_score["rating"]
)

col3.metric(
    "Recommendation",
    company_score["recommendation"]
)

st.subheader("📝 AI Financial Narrative")

company_narrative = narratives[
    narratives["company_id"] == company
]

if not company_narrative.empty:

    st.info(
        company_narrative.iloc[0]["narrative"]
    )
    st.divider()

else:

    st.warning(
        "No narrative available."
    )

st.subheader("🏅 Company Ranking")

col1, col2 = st.columns(2)

col1.metric(
    "Overall Rank",
    int(company_score["rank"])
)

col2.metric(
    "Investment Score",
    int(company_score["investment_score"])
)

st.subheader("📋 Company Details")

st.dataframe(
    company_score.to_frame().T,
    use_container_width=True
)

st.divider()