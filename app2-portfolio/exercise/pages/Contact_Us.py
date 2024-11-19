import streamlit as st
import pandas as pd
from send_email import send_email

df = pd.read_csv("topics.csv")

topics = df["topic"]

with st.form("email_form"):
    email_address = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discuss?", options=topics)
    raw_message = st.text_area("Text")
    message = f"""\
Subject: New email from {email_address}

From: {email_address}
Topic {topic}
{raw_message}
"""

    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your email was sent successfully.")
