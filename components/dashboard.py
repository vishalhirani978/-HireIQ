# components/dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.helpers import extract_skills, get_match_score

def show_dashboard():
    st.markdown("""
    <div style='padding-bottom: 2rem;'>
        <div style='display: flex; align-items: center; gap: 16px; margin-bottom: 0.75rem;'>
            <div style='
                width: 48px;
                height: 48px;
                background: linear-gradient(135deg, rgba(46,134,171,0.2) 0%, rgba(46,134,171,0.1) 100%);
                border: 1px solid rgba(46,134,171,0.3);
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
            '>
                <span style='color: #2E86AB; font-size: 1.4rem;'>○</span>
            </div>
            <div>
                <h1 style='font-size: 2rem; font-weight: 700; margin: 0; letter-spacing: -0.5px;'>Candidates Dashboard</h1>
                <p style='color: #8B949E; font-size: 0.95rem; margin: 4px 0 0;'>Compare multiple candidates and make data-driven hiring decisions</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='
        background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
        border: 1px solid #30363D;
        border-radius: 14px;
        padding: 1.75rem;
        margin-bottom: 1.75rem;
    '>
        <div style='display: flex; align-items: center; gap: 14px; margin-bottom: 1.25rem;'>
            <div style='
                width: 40px;
                height: 40px;
                background: rgba(46, 134, 171, 0.15);
                border: 1px solid rgba(46, 134, 171, 0.2);
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
            '>
                <span style='color: #2E86AB;'>◆</span>
            </div>
            <div>
                <h3 style='margin: 0; color: #FFFFFF; font-size: 1.15rem; font-weight: 600;'>Job Description</h3>
                <p style='margin: 2px 0 0; color: #6E7681; font-size: 0.8rem;'>Enter the role requirements for comparison</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    job_desc_dash = st.text_area(
        "Paste job description here:",
        height=150,
        placeholder="e.g. We need a Python developer with ML experience...",
        label_visibility="collapsed"
    )
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
            border: 1px solid #30363D;
            border-radius: 14px;
            padding: 1.25rem;
            margin-bottom: 1rem;
        '>
            <p style='color: #8B949E; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 0.5rem 0;'>Candidates</p>
        </div>
        """, unsafe_allow_html=True)
        num_candidates = st.select_slider(
            "Number of Candidates",
            options=[2, 3, 4, 5],
            value=3
        )
    
    st.markdown("<hr style='margin: 1.5rem 0;'>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='padding: 0.5rem 0 1.5rem;'>
        <h3 style='color: #FFFFFF; margin-bottom: 1.25rem; font-weight: 600; font-size: 1.1rem;'>Candidate Information</h3>
    </div>
    """, unsafe_allow_html=True)
    
    candidates = []
    for i in range(num_candidates):
        with st.expander(f"Candidate {i+1}"):
            name = st.text_input(f"Name:", key=f"name_{i}")
            cv = st.text_area(
                "Paste CV:",
                height=150,
                key=f"cv_{i}",
                placeholder="Paste candidate CV here...",
                label_visibility="collapsed"
            )
            candidates.append({"name": name, "cv": cv})
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    col_center = st.columns([1, 2, 1])
    with col_center[1]:
        if st.button("Compare All Candidates", use_container_width=True):
            if job_desc_dash and all(c["cv"] and c["name"] for c in candidates):
                with st.spinner("Analyzing all candidates..."):
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
                            verdict = "HIRE"
                            verdict_color = "#00D4AA"
                        elif percentage >= 40:
                            verdict = "MAYBE"
                            verdict_color = "#FFA500"
                        else:
                            verdict = "REJECT"
                            verdict_color = "#FF4B4B"

                        results.append({
                            "name": candidate["name"],
                            "score": percentage,
                            "matched": len(matched),
                            "missing": len(missing),
                            "verdict": verdict,
                            "verdict_color": verdict_color
                        })

                results = sorted(
                    results, key=lambda x: x["score"], reverse=True
                )

                st.markdown("<hr style='margin: 2.5rem 0;'>", unsafe_allow_html=True)
                
                st.markdown("""
                <div style='padding-bottom: 1.5rem;'>
                    <div style='display: flex; align-items: center; gap: 14px;'>
                        <div style='
                            width: 40px;
                            height: 40px;
                            background: rgba(0, 212, 170, 0.15);
                            border: 1px solid rgba(0, 212, 170, 0.2);
                            border-radius: 10px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                        '>
                            <span style='color: #00D4AA; font-size: 1.1rem;'>◆</span>
                        </div>
                        <div>
                            <h2 style='font-size: 1.5rem; font-weight: 700; margin: 0;'>Candidate Rankings</h2>
                            <p style='color: #8B949E; font-size: 0.85rem; margin: 4px 0 0;'>Sorted by match score</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                df = pd.DataFrame([{
                    "Rank": i+1,
                    "Name": r["name"],
                    "Match Score": f"{r['score']}%",
                    "Matched": r["matched"],
                    "Missing": r["missing"],
                    "Verdict": r["verdict"]
                } for i, r in enumerate(results)])

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

                st.markdown("""
                <div style='padding: 2rem 0 1.5rem;'>
                    <h3 style='font-size: 1.2rem; font-weight: 600; color: #FFFFFF; margin-bottom: 1.5rem;'>Score Comparison</h3>
                </div>
                """, unsafe_allow_html=True)
                
                fig, ax = plt.subplots(figsize=(12, 6))
                fig.patch.set_facecolor('#161B22')
                ax.set_facecolor('#161B22')
                
                colors = [
                    "#00D4AA" if r["score"] >= 70
                    else "#FFA500" if r["score"] >= 40
                    else "#FF4B4B"
                    for r in results
                ]

                bars = ax.bar(
                    [r["name"] for r in results],
                    [r["score"] for r in results],
                    color=colors,
                    edgecolor='none',
                    linewidth=0,
                    width=0.6
                )

                for bar, r in zip(bars, results):
                    height = bar.get_height()
                    ax.text(
                        bar.get_x() + bar.get_width()/2,
                        height + 2,
                        f"{r['score']}%",
                        ha="center",
                        fontweight="bold",
                        color='#FFFFFF',
                        fontsize=13
                    )

                ax.set_ylabel("Match Score (%)", color='#8B949E', fontsize=11)
                ax.set_title("Candidate Comparison", color='#FFFFFF', fontsize=14, fontweight='bold', pad=15)
                ax.set_ylim(0, 120)
                ax.tick_params(axis='x', colors='#FFFFFF', labelsize=11)
                ax.tick_params(axis='y', colors='#8B949E')
                ax.spines['bottom'].set_color('#30363D')
                ax.spines['left'].set_color('#30363D')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                
                ax.axhline(
                    y=70, color="#00D4AA",
                    linestyle="--", alpha=0.5,
                    label="Hire threshold (70%)"
                )
                ax.axhline(
                    y=40, color="#FFA500",
                    linestyle="--", alpha=0.5,
                    label="Maybe threshold (40%)"
                )
                ax.legend(loc='upper right', framealpha=0.2, labelcolor='#8B949E')
                
                plt.tight_layout()
                st.pyplot(fig)

                st.markdown("<hr style='margin: 2.5rem 0;'>", unsafe_allow_html=True)
                
                top = results[0]
                
                st.markdown(f"""
                <div style='padding-bottom: 1.5rem;'>
                    <div style='display: flex; align-items: center; gap: 12px;'>
                        <div style='
                            width: 40px;
                            height: 40px;
                            background: linear-gradient(135deg, #FFA500 0%, #FF8C00 100%);
                            border-radius: 10px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            font-size: 1.2rem;
                        '>
                            <span style='color: white;'>★</span>
                        </div>
                        <h2 style='font-size: 1.5rem; font-weight: 700; margin: 0;'>Top Candidate</h2>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Best Candidate", top["name"])
                with col2:
                    st.metric("Match Score", f"{top['score']}%")
                with col3:
                    st.metric("Skills Matched", top["matched"])

                st.markdown(f"""
                <div style='
                    background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
                    border: 1px solid #30363D;
                    border-radius: 14px;
                    padding: 1.75rem;
                    margin-top: 1.5rem;
                '>
                    <div style='
                        display: inline-block;
                        background: {top['verdict_color']}20;
                        border: 1px solid {top['verdict_color']}40;
                        border-radius: 8px;
                        padding: 0.5rem 1rem;
                        margin-bottom: 1rem;
                    '>
                        <span style='color: {top['verdict_color']}; font-weight: 700; font-size: 1rem;'>{top['verdict']}</span>
                    </div>
                    <p style='color: #8B949E; margin: 0; line-height: 1.7; font-size: 1rem;'>
                        <strong style='color: #FFFFFF;'>{top['name']}</strong>
                        is the top candidate with a match score of 
                        <strong style='color: {top['verdict_color']};'>{top['score']}%</strong>
                        — {top['matched']} skills matched and {top['missing']} skills missing.
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
            else:
                st.markdown("""
                <div style='
                    background: rgba(255, 165, 0, 0.1);
                    border: 1px solid rgba(255, 165, 0, 0.25);
                    border-radius: 12px;
                    padding: 1.25rem 1.5rem;
                '>
                    <div style='display: flex; align-items: center; gap: 12px;'>
                        <span style='color: #FFA500; font-size: 1.2rem;'>!</span>
                        <span style='color: #FFA500; font-weight: 500;'>Please fill Job Description and ALL candidate names + CVs</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
