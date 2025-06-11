# Placeholder for app.py
import streamlit as st
from streamlit_ui.utils import run_feedback_pipeline

st.set_page_config(page_title="InsightMesh Feedback Pipeline", layout="centered")
st.title("🧠 InsightMesh - Feedback Intelligence")

user_feedback = st.text_area("Enter Feedback:", height=150)

if st.button("Analyze Feedback") and user_feedback:
    with st.spinner("Running analysis..."):
        result = run_feedback_pipeline(user_feedback)
    st.success("✅ Analysis Complete")
    st.write(result)