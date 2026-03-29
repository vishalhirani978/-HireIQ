# pages/interview.py
import streamlit as st
from utils.helpers import extract_skills
from backend.question_gen import generate_questions

def show_interview():
    st.title("❓ Interview Questions Generator")
    st.write("Generate smart interview questions based on job requirements and candidate gaps!")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📋 Job Description")
        jd = st.text_area("Paste job description here:", height=250,
                          placeholder="e.g. We need a Python developer with ML experience...")
    with col2:
        st.subheader("👤 Candidate CV")
        cv = st.text_area("Paste candidate CV here:", height=250,
                          placeholder="e.g. Ahmed Khan, Python developer, 2 years experience...")

    difficulty = st.select_slider("Question Difficulty:", options=["Easy", "Medium", "Hard"], value="Medium")
    num_questions = st.slider("Total number of questions:", 3, 10, 5)

    if st.button("🎯 Generate Interview Questions!", use_container_width=True):
        if jd and cv:
            with st.spinner("AI is generating questions... 🤔"):
                job_skills = extract_skills(jd)
                cv_skills = extract_skills(cv)
                missing_skills = [s for s in job_skills if s not in cv_skills]
                matched_skills = [s for s in job_skills if s in cv_skills]
                questions = generate_questions(matched_skills, missing_skills, difficulty, num_questions)

            st.divider()
            st.subheader("🎯 Generated Interview Questions")
            st.write(f"**Total: {num_questions} questions | Difficulty: {difficulty}**")

            if questions["gap"]:
                st.subheader(f"🔴 Skill Gap Questions ({questions['gap_count']}):")
                for i, q in enumerate(questions["gap"], 1):
                    st.error(f"**Q{i}.** {q}")

            if questions["verify"]:
                st.subheader(f"🟢 Skill Verification Questions ({questions['verify_count']}):")
                for i, q in enumerate(questions["verify"], 1):
                    st.success(f"**Q{i}.** {q}")

            if questions["difficulty"]:
                st.subheader(f"🟡 {difficulty} Level Questions ({questions['difficulty_count']}):")
                for i, q in enumerate(questions["difficulty"], 1):
                    st.warning(f"**Q{i}.** {q}")
        else:
            st.warning("⚠️ Please paste both Job Description and CV!")