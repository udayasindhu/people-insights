import streamlit as st

# ----------------------------
# Page config (title, icon)
# ----------------------------
st.set_page_config(
    page_title="People Insights Dashboard",
    page_icon="👥",
    layout="wide"
)

# ----------------------------
# Main Layout
# ----------------------------
st.title("📊 Welcome to the People Insights Dashboard")
st.markdown(
    "This dashboard helps you **upload**, **view**, and **analyze** people data step by step."
)

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 Explore Data")
    st.write("""
        Browse and interact with your dataset in a clean table view.
        You’ll be able to:
        - Apply filters (e.g., by age, job role)
        - Search records easily
        - View updated data in real time
        """)
    if st.button("Go to Explore Data"):
        st.switch_page("pages/explore_data.py")

with col2:
    st.subheader("📈 Visualize Trends")
    st.write("""
        Generate insightful visualizations to understand your data better.
        This section will include:
        - Age distribution charts
        - Role/category breakdowns
        - Interactive plots and trends
        """)
    if st.button("Go to Visualize Trends"):
        st.switch_page("pages/visualize_trends.py")

# Footer or info
st.markdown("---")
st.info("Start by adding some data or exploring sample data from the sidebar.")

