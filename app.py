# app.py — Main entry point
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="HireIQ - AI Hiring Assistant",
    page_icon="🐱‍🏍",
    layout="wide"
)

# Import page modules
from components.home import show_home
from components.cv_screening import show_cv_screening
from components.dashboard import show_dashboard
from components.interview import show_interview
from components.bias_detector import show_bias_detector
# Sidebar
st.sidebar.title("🐱‍🏍 HireIQ")
page = st.sidebar.radio("Go to:", [
    "🏠 Home",
    "📄 Screen CVs",
    "📊 Dashboard",
    "❓ Interview Questions",
    "🔍 Bias Detector"
])

# Route to correct page
if page == "🏠 Home":
    show_home()
elif page == "📄 Screen CVs":
    show_cv_screening()
elif page == "📊 Dashboard":
    show_dashboard()
elif page == "❓ Interview Questions":
    show_interview()
elif page == "🔍 Bias Detector":
    show_bias_detector()