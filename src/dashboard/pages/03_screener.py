import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[3]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))
from screener.engine import run_preset
import screener.engine
st.write("Engine file:", screener.engine.__file__)
#from utils.db import run_query

st.title("🔍 Stock Screener")

st.write("Screen Nifty 100 companies using predefined strategies.")

preset = st.selectbox(
    "Choose a Screener",
    [
        "Quality Compounder",
        "Value Pick",
        "Growth Accelerator",
        "Dividend Champion",
        "Debt Free Bluechip",
        "Turnaround Watch"
    ]
)

st.write("Selected Screener:", preset)

preset_mapping = {
    "Quality Compounder": "quality_compounder",
    "Value Pick": "value_pick",
    "Growth Accelerator": "growth_accelerator",
    "Dividend Champion": "dividend_champion",
    "Debt Free Bluechip": "debt_free_bluechip",
    "Turnaround Watch": "turnaround_watch"
}

result = run_preset(preset_mapping[preset])

st.write("Rows returned:", len(result))
st.write(result.head())

st.subheader(f"Companies Found: {len(result)}")

st.dataframe(
    result[
        [
            "company_id",
            "return_on_equity_pct",
            "debt_to_equity",
            "composite_quality_score"
        ]
    ],
    use_container_width=True
)