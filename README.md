# People Insights Dashboard (Streamlit)

A beginner-friendly **Streamlit** dashboard to upload, explore, and visualize people data. Developed incrementally to demonstrate key Streamlit capabilities like file upload, interactive filters, dynamic charts, multi-page layout, and optional authentication.

---

## 🚀 Goal

Create a fully functional dashboard where users can:
- Upload people data (CSV/JSON)
- View, filter, and export data
- Visualize demographic trends (e.g., age, role)
- Add new entries via form
- Manage document uploads (resumes, certificates, images)
- Optionally support login and deploy to the cloud

---

## 🛠 Tech Stack

- **Python 3.11**
- **Streamlit 1.46.1**
- **Pandas** — Data handling
- **Matplotlib / Altair / Plotly** — Data visualizations

---

## 🧭 Roadmap & Features

| Phase | Feature                   | Description                                                   |
|-------|---------------------------|---------------------------------------------------------------|
| 1     | UI Setup                  | Add title, layout, sidebar, and columns                       |
| 2     | Data Display              | Load and filter data in a table format                        |
| 3     | Add Entry via Form        | Input form for name, age, role, etc.                          |
| 4     | Visualize Demographics    | Age histogram, role-based charts                              |
| 5     | File Upload               | Upload CSV/JSON using `st.file_uploader`                      |
| 6     | Data Export               | Export filtered data as CSV                                   |
| 7     | Multipage Navigation      | Separate views: Dashboard, Add, Upload                        |
| 8     | Styling & Theming         | Page config, layout enhancements                              |
| 9     | Authentication (Optional) | Login with `st.session_state`                                 |
| 10    | Document Vault            | Upload/view/download PDFs or images in a centralized page     |
| 11    | Deployment                | Deploy to Streamlit Cloud or Hugging Face Spaces              |

---

## ✨ Feature Details

The People Insights Dashboard includes the following key features:

### 🔍 Data Exploration
- **Upload People Data**
  Upload `.csv` file using Streamlit’s file uploader. The uploaded data is stored and used across pages.

- **Interactive Data Table**
  View all uploaded data in a structured table with built-in support for:
  - Column sorting
  - Dynamic filtering
  - Scrollable view for large datasets
  - Auto sizing columns
  - Pinning columns
  - Hide Columns etc
  - Full screen table

- **Filter by Field**
  Use multiselect filters to narrow down results by:
  - Name
  - Email
  - Department etc

- **Export Data**
  Download the filtered data as a `.csv` file with one click.

---

### 📈 Visualize Trends
- **Charts for Demographics**
  Generate visual insights using:
  - Age distribution histograms
  - Gender-based pie charts
  - Salary and experience scatter plots
  - Role or department breakdowns

- **Altair & Matplotlib Support**
  Lightweight charts are rendered using Altair by default. Matplotlib/Plotly can be swapped if needed.

---

### 📝 Add New Records

- **Add People via Form**
  Easily add or update individuals in the dataset using a structured form that includes:

  - **ID** — Unique numeric identifier
  - **Name** — Full name of the person
  - **Email** — Valid email address
  - **Department** — e.g., IT, HR, Finance
  - **Date of Birth** — Selected via date picker
  - **Gender** — Male, Female, or Other
  - **Salary** — Numeric value in local currency
  - **Years of Experience** — Integer value (0–50)
  - **Location** — City or branch location
  - **Employment Type** — Intern, Contract, Full-time, Part-time
  - **Joining Date** — Date of joining the company

- **Auto Merge by ID**
  If an ID already exists, the record will be updated instead of duplicated.

- **CSV Upload Support**
  Users can upload a CSV file with the same structure to bulk import people.
  The system automatically merges and deduplicates based on the `id` column.

- **Input Validation & Feedback**
  Validates required fields and email format. Success messages appear after save.

---

### 🗂 Central Document Vault
- **Upload Documents**
  Upload and manage resumes, certificates, or profile pictures. Supported formats:
  - PDF
  - JPG, PNG, JPEG

- **View Files Inline**
  PDFs are rendered inline using an embedded viewer (iframe). Images are shown in a responsive gallery.

- **Download Documents**
  Each uploaded document can be downloaded individually.

- **Categorized Display**
  Files are visually grouped based on their type (PDF vs Image).

---

## 📁 Project Structure

<pre lang="markdown">
people_insights/
├── app.py                       # Main entry point
├── README.md                    # Project documentation
├── data/
│   └── people_data.csv          # Sample people dataset
├── pages/
│   ├── explore_data.py          # View & filter uploaded data
│   ├── visualize_trends.py      # Demographic visualizations
│   └── central_document_vault.py # Document manager for PDFs/images
└── utils/
    └── helpers.py               # Reusable helper functions
</pre>

---

## Getting Started

### Prerequisites

- Python 3.8 to 3.12
- pip → Comes with Python
- Streamlit, Pandas, and Matplotlib

---

### 1️. Install Python (if not already installed)

Download and install Python from the official website:
https://www.python.org/downloads/

> **Important:** During installation, check the box that says **"Add Python to PATH"**.

After installing, open a terminal or command prompt and run:

`python --version`

### 2. Install Required Libraries

Install the app dependencies, open a terminal or command prompt and run:

`pip install streamlit pandas matplotlib`

This installs:

- Streamlit → for building and running the app
- Pandas → for handling and analyzing data
- Matplotlib → for creating charts

### 3. Run the Application
Once your `app.py` file is created, go to the folder where `app.py` is present and start the app by running the below command:

`streamlit run app.py`

This will automatically open your app in the browser at:
http://localhost:8501

---
## Functionality
[🎥 Watch the Functionality Demo](https://github.com/udayasindhu/people-insights/raw/main/Functionality.mp4)
