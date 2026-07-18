import streamlit as st
from utils.db import run_query

st.title("📄 Reports & Downloads")

st.write(
    "Download project datasets and reports."
)

# -------------------------
# Load Tables
# -------------------------

financial_ratios = run_query("""
SELECT *
FROM financial_ratios
""")

companies = run_query("""
SELECT *
FROM companies
""")

sectors = run_query("""
SELECT *
FROM sectors
""")

st.subheader("Dataset Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Companies",
        len(companies)
    )

with col2:
    st.metric(
        "Financial Records",
        len(financial_ratios)
    )

with col3:
    st.metric(
        "Sector Records",
        len(sectors)
    )

st.subheader("Download Financial Ratios")

csv = financial_ratios.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Financial Ratios",
    data=csv,
    file_name="financial_ratios.csv",
    mime="text/csv"
)

st.subheader("Download Companies")

company_csv = companies.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Companies",
    data=company_csv,
    file_name="companies.csv",
    mime="text/csv"
)

st.subheader("Download Sectors")

sector_csv = sectors.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Sectors",
    data=sector_csv,
    file_name="sectors.csv",
    mime="text/csv"
)