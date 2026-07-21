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

st.subheader("🏆 Top 10 Investment Picks")

st.dataframe(df.head(10), use_container_width=True)