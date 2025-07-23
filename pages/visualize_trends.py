import streamlit as st
import pandas as pd
import os
import altair as alt

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(page_title="Visualize Trends", page_icon="📈", layout="wide")
st.title("Visualize People Trends")

# ---------------------------------
# Load Data
# ---------------------------------
DATA_PATH = "data/people_data.csv"

@st.cache_data
def load_data():
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        df["joining_date"] = pd.to_datetime(df["joining_date"], errors="coerce")
        return df
    else:
        st.error("Data file not found.")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.warning("No data available.")
    st.stop()

# ---------------------------------
# Layout & Charts
# ---------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧑‍💼 Department Distribution")
    dept_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("department", title="Department"),
        y=alt.Y("count()", title="Number of People"),
        tooltip=["department", "count()"]
    ).properties(height=300)
    st.altair_chart(dept_chart, use_container_width=True)

with col2:
    st.subheader("👥 Gender Distribution")
    gender_counts = df["gender"].value_counts().reset_index()
    gender_counts.columns = ["gender", "count"]

    gender_pie = alt.Chart(gender_counts).mark_arc().encode(
        theta="count:Q",
        color=alt.Color("gender:N", legend=alt.Legend(title="Gender")),
        tooltip=["gender:N", "count:Q"]
    ).properties(height=300)

    st.altair_chart(gender_pie, use_container_width=True)

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.subheader("💸 Average Salary by Department")
    avg_salary = df.groupby("department")["salary"].mean().reset_index()

    salary_chart = alt.Chart(avg_salary).mark_bar().encode(
        x=alt.X("salary:Q", title="Average Salary"),
        y=alt.Y("department:N", sort="-x", title="Department"),
        color=alt.Color("department:N", legend=None),
        tooltip=["department", "salary"]
    ).properties(height=350)

    st.altair_chart(salary_chart, use_container_width=True)

with col4:
    st.subheader("📊 Experience vs Salary")
    scatter_chart = alt.Chart(df).mark_circle(size=80).encode(
        x=alt.X("years_of_experience:Q", title="Years of Experience"),
        y=alt.Y("salary:Q", title="Salary"),
        color="department:N",
        tooltip=["name", "salary", "years_of_experience"]
    ).interactive().properties(height=300)
    st.altair_chart(scatter_chart, use_container_width=True)

st.divider()

col5, col6 = st.columns(2)

with col5:
    st.subheader("📅 Joinings Over Time")
    line_chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X("yearmonth(joining_date):T", title="Joining Date"),
        y=alt.Y("count()", title="Number of Joinees"),
        tooltip=["yearmonth(joining_date):T", "count()"]
    ).properties(height=300)
    st.altair_chart(line_chart, use_container_width=True)

with col6:
    st.subheader("🌍 Employees by Location and Dept")
    location_dept = df.groupby(["location", "department"]).size().reset_index(name="count")
    heatmap = alt.Chart(location_dept).mark_rect().encode(
        x=alt.X("department:N"),
        y=alt.Y("location:N"),
        color=alt.Color("count:Q", scale=alt.Scale(scheme='blues')),
        tooltip=["location", "department", "count"]
    ).properties(height=300)
    st.altair_chart(heatmap, use_container_width=True)

st.divider()

# Final row with Employment Type + Multi-line Salary Trend
col7, col8 = st.columns(2)

with col7:
    st.subheader("💼 Employment Type by Department")
    emp_type_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("department:N", title="Department"),
        y=alt.Y("count():Q", title="Count"),
        color=alt.Color("employment_type:N", title="Employment Type"),
        tooltip=["department", "employment_type", "count()"]
    ).properties(height=350)
    st.altair_chart(emp_type_chart, use_container_width=True)

with col8:
    st.subheader("📈 Avg Salary by Year & Department")
    df["joining_year"] = df["joining_date"].dt.year
    trend_df = df.groupby(["joining_year", "department"])["salary"].mean().reset_index()
    multiline_chart = alt.Chart(trend_df).mark_line(point=True).encode(
        x=alt.X("joining_year:O", title="Joining Year"),
        y=alt.Y("salary:Q", title="Average Salary"),
        color=alt.Color("department:N"),
        tooltip=["joining_year", "department", "salary"]
    ).properties(height=350)
    st.altair_chart(multiline_chart, use_container_width=True)
