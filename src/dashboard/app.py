import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Nifty 100 Analytics",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📊 Nifty 100 Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Company Profile",
        "Screener",
        "Peer Comparison",
        "Trend Analysis",
        "Sector Analysis",
        "Capital Allocation",
        "Annual Reports",
    ],
)

# -----------------------------
# Main Area
# -----------------------------
st.title(page)

st.info(
    "Sprint 4 Dashboard Scaffold\n\n"
    "This is the main dashboard entry point. "
    "Each page will be implemented during Sprint 4."
)

st.write("---")

if page == "Home":
    st.header("🏠 Home")

elif page == "Company Profile":
    st.header("🏢 Company Profile")

elif page == "Screener":
    st.header("🔍 Screener")

elif page == "Peer Comparison":
    st.header("📊 Peer Comparison")

elif page == "Trend Analysis":
    st.header("📈 Trend Analysis")

elif page == "Sector Analysis":
    st.header("🏭 Sector Analysis")

elif page == "Capital Allocation":
    st.header("💰 Capital Allocation")

elif page == "Annual Reports":
    st.header("📄 Annual Reports")