from dotenv import load_dotenv
import streamlit as st
from huggingface_hub import InferenceClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os

# Page config
st.set_page_config(
    page_title="HireIQ - AI Hiring Assistant",
    page_icon="🐱‍🏍",
    layout="wide"
)

# API Token
load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
client = InferenceClient(token=API_TOKEN)

# Sidebar
st.sidebar.title("🐱‍🏍 HireIQ")
page = st.sidebar.radio("Go to:", [
    "🏠 Home",
    "📄 Screen CVs",
    "📊 Dashboard",
    "❓ Interview Questions",
    "🔍 Bias Detector"
])

# ─────────────────────────────
# 🏠 HOME PAGE
# ─────────────────────────────
if page == "🏠 Home":
    st.title("🐱‍🏍 HireIQ")
    st.subheader("Free AI-Powered CV Screening for Pakistani Startups & SMEs!")
    st.write("Screen CVs faster, fairer and smarter!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📄 **Screen CVs**\nPaste CV + Job Description → AI scores the match!")
    with col2:
        st.info("📊 **Dashboard**\nCompare multiple candidates visually!")
    with col3:
        st.info("❓ **Interview Questions**\nAI generates smart questions from CV gaps!")

# ─────────────────────────────
# 📄 SCREEN CVs PAGE
# ─────────────────────────────
elif page == "📄 Screen CVs":
    st.title("📄 CV Screening")
    st.write("Paste the Job Description and Candidate CV below!")

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

                # Match Score
                vectorizer = TfidfVectorizer()
                vectors = vectorizer.fit_transform([job_desc, cv_text])
                score = cosine_similarity(vectors[0], vectors[1])[0][0]
                percentage = round(score * 100, 1)

                # Skill Extraction
                def extract_skills(text):
                    skills = [
                        "python", "sql", "java", "machine learning", "ml",
                        "data science", "pandas", "numpy", "scikit-learn",
                        "tensorflow", "keras", "deep learning", "nlp",
                        "communication", "teamwork", "leadership",
                        "javascript", "react", "nodejs", "html", "css",
                        "excel", "powerpoint", "management", "analysis"
                    ]
                    found = []
                    text_lower = text.lower()
                    for skill in skills:
                        if skill in text_lower:
                            found.append(skill.title())
                    return found

                job_skills = extract_skills(job_desc)
                cv_skills = extract_skills(cv_text)
                matched_skills = [s for s in job_skills if s in cv_skills]
                missing_skills = [s for s in job_skills if s not in cv_skills]
                matched_count = len(matched_skills)
                missing_count = len(missing_skills)

                # Hiring Recommendation
                if percentage >= 70:
                    recommendation = f"""
**✅ STRONG HIRE — {percentage}% Match**

This candidate is an excellent fit for the role!

**Why Hire:**
- Matches {matched_count} out of {matched_count + missing_count} required skills
- Matched Skills: {', '.join(matched_skills) if matched_skills else 'N/A'}
- Score above 70% indicates strong alignment with job requirements

**Suggested Action:** Invite for technical interview immediately!
                    """
                elif percentage >= 40:
                    recommendation = f"""
**⚠️ MAYBE — {percentage}% Match**

This candidate partially meets the requirements.

**Why Consider:**
- Matches {matched_count} key skills: {', '.join(matched_skills) if matched_skills else 'None'}
- Shows potential in core areas

**Why Hesitate:**
- Missing {missing_count} skills: {', '.join(missing_skills) if missing_skills else 'None'}
- May need additional training

**Suggested Action:** Consider for interview only if no stronger candidates available.
                    """
                else:
                    recommendation = f"""
**❌ REJECT — {percentage}% Match**

This candidate does not meet the minimum requirements.

**Why Reject:**
- Only matches {matched_count} skills: {', '.join(matched_skills) if matched_skills else 'None'}
- Missing {missing_count} critical skills: {', '.join(missing_skills) if missing_skills else 'None'}
- Score below 40% indicates poor alignment

**Suggested Action:** Do not proceed. Look for stronger candidates.
                    """

                # AI Summary
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

            # Results
            st.divider()
            st.subheader("📊 Screening Results")

            # Score badge
            if percentage >= 70:
                st.success(f"✅ Match Score: {percentage}% — Strong Match!")
            elif percentage >= 40:
                st.warning(f"⚠️ Match Score: {percentage}% — Partial Match")
            else:
                st.error(f"❌ Match Score: {percentage}% — Weak Match")

            # Progress bar
            st.progress(score)

            # Recommendation box
            st.subheader("🎯 Hiring Recommendation:")
            if percentage >= 70:
                st.success(recommendation)
            elif percentage >= 40:
                st.warning(recommendation)
            else:
                st.error(recommendation)

            # Skill columns
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

            # AI Analysis
            st.subheader("🤖 AI Analysis:")
            st.write(explanation)

        else:
            st.warning("⚠️ Please paste both Job Description and CV!")

# ─────────────────────────────
# 📊 DASHBOARD
# ─────────────────────────────
elif page == "📊 Dashboard":
    st.title("📊 Candidates Dashboard")
    st.write("Compare multiple candidates visually and make better hiring decisions!")

    st.subheader("👥 Add Candidates")
    st.write("Add up to 5 candidates to compare them side by side!")

    # Job Description
    job_desc_dash = st.text_area(
        "📋 Paste Job Description:",
        height=150,
        placeholder="e.g. We need a Python developer with ML experience..."
    )

    # Number of candidates
    num_candidates = st.slider("How many candidates?", 2, 5, 3)

    # Candidate inputs
    candidates = []
    for i in range(num_candidates):
        with st.expander(f"👤 Candidate {i+1}"):
            name = st.text_input(f"Candidate {i+1} Name:", key=f"name_{i}")
            cv = st.text_area(
                f"Paste CV:",
                height=150,
                key=f"cv_{i}",
                placeholder="Paste candidate CV here..."
            )
            candidates.append({"name": name, "cv": cv})

    if st.button("📊 Compare All Candidates!", use_container_width=True):
        if job_desc_dash and all(c["cv"] for c in candidates):
            with st.spinner("Analyzing all candidates... 🤔"):

                # Extract skills function
                def extract_skills(text):
                    skills = [
                        "python", "sql", "java", "machine learning", "ml",
                        "data science", "pandas", "numpy", "scikit-learn",
                        "tensorflow", "keras", "deep learning", "nlp",
                        "communication", "teamwork", "leadership",
                        "javascript", "react", "nodejs", "html", "css",
                        "excel", "powerpoint", "management", "analysis"
                    ]
                    found = []
                    text_lower = text.lower()
                    for skill in skills:
                        if skill in text_lower:
                            found.append(skill.title())
                    return found

                # Calculate scores for each candidate
                results = []
                vectorizer = TfidfVectorizer()

                for candidate in candidates:
                    if candidate["cv"] and candidate["name"]:
                        vectors = vectorizer.fit_transform(
                            [job_desc_dash, candidate["cv"]]
                        )
                        score = cosine_similarity(
                            vectors[0], vectors[1]
                        )[0][0]
                        percentage = round(score * 100, 1)

                        job_skills = extract_skills(job_desc_dash)
                        cv_skills = extract_skills(candidate["cv"])
                        matched = [s for s in job_skills if s in cv_skills]
                        missing = [s for s in job_skills if s not in cv_skills]

                        if percentage >= 70:
                            verdict = "✅ HIRE"
                        elif percentage >= 40:
                            verdict = "⚠️ MAYBE"
                        else:
                            verdict = "❌ REJECT"

                        results.append({
                            "name": candidate["name"],
                            "score": percentage,
                            "matched": len(matched),
                            "missing": len(missing),
                            "matched_skills": matched,
                            "missing_skills": missing,
                            "verdict": verdict
                        })

            # Sort by score
            results = sorted(results, key=lambda x: x["score"], reverse=True)

            st.divider()
            st.subheader("🏆 Candidate Rankings")

            # Ranking table
            import pandas as pd
            import matplotlib.pyplot as plt

            df = pd.DataFrame([{
                "Rank": i+1,
                "Name": r["name"],
                "Match Score": f"{r['score']}%",
                "Matched Skills": r["matched"],
                "Missing Skills": r["missing"],
                "Verdict": r["verdict"]
            } for i, r in enumerate(results)])

            st.dataframe(df, use_container_width=True)

            # Bar Chart
            st.subheader("📊 Score Comparison Chart")
            fig, ax = plt.subplots(figsize=(10, 5))
            colors = []
            for r in results:
                if r["score"] >= 70:
                    colors.append("green")
                elif r["score"] >= 40:
                    colors.append("orange")
                else:
                    colors.append("red")

            bars = ax.bar(
                [r["name"] for r in results],
                [r["score"] for r in results],
                color=colors
            )

            # Add score labels on bars
            for bar, r in zip(bars, results):
                ax.text(
                    bar.get_x() + bar.get_width()/2,
                    bar.get_height() + 1,
                    f"{r['score']}%",
                    ha="center",
                    fontweight="bold"
                )

            ax.set_ylabel("Match Score (%)")
            ax.set_title("Candidate Comparison")
            ax.set_ylim(0, 110)
            ax.axhline(y=70, color="green", linestyle="--", alpha=0.5, label="Hire threshold")
            ax.axhline(y=40, color="orange", linestyle="--", alpha=0.5, label="Maybe threshold")
            ax.legend()
            st.pyplot(fig)

            # Skill comparison
            st.subheader("🥇 Top Candidate Details")
            top = results[0]
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("🏆 Best Candidate", top["name"])
            with col2:
                st.metric("📊 Match Score", f"{top['score']}%")
            with col3:
                st.metric("✅ Skills Matched", top["matched"])

            st.success(f"**Recommendation: {top['verdict']} {top['name']}** — highest match at {top['score']}%!")

        else:
            st.warning("⚠️ Please fill in Job Description and all candidate CVs!")

# ─────────────────────────────
# ❓ INTERVIEW QUESTIONS
# ─────────────────────────────
elif page == "❓ Interview Questions":
    st.title("❓ Interview Questions Generator")
    st.write("Generate smart interview questions based on job requirements and candidate gaps!")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📋 Job Description")
        jd = st.text_area(
            "Paste job description here:",
            height=250,
            placeholder="e.g. We need a Python developer with ML experience..."
        )
    with col2:
        st.subheader("👤 Candidate CV")
        cv = st.text_area(
            "Paste candidate CV here:",
            height=250,
            placeholder="e.g. Ahmed Khan, Python developer, 2 years experience..."
        )

    difficulty = st.select_slider(
        "Question Difficulty:",
        options=["Easy", "Medium", "Hard"],
        value="Medium"
    )

    num_questions = st.slider("Total number of questions:", 3, 10, 5)

    if st.button("🎯 Generate Interview Questions!", use_container_width=True):
        if jd and cv:
            with st.spinner("AI is generating questions... 🤔"):

                # Extract skills
                def extract_skills(text):
                    skills = [
                        "python", "sql", "java", "machine learning", "ml",
                        "data science", "pandas", "numpy", "scikit-learn",
                        "tensorflow", "keras", "deep learning", "nlp",
                        "communication", "teamwork", "leadership",
                        "javascript", "react", "nodejs", "html", "css",
                        "excel", "powerpoint", "management", "analysis"
                    ]
                    found = []
                    text_lower = text.lower()
                    for skill in skills:
                        if skill in text_lower:
                            found.append(skill.title())
                    return found

                job_skills = extract_skills(jd)
                cv_skills = extract_skills(cv)
                missing_skills = [s for s in job_skills if s not in cv_skills]
                matched_skills = [s for s in job_skills if s in cv_skills]

                # Distribute questions
                gap_count = min(len(missing_skills), max(1, num_questions // 3))
                verify_count = min(len(matched_skills), max(1, num_questions // 3))
                difficulty_count = num_questions - gap_count - verify_count

                # Gap questions
                all_gap_questions = []
                for skill in missing_skills:
                    all_gap_questions.append(
                        f"You listed {skill} as a requirement but it's not clear in the CV. "
                        f"Can you walk us through your experience with {skill}?"
                    )

                # Verify questions with different templates
                templates = [
                    "Tell me about a specific project where you used {}. What was the outcome?",
                    "How confident are you with {} on a scale of 1-10? Give an example.",
                    "What is the most complex task you have done using {}?",
                    "How long have you been working with {} and what have you built?",
                    "What challenges did you face while using {} and how did you solve them?"
                ]
                all_verify_questions = []
                for i, skill in enumerate(matched_skills):
                    template = templates[i % len(templates)]
                    all_verify_questions.append(template.format(skill))

                # Difficulty questions
                easy_q = [
                    "Tell me about yourself and your background.",
                    "Why are you interested in this position?",
                    "What are your key strengths?",
                    "Where do you see yourself in 5 years?",
                    "Why are you leaving your current job?",
                ]
                medium_q = [
                    "Describe a challenging problem you solved and how you approached it.",
                    "How do you stay updated with the latest technologies in your field?",
                    "Tell me about a time you worked in a team under pressure.",
                    "How do you handle tight deadlines and multiple priorities?",
                    "Describe a situation where you had to learn something quickly.",
                ]
                hard_q = [
                    "Design a scalable ML pipeline for processing 1 million records daily.",
                    "How would you handle model drift in a production environment?",
                    "Explain the trade-offs between precision and recall in your last project.",
                    "How would you architect a real-time recommendation system?",
                    "What strategies would you use to reduce overfitting in a deep learning model?",
                ]

                if difficulty == "Easy":
                    all_difficulty_q = easy_q
                elif difficulty == "Medium":
                    all_difficulty_q = medium_q
                else:
                    all_difficulty_q = hard_q

                # Final selection
                missing_questions = all_gap_questions[:gap_count]
                matched_questions = all_verify_questions[:verify_count]
                extra = all_difficulty_q[:difficulty_count]

            # Show results
            st.divider()
            st.subheader("🎯 Generated Interview Questions")
            st.write(f"**Total: {num_questions} questions | Difficulty: {difficulty}**")

            if missing_questions:
                st.subheader(f"🔴 Skill Gap Questions ({gap_count}):")
                for i, q in enumerate(missing_questions, 1):
                    st.error(f"**Q{i}.** {q}")

            if matched_questions:
                st.subheader(f"🟢 Skill Verification Questions ({verify_count}):")
                for i, q in enumerate(matched_questions, 1):
                    st.success(f"**Q{i}.** {q}")

            if extra:
                st.subheader(f"🟡 {difficulty} Level Questions ({difficulty_count}):")
                for i, q in enumerate(extra, 1):
                    st.warning(f"**Q{i}.** {q}")

        else:
            st.warning("⚠️ Please paste both Job Description and CV!")   
# ─────────────────────────────
# 🔍 BIAS DETECTOR
# ─────────────────────────────
elif page == "🔍 Bias Detector":
    st.title("🔍 Job Description Bias Detector")
    st.write("Detect biased language in job descriptions to ensure fair hiring!")

    job_desc_bias = st.text_area(
        "📋 Paste Job Description to analyze:",
        height=250,
        placeholder="Paste your job description here..."
    )

    if st.button("🔍 Detect Bias!", use_container_width=True):
        if job_desc_bias:
            with st.spinner("Analyzing for bias... 🤔"):

                # Bias word dictionary
                bias_dict = {
                    "Age Bias": {
                        "words": [
                            "young", "energetic", "fresh graduate", "recent graduate",
                            "digital native", "old", "mature", "experienced only",
                            "years old", "age limit", "under 30", "under 25"
                        ],
                        "color": "🔴",
                        "suggestion": "Remove age-related language — focus on skills and experience instead!"
                    },
                    "Gender Bias": {
                        "words": [
                            "he must", "she must", "him", "her", "guys",
                            "manpower", "mankind", "man the", "salesman",
                            "businessman", "craftsman", "chairman", "freshman"
                        ],
                        "color": "🔴",
                        "suggestion": "Use gender-neutral language like 'they', 'the candidate', 'team member'!"
                    },
                    "Origin Bias": {
                        "words": [
                            "native speaker", "mother tongue", "born in",
                            "local candidate", "nationals only", "citizens only",
                            "local residents", "must be from"
                        ],
                        "color": "🔴",
                        "suggestion": "Focus on language proficiency level instead of origin!"
                    },
                    "Appearance Bias": {
                        "words": [
                            "well groomed", "presentable", "attractive",
                            "good looking", "physically fit", "slim",
                            "height", "weight", "appearance"
                        ],
                        "color": "🟡",
                        "suggestion": "Only mention appearance requirements if strictly necessary for the role!"
                    },
                    "Exclusionary Language": {
                        "words": [
                            "must be", "only", "exclusively", "no exceptions",
                            "strictly", "mandatory background", "specific religion",
                            "specific sect", "caste"
                        ],
                        "color": "🟡",
                        "suggestion": "Use inclusive language that welcomes diverse candidates!"
                    }
                }

                # Detect bias
                found_biases = {}
                text_lower = job_desc_bias.lower()

                for bias_type, data in bias_dict.items():
                    found_words = []
                    for word in data["words"]:
                        if word.lower() in text_lower:
                            found_words.append(word)
                    if found_words:
                        found_biases[bias_type] = {
                            "words": found_words,
                            "color": data["color"],
                            "suggestion": data["suggestion"]
                        }

                # Calculate bias score
                total_checks = len(bias_dict)
                biased_count = len(found_biases)
                clean_count = total_checks - biased_count
                bias_percentage = round((biased_count / total_checks) * 100)
                fairness_score = 100 - bias_percentage

            # Show results
            st.divider()
            st.subheader("📊 Bias Analysis Results")

            # Fairness score
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("🎯 Fairness Score", f"{fairness_score}%")
            with col2:
                st.metric("⚠️ Bias Types Found", biased_count)
            with col3:
                st.metric("✅ Clean Categories", clean_count)

            # Progress bar
            st.progress(fairness_score / 100)

            # Overall verdict
            if fairness_score >= 80:
                st.success("✅ This job description is largely bias-free! Minor improvements possible.")
            elif fairness_score >= 60:
                st.warning("⚠️ This job description has some bias — review highlighted issues!")
            else:
                st.error("❌ This job description has significant bias — major revision needed!")

            st.divider()

            # Show found biases
            if found_biases:
                st.subheader("⚠️ Bias Found:")
                for bias_type, data in found_biases.items():
                    with st.expander(f"{data['color']} {bias_type} — Found: {', '.join(data['words'])}"):
                        st.write(f"**Biased words found:** {', '.join(data['words'])}")
                        st.write(f"**💡 Suggestion:** {data['suggestion']}")
            else:
                st.success("🎉 No bias detected! This is a fair and inclusive job description!")

            # Show clean categories
            st.subheader("✅ Clean Categories:")
            for bias_type in bias_dict:
                if bias_type not in found_biases:
                    st.success(f"✅ {bias_type} — No bias detected!")

        else:
            st.warning("⚠️ Please paste a job description first!")
