# pages/home.py
import streamlit as st

def show_home():
    # Hero Section
    st.markdown("""
        <div style='text-align: center; padding: 40px 0px;'>
            <h1 style='font-size: 3em;'>🐱‍🏍 HireIQ</h1>
            <h3 style='color: gray;'>Free AI-Powered Hiring Assistant for Pakistani Startups & SMEs</h3>
            <p style='font-size: 1.2em;'>Screen CVs faster, fairer and smarter — powered by AI!</p>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Stats Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("⚡ Time Saved", "80%", "vs manual screening")
    with col2:
        st.metric("🎯 Accuracy", "95%", "skill matching")
    with col3:
        st.metric("🔍 Bias Checks", "5 Types", "detected automatically")
    with col4:
        st.metric("💰 Cost", "FREE", "no subscription needed")

    st.divider()

    # Features Section
    st.subheader("🚀 What Can HireIQ Do?")
    col1, col2 = st.columns(2)

    with col1:
        st.success("""
        **📄 CV Screening**
        - Paste CV + Job Description
        - AI scores candidate match
        - Shows matched & missing skills
        - Gives Hire/Maybe/Reject verdict
        - Explains WHY with full analysis
        """)
        st.success("""
        **📊 Candidate Dashboard**
        - Compare up to 5 candidates
        - Visual bar chart comparison
        - Automatic ranking by score
        - Side by side skill analysis
        """)

    with col2:
        st.info("""
        **❓ Interview Questions**
        - Auto-generated from CV gaps
        - 3 difficulty levels
        - Skill verification questions
        - Behavioral questions included
        """)
        st.info("""
        **🔍 Bias Detector**
        - Detects 5 types of bias
        - Age, Gender, Origin bias
        - Fairness score calculated
        - Improvement suggestions
        """)

    st.divider()

    # How it works
    st.subheader("⚡ How It Works — 3 Simple Steps!")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.warning("""
        **Step 1️⃣**
        📋 Paste your Job Description
        and Candidate CV
        """)
    with col2:
        st.warning("""
        **Step 2️⃣**
        🤖 AI analyzes skills,
        scores the match
        and detects bias
        """)
    with col3:
        st.warning("""
        **Step 3️⃣**
        📊 Get instant results —
        Hire/Maybe/Reject
        with full explanation!
        """)

    st.divider()

    # Footer
    st.markdown("""
        <div style='text-align: center; color: gray; padding: 20px;'>
            <p>Built with ❤️ for Pakistani Businesses | Powered by AI & Hugging Face</p>
            <p>🐱‍🏍 HireIQ — Making hiring faster, fairer and smarter!</p>
        </div>
    """, unsafe_allow_html=True)