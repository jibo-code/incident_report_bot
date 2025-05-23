import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Incident Report Bot", layout="centered")

st.title("📝 Incident Reporting Chatbot (Urdu & English)")

st.markdown("Please describe the incident below in Urdu or English:")

user_input = st.text_area("Incident Description", height=200)

if st.button("Submit Report"):
    if user_input.strip() == "":
        st.error("Please enter some description before submitting.")
    else:
        st.success("✅ Incident recorded successfully.")
        st.markdown("### 🔐 Incident Summary")
        st.write(f"🕒 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        st.write(f"🗒️ Description: {user_input}")
