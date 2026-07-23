import streamlit as st

from auth import (
    create_session_table,
    create_user_table
)


# Website settings
st.set_page_config(
    page_title="AI Study Companion",
    page_icon="📚",
    layout="wide"
)


# Create database tables
create_user_table()
create_session_table()


# Home page

st.title("📚 AI Study Companion")

st.write(
    "Your personal AI-powered study platform"
)

st.success("Website setup successful!")


