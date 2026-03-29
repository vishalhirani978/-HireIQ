# pages/cv_screening.py
import streamlit as st
from huggingface_hub import InferenceClient
from utils.helpers import extract_skills, get_match_score, get_recommendation
import os

def show_cv_screening():
    st.title("📄 CV Screening")
    st.write("Paste the Job Description and Candidate CV below!")

    client = InferenceClient(token=os.getenv("HUGGINGFACE_TOKEN"))

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📋 Job Description")
        job_desc = st.text_area(
            "Paste job description here:",
            height=300,
            placeholder="e.g. We need a Python developer with 2 years experience in ML..."
        )
    with col2:
        st.subheader("👤 Candidate CV")
        cv_text = st.text_area(
            "Paste candidate CV here:",
            height=300,
            placeholder="e.g. John Doe, 3 years Python experience, worked on ML projects..."
        )

    if st.button("🔍 Screen This Candidate!", use_container_width=True):
        if job_desc and cv_text:
            with st.spinner("AI is analyzing the CV... 🤔"):
                score, percentage = get_match_score(job_desc, cv_text)
                job_skills = extract_skills(job_desc)
                cv_skills = extract_skills(cv_text)
                matched_skills = [s for s in job_skills if s in cv_skills]
                missing_skills = [s for s in job_skills if s not in cv_skills]
                recommendation = get_recommendation(percentage, matched_skills, missing_skills)

                analysis_text = (
                    f"Job requires: {job_desc[:300]}. "
                    f"Candidate has: {cv_text[:300]}. "
                    f"Matched skills: {', '.join(matched_skills)}. "
                    f"Missing skills: {', '.join(missing_skills)}. "
                    f"Overall match score: {percentage}%."
                )
                ai_summary = client.summarization(
                    analysis_text,
                    model="facebook/bart-large-cnn"
                )
                explanation = ai_summary.summary_text

            st.divider()
            st.subheader("📊 Screening Results")

            if percentage >= 70:
                st.success(f"✅ Match Score: {percentage}% — Strong Match!")
            elif percentage >= 40:
                st.warning(f"⚠️ Match Score: {percentage}% — Partial Match")
            else:
                st.error(f"❌ Match Score: {percentage}% — Weak Match")

            st.progress(score)

            st.subheader("🎯 Hiring Recommendation:")
            if percentage >= 70:
                st.success(recommendation)
            elif percentage >= 40:
                st.warning(recommendation)
            else:
                st.error(recommendation)

            col1, col2 = st.columns(2)
            with col1:
                st.subheader("✅ Matched Skills:")
                if matched_skills:
                    for skill in matched_skills:
                        st.success(f"✅ {skill}")
                else:
                    st.write("No matched skills found.")
            with col2:
                st.subheader("❌ Missing Skills:")
                if missing_skills:
                    for skill in missing_skills:
                        st.error(f"❌ {skill}")
                else:
                    st.write("No missing skills — great candidate!")

            st.subheader("🤖 AI Analysis:")
            st.write(explanation)

        else:
            st.warning("⚠️ Please paste both Job Description and CV!")