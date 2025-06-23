import streamlit as st
from streamlit_ui.utils import run_feedback_pipeline
from tools.bigquery_utils import get_feedback_record
from tools.summarizer_tool import summarize_with_gemini
from tools.classification_tool import classify_text
from tools.priority_tool import assign_priority
from tools.logger_tool import log_to_db
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="InsightMesh", layout="wide")
st.title("🧠 InsightMesh - Feedback Intelligence Dashboard")

# Define Tabs
tabs = st.tabs(["💬 Feedback Analyzer", "📊 Insights", "✨ Summarizer", "📝 Add Feedback"])

# ----------------------- TAB 1: FEEDBACK ANALYZER -----------------------
with tabs[0]:
    st.header("💬 Feedback Analyzer")
    user_feedback = st.text_area("Enter Feedback", height=150)

    if st.button("🔍 Analyze Feedback"):
        if user_feedback.strip():
            with st.spinner("Running multi-agent pipeline..."):
                context, explanation = run_feedback_pipeline(user_feedback)

            st.success("✅ Analysis Complete")

            st.subheader("📦 Final Output Context")
            st.json(context)

            st.subheader("🧠 Agent Explanation")
            st.text_area("Step-by-step pipeline output", explanation, height=250)
        else:
            st.warning("Please enter feedback before analyzing.")

# ----------------------- TAB 2: INSIGHTS -----------------------
with tabs[1]:
    st.header("📊 Feedback Insights Dashboard")

    try:
        records = get_feedback_record()
        if not records:
            st.warning("Sorry,No feedback records found in BigQuery.")
        else:
            df = pd.DataFrame(records)
            df["timestamp"]=pd.to_datetime(df["timestamp"])
            
            st.subheader("🗃️ Recent Feedback Records")
            st.dataframe(df, use_container_width=True)

            st.subheader("📌 Category Distribution")
            st.bar_chart(df["category"].value_counts())

            st.subheader("🔥 Priority Distribution")
            st.bar_chart(df["priority"].value_counts())

            st.subheader("📆 Feedback Over Time")
            timeline = df.groupby(df["timestamp"].dt.date).size()
            st.line_chart(timeline)

    except Exception as e:
        st.error(f"Error fetching feedback records: {e}")

# ----------------------- TAB 3: SUMMARIZER -----------------------
with tabs[2]:
    st.header("✨ Feedback Summarizer (Gemini)")
    input_text = st.text_area("Paste multiple feedback entries for summarization", height=200)

    if st.button("🧠 Summarize Feedback"):
        if input_text.strip():
            with st.spinner("Summarizing using Gemini..."):
                summary = summarize_with_gemini(input_text)
            st.success("✅ Summary Generated")
            st.text_area("📋 Summary Output", summary, height=200)
        else:
            st.warning("Please paste some feedback to summarize.")

# ----------------------- TAB 4: ADD FEEDBACK -----------------------
with tabs[3]:
    st.header("📝 Inject Feedback to BigQuery")

    new_feedback = st.text_input("Enter new feedback")

    if st.button("🚀 Inject into BigQuery"):
        if new_feedback.strip():
            category = classify_text(new_feedback)
            priority = assign_priority(category)
            log_data = {
                "feedback": new_feedback,
                "category": category,
                "priority": priority,
                "timestamp": datetime.utcnow().isoformat()
            }

            try:
                if log_to_db(log_data):
                    st.success("✅ Feedback logged to BigQuery successfully.")
                else:
                    st.error("❌ Failed to log feedback.")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter valid feedback.")








