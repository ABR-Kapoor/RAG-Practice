import streamlit as st
from components.upload import render_upload
from components.chatUI import render_chatui
from components.history_download import render_history_download



st.set_page_config(page_title="Noddy Bot Candidate Resume HR chat", layout="wide")
st.title("Noddy Bot Candidate Resume HR Chat")

render_upload()
render_chatui()
render_history_download()