# app.py - Main entry point
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

st.set_page_config(
    page_title="HireIQ - AI Hiring Assistant",
    page_icon="",
    layout="wide"
)

# Load External CSS
def load_css():
    try:
        with open("styles.css", "r") as f:
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("styles.css not found")

load_css()

# Logo Component with professional icon
st.sidebar.markdown("""
<div class="logo-container">
    <div class="logo-wrapper">
        <div class="logo-icon">
            <div class="logo-outer"></div>
            <div class="logo-inner"></div>
        </div>
        <div class="logo-text">
            <span class="logo-hire">Hire</span><span class="logo-iq">IQ</span>
        </div>
    </div>
    <div class="logo-subtitle">
        <div class="subtitle-line1">AI-Powered</div>
        <div class="subtitle-line2">Hiring Assistant</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<div class='nav-header'>Navigation</div>", unsafe_allow_html=True)

nav_options = [
    ("Home", "▶", "show_home"),
    ("CV Screening", "◆", "show_cv_screening"),
    ("Dashboard", "○", "show_dashboard"),
    ("Interview Questions", "●", "show_interview"),
    ("Bias Detector", "◇", "show_bias_detector")
]

page = st.sidebar.radio(
    "Navigation",
    [f"{icon}  {name}" for name, icon, _ in nav_options],
    index=0,
    label_visibility="collapsed"
)

page_key = next(key for name, icon, key in nav_options if f"{icon}  {name}" == page)

if page_key == "show_home":
    from components.home import show_home
    show_home()
elif page_key == "show_cv_screening":
    from components.cv_screening import show_cv_screening
    show_cv_screening()
elif page_key == "show_dashboard":
    from components.dashboard import show_dashboard
    show_dashboard()
elif page_key == "show_interview":
    from components.interview import show_interview
    show_interview()
elif page_key == "show_bias_detector":
    from components.bias_detector import show_bias_detector
    show_bias_detector()

# Sidebar Footer
st.sidebar.markdown("""
<div class="sidebar-footer">
    <div class="sidebar-footer-inner">
        <div class="sidebar-footer-status">
            <div class="sidebar-footer-dot"></div>
            <span class="sidebar-footer-text">System Online</span>
        </div>
        <div class="sidebar-footer-credit">Powered by AI & Hugging Face</div>
    </div>
</div>
""", unsafe_allow_html=True)
