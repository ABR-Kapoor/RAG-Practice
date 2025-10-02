import streamlit as st
from utils.api import upload_files_api

def render_upload():
    st.subheader("Upload your medical documents (PDF only) :paperclip:")
    uploaded_files = st.sidebar.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True) 
    if st.sidebar.button("Upload and Process") and uploaded_files:
       response = upload_files_api(uploaded_files) 
       if response and response.status_code == 200:
            st.sidebar.success("Files uploaded and processed successfully!")
       else:
            st.sidebar.error("Error uploading files. Please try again.")