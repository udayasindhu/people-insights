# central_document_vault.py
import streamlit as st
import os
import base64
from pathlib import Path

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="Central Document Vault", page_icon="📁", layout="wide")
st.title("Central Document Vault")

# -----------------------------
# Setup Directories
# -----------------------------
PDF_DIR = Path("data/documents/pdfs")
IMG_DIR = Path("data/documents/images")
PDF_DIR.mkdir(parents=True, exist_ok=True)
IMG_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Upload Section
# -----------------------------
st.header("📤 Upload Files")
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Upload PDF Documents")
    pdf_files = st.file_uploader(
        "Upload PDFs (e.g., certificates, resumes)",
        type=["pdf"],
        accept_multiple_files=True,
        key="pdf_upload"
    )
    if pdf_files:
        for file in pdf_files:
            with open(PDF_DIR / file.name, "wb") as f:
                f.write(file.read())
        st.success(f"Uploaded {len(pdf_files)} PDF(s) successfully.")

with col2:
    st.subheader("🖼️ Upload Images")
    image_files = st.file_uploader(
        "Upload Images (e.g., profile pictures, achievements)",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True,
        key="img_upload"
    )
    if image_files:
        for file in image_files:
            with open(IMG_DIR / file.name, "wb") as f:
                f.write(file.read())
        st.success(f"Uploaded {len(image_files)} image(s) successfully.")

st.divider()

# -----------------------------
# View & Download Section
# -----------------------------
st.header("📂 Stored Files")

pdf_list = sorted([f for f in os.listdir(PDF_DIR) if f.endswith(".pdf")])
img_list = sorted([f for f in os.listdir(IMG_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg"))])

col3, col4 = st.columns(2)

with col3:
    st.subheader("📄 PDF Files")
    if pdf_list:
        for pdf in pdf_list:
            file_path = PDF_DIR / pdf
            with open(file_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode("utf-8")
                pdf_viewer = f"""
                    <iframe
                        src="data:application/pdf;base64,{base64_pdf}"
                        width="100%"
                        height="350px"
                        type="application/pdf">
                    </iframe>
                """
                st.markdown(f"**{pdf}**", unsafe_allow_html=True)
                st.markdown(pdf_viewer, unsafe_allow_html=True)
            with open(file_path, "rb") as download_file:
                st.download_button("⬇️ Download", download_file, file_name=pdf, mime="application/pdf", key=f"pdf_{pdf}")
            st.divider()
    else:
        st.info("No PDF files uploaded yet.")

with col4:
    st.subheader("🖼️ Image Files")
    if img_list:
        for img in img_list:
            image_path = IMG_DIR / img
            st.image(str(image_path), width=250, caption=img)
            with open(image_path, "rb") as f:
                st.download_button("⬇️ Download", f, file_name=img, key=f"img_{img}")
            st.divider()
    else:
        st.info("No image files uploaded yet.")
