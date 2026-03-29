# components/dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.helpers import extract_skills, get_match_score

def show_dashboard():
    st.title("📊 Candidates Dashboard")
    st.write("Compare multiple candidates visually and make better hiring decisions!")

    job_desc_dash = st.text_area(
        "📋 Paste Job Description:",
        height=150,
        placeholder="e.g. We need a Python developer with ML experience..."
    )

    num_candidates = st.slider("How many candidates?", 2, 5, 3)

    candidates = []
    for i in range(num_candidates):
        with st.expander(f"👤 Candidate {i+1}"):
            name = st.text_input(f"Name:", key=f"name_{i}")
            cv = st.text_area(
                "Paste CV:",
                height=150,
                key=f"cv_{i}",
                placeholder="Paste candidate CV here..."
            )
            candidates.append({"name": name, "cv": cv})

    if st.button("📊 Compare All Candidates!", use_container_width=True):
        if job_desc_dash and all(c["cv"] and c["name"] for c in candidates):
            with st.spinner("Analyzing all candidates... 🤔"):
                results = []
                for candidate in candidates:
                    score, percentage = get_match_score(
                        job_desc_dash, candidate["cv"]
                    )
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
                        "verdict": verdict
                    })

            # Sort by score
            results = sorted(
                results, key=lambda x: x["score"], reverse=True
            )

            st.divider()
            st.subheader("🏆 Candidate Rankings")

            # Rankings table
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

            colors = [
                "green" if r["score"] >= 70
                else "orange" if r["score"] >= 40
                else "red"
                for r in results
            ]

            bars = ax.bar(
                [r["name"] for r in results],
                [r["score"] for r in results],
                color=colors
            )

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
            ax.axhline(
                y=70, color="green",
                linestyle="--", alpha=0.5,
                label="Hire threshold (70%)"
            )
            ax.axhline(
                y=40, color="orange",
                linestyle="--", alpha=0.5,
                label="Maybe threshold (40%)"
            )
            ax.legend()
            st.pyplot(fig)

            # Top candidate
            st.divider()
            top = results[0]
            st.subheader("🥇 Top Candidate Details")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("🏆 Best Candidate", top["name"])
            with col2:
                st.metric("📊 Match Score", f"{top['score']}%")
            with col3:
                st.metric("✅ Skills Matched", top["matched"])

            if top["score"] >= 70:
                st.success(
                    f"**Recommendation: {top['verdict']} {top['name']}**"
                    f" — highest match at {top['score']}%!"
                )
            elif top["score"] >= 40:
                st.warning(
                    f"**Recommendation: {top['verdict']} {top['name']}**"
                    f" — consider for interview at {top['score']}%!"
                )
            else:
                st.error(
                    f"**Recommendation: {top['verdict']} {top['name']}**"
                    f" — no strong candidates found!"
                )

        else:
            st.warning(
                "⚠️ Please fill Job Description and ALL candidate names + CVs!"
            )