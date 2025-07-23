import streamlit as st
import pandas as pd
import os
import re
from datetime import date

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(page_title="Explore Data", page_icon="🔍", layout="wide")
st.title("Explore People Data")

# ---------------------------------
# Load People Data from CSV
# ---------------------------------
DATA_PATH = "data/people_data.csv"

def load_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    else:
        return pd.DataFrame(columns=[
            "id", "name", "email", "department", "dob", "gender", "salary",
            "years_of_experience", "location", "employment_type", "joining_date"
        ])

# ---------------------------------
# Session State Initialization
# ---------------------------------
if "data" not in st.session_state:
    st.session_state["data"] = load_data()

data = st.session_state["data"]

# ---------------------------------
# Form to Add/Update Entry
# ---------------------------------
st.subheader("➕ Add or Update a Person")

with st.form("add_person_form", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        id_input = st.number_input("ID", min_value=1, step=1)
        name_input = st.text_input("Name")
        gender_input = st.selectbox("Gender", options=["Male", "Female", "Other", "Unknown"])
        salary_input = st.number_input("Salary", min_value=0)
    with col2:
        email_input = st.text_input("Email")
        dept_input = st.selectbox("Department", options=["IT", "HR", "Sales", "Finance", "Support", "Other"])
        experience_input = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
        location_input = st.text_input("Location")
    with col3:
        dob_input = st.date_input("Date of Birth", max_value=date.today(), min_value=date(1950, 1, 1))
        emp_type_input = st.selectbox("Employment Type", options=["Intern", "Contract", "Full-time", "Part-time"])
        joining_input = st.date_input("Joining Date", max_value=date.today(), min_value=date(2000, 1, 1))

    submitted = st.form_submit_button("Add / Update")

    EMAIL_REGEX = r"^[\w\.-]{2,}@[\w\.-]{2,}\.\w+$"

    if submitted:
        if not name_input.strip() or not email_input.strip() or not location_input.strip():
            st.warning("Please fill in all required fields.")
        elif not re.match(EMAIL_REGEX, email_input):
            st.error("Please enter a valid email address.")
        else:
            new_entry = {
                "id": int(id_input),
                "name": name_input.strip(),
                "email": email_input.strip(),
                "department": dept_input,
                "dob": dob_input.strftime("%Y-%m-%d"),
                "gender": gender_input,
                "salary": salary_input,
                "years_of_experience": experience_input,
                "location": location_input.strip(),
                "employment_type": emp_type_input,
                "joining_date": joining_input.strftime("%Y-%m-%d")
            }

            # Remove duplicate by ID and insert new
            existing_data = st.session_state["data"]
            existing_data = existing_data[existing_data["id"] != int(id_input)]
            updated_data = pd.concat([existing_data, pd.DataFrame([new_entry])], ignore_index=True)
            st.session_state["data"] = updated_data.sort_values("id").reset_index(drop=True)

            st.toast(f"Entry for ID {id_input} saved.", icon="✅")

# ---------------------------------
# Upload CSV to Merge
# ---------------------------------
st.subheader("📤 Upload CSV File to Add/Update Multiple People")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    try:
        uploaded_df = pd.read_csv(uploaded_file)

        required_columns = [
            "id", "name", "email", "department", "dob", "gender", "salary",
            "years_of_experience", "location", "employment_type", "joining_date"
        ]

        missing_cols = [col for col in required_columns if col not in uploaded_df.columns]

        if missing_cols:
            st.error(f"CSV is missing required columns: {', '.join(missing_cols)}")
        else:
            combined = pd.concat([st.session_state["data"], uploaded_df], ignore_index=True)
            combined = combined.drop_duplicates(subset="id", keep="last")
            st.session_state["data"] = combined.sort_values("id").reset_index(drop=True)
            st.success("✅ CSV data merged successfully!")

    except Exception as e:
        st.error(f"Error reading CSV: {e}")

# ---------------------------------
# Display Final Data (with Search & Pagination)
# ---------------------------------
st.subheader("📋 People Data Table")

# 🔍 Search
search_term = st.text_input("Search by name, email, department or location", "").strip().lower()

filtered_data = st.session_state["data"]
if search_term:
    filtered_data = filtered_data[
        filtered_data["name"].str.lower().str.contains(search_term) |
        filtered_data["email"].str.lower().str.contains(search_term) |
        filtered_data["department"].str.lower().str.contains(search_term) |
        filtered_data["location"].str.lower().str.contains(search_term)
    ]

# 📄 Pagination
page_size = 100
total_rows = len(filtered_data)
total_pages = max(1, (total_rows - 1) // page_size + 1)

if "current_page" not in st.session_state:
    st.session_state["current_page"] = 1
current_page = st.session_state["current_page"]
current_page = min(max(1, current_page), total_pages)

start_idx = (current_page - 1) * page_size
end_idx = start_idx + page_size
paginated_data = filtered_data.iloc[start_idx:end_idx]

# Display table
st.dataframe(
    paginated_data[
        ["id", "name", "email", "department", "dob", "gender", "salary",
         "years_of_experience", "location", "employment_type", "joining_date"]
    ],
    use_container_width=True,
    hide_index=True
)

# 📌 Footer with record count and navigation
left_col, right_col = st.columns([5, 1])
with left_col:
    st.caption(f"Showing {start_idx + 1}-{min(end_idx, total_rows)} of {total_rows} records")
with right_col:
    col_prev, col_next = st.columns([1, 1])
    with col_prev:
        if st.button("⏮", help="Previous Page", use_container_width=True, disabled=(current_page <= 1)):
            st.session_state["current_page"] = current_page - 1
            st.rerun()
    with col_next:
        if st.button("⏭", help="Next Page", use_container_width=True, disabled=(current_page >= total_pages)):
            st.session_state["current_page"] = current_page + 1
            st.rerun()
