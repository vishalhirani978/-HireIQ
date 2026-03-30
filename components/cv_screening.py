# components/cv_screening.py
import streamlit as st
from huggingface_hub import InferenceClient
from utils.helpers import extract_skills, get_match_score, get_recommendation
import os

def show_cv_screening():
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
                <span style='color: #2E86AB; font-size: 1.4rem;'>◆</span>
            </div>
            <div>
                <h1 style='font-size: 2rem; font-weight: 700; margin: 0; letter-spacing: -0.5px;'>CV Screening</h1>
                <p style='color: #8B949E; font-size: 0.95rem; margin: 4px 0 0;'>Analyze candidate qualifications against job requirements</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    client = InferenceClient(token=os.getenv("HUGGINGFACE_TOKEN"))
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
            border: 1px solid #30363D; 
            border-radius: 14px;
            padding: 1.5rem;
            margin-bottom: 0.75rem;
        '>
            <div style='display: flex; align-items: center; gap: 12px;'>
                <div style='
                    width: 36px;
                    height: 36px;
                    background: rgba(46, 134, 171, 0.15);
                    border: 1px solid rgba(46, 134, 171, 0.2);
                    border-radius: 8px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                '>
                    <span style='color: #2E86AB; font-size: 1rem;'>◆</span>
                </div>
                <div>
                    <h3 style='margin: 0; color: #FFFFFF; font-size: 1.05rem; font-weight: 600;'>Job Description</h3>
                    <p style='margin: 2px 0 0; color: #6E7681; font-size: 0.8rem;'>Enter the role requirements</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        job_desc = st.text_area(
            "Paste job description here:",
            height=320,
            placeholder="e.g. We need a Python developer with 2 years experience in ML...",
            label_visibility="collapsed"
        )
    
    with col2:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
            border: 1px solid #30363D; 
            border-radius: 14px;
            padding: 1.5rem;
            margin-bottom: 0.75rem;
        '>
            <div style='display: flex; align-items: center; gap: 12px;'>
                <div style='
                    width: 36px;
                    height: 36px;
                    background: rgba(0, 212, 170, 0.15);
                    border: 1px solid rgba(0, 212, 170, 0.2);
                    border-radius: 8px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                '>
                    <span style='color: #00D4AA; font-size: 1rem;'>○</span>
                </div>
                <div>
                    <h3 style='margin: 0; color: #FFFFFF; font-size: 1.05rem; font-weight: 600;'>Candidate CV</h3>
                    <p style='margin: 2px 0 0; color: #6E7681; font-size: 0.8rem;'>Enter the candidate's resume</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        cv_text = st.text_area(
            "Paste candidate CV here:",
            height=320,
            placeholder="e.g. John Doe, 3 years Python experience, worked on ML projects...",
            label_visibility="collapsed"
        )
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    col_center = st.columns([1, 2, 1])
    with col_center[1]:
        if st.button("Analyze Candidate", use_container_width=True):
            if job_desc and cv_text:
                with st.spinner("AI is analyzing the CV..."):
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

                st.markdown("<hr style='margin: 2.5rem 0;'>", unsafe_allow_html=True)
                
                st.markdown("""
                <div style='padding-bottom: 1.5rem;'>
                    <div style='display: flex; align-items: center; gap: 12px;'>
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
                            <h2 style='font-size: 1.5rem; font-weight: 700; margin: 0;'>Screening Results</h2>
                            <p style='color: #8B949E; font-size: 0.85rem; margin: 4px 0 0;'>AI-powered candidate analysis</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if percentage >= 70:
                    score_color = "#00D4AA"
                    score_label = "Strong Match"
                    score_bg = "rgba(0, 212, 170, 0.08)"
                    score_border = "rgba(0, 212, 170, 0.2)"
                elif percentage >= 40:
                    score_color = "#FFA500"
                    score_label = "Partial Match"
                    score_bg = "rgba(255, 165, 0, 0.08)"
                    score_border = "rgba(255, 165, 0, 0.2)"
                else:
                    score_color = "#FF4B4B"
                    score_label = "Weak Match"
                    score_bg = "rgba(255, 75, 75, 0.08)"
                    score_border = "rgba(255, 75, 75, 0.2)"
                
                st.markdown(f"""
                <div style='
                    background: {score_bg};
                    border: 1px solid {score_border};
                    border-radius: 16px;
                    padding: 2rem;
                    text-align: center;
                    margin-bottom: 1.5rem;
                    position: relative;
                    overflow: hidden;
                '>
                    <div style='
                        position: absolute;
                        top: -50%;
                        left: 50%;
                        transform: translateX(-50%);
                        width: 300px;
                        height: 300px;
                        background: radial-gradient(circle, {score_color}15 0%, transparent 60%);
                        pointer-events: none;
                    '></div>
                    <p style='color: #8B949E; font-size: 0.9rem; margin: 0 0 0.5rem 0; text-transform: uppercase; letter-spacing: 1px;'>Match Score</p>
                    <h1 style='
                        font-size: 5rem; 
                        font-weight: 800; 
                        margin: 0;
                        color: {score_color};
                        letter-spacing: -3px;
                        line-height: 1;
                    '>{percentage}%</h1>
                    <div style='
                        display: inline-block;
                        background: {score_color}20;
                        border: 1px solid {score_color}40;
                        border-radius: 20px;
                        padding: 0.5rem 1.25rem;
                        margin-top: 1rem;
                    '>
                        <span style='color: {score_color}; font-size: 0.95rem; font-weight: 600;'>{score_label}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.progress(score)
                
                st.markdown(f"""
                <div style='
                    background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
                    border: 1px solid #30363D;
                    border-radius: 14px;
                    padding: 1.75rem;
                    margin: 2rem 0;
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
                        <h3 style='margin: 0; color: #FFFFFF; font-size: 1.15rem; font-weight: 600;'>Hiring Recommendation</h3>
                    </div>
                    <p style='color: #8B949E; line-height: 1.7; margin: 0; font-size: 0.95rem;'>{recommendation}</p>
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("""
                    <div style='
                        background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
                        border: 1px solid #30363D;
                        border-radius: 14px;
                        padding: 1.5rem;
                        height: 100%;
                    '>
                        <div style='display: flex; align-items: center; gap: 12px; margin-bottom: 1.25rem;'>
                            <span style='color: #00D4AA; font-size: 1.2rem;'>●</span>
                            <h4 style='margin: 0; color: #FFFFFF; font-size: 1rem; font-weight: 600;'>Matched Skills</h4>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    if matched_skills:
                        for skill in matched_skills:
                            st.markdown(f"""
                            <span style='
                                display: inline-block;
                                background: rgba(0, 212, 170, 0.1);
                                border: 1px solid rgba(0, 212, 170, 0.25);
                                border-radius: 8px;
                                padding: 0.6rem 1.1rem;
                                margin: 0.35rem;
                                color: #00D4AA;
                                font-size: 0.9rem;
                                font-weight: 500;
                            '>{skill}</span>
                            """, unsafe_allow_html=True)
                    else:
                        st.markdown("<p style='color: #8B949E; font-size: 0.9rem;'>No matched skills found.</p>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                
                with col2:
                    st.markdown("""
                    <div style='
                        background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
                        border: 1px solid #30363D;
                        border-radius: 14px;
                        padding: 1.5rem;
                        height: 100%;
                    '>
                        <div style='display: flex; align-items: center; gap: 12px; margin-bottom: 1.25rem;'>
                            <span style='color: #FF4B4B; font-size: 1.2rem;'>●</span>
                            <h4 style='margin: 0; color: #FFFFFF; font-size: 1rem; font-weight: 600;'>Missing Skills</h4>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    if missing_skills:
                        for skill in missing_skills:
                            st.markdown(f"""
                            <span style='
                                display: inline-block;
                                background: rgba(255, 75, 75, 0.1);
                                border: 1px solid rgba(255, 75, 75, 0.25);
                                border-radius: 8px;
                                padding: 0.6rem 1.1rem;
                                margin: 0.35rem;
                                color: #FF4B4B;
                                font-size: 0.9rem;
                                font-weight: 500;
                            '>{skill}</span>
                            """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div style='
                            background: rgba(0, 212, 170, 0.1);
                            border: 1px solid rgba(0, 212, 170, 0.2);
                            border-radius: 8px;
                            padding: 1rem;
                            text-align: center;
                        '>
                            <span style='color: #00D4AA; font-size: 0.9rem; font-weight: 500;'>No missing skills — great candidate!</span>
                        </div>
                        """, unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                
                st.markdown(f"""
                <div style='
                    background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
                    border: 1px solid #30363D;
                    border-radius: 14px;
                    padding: 1.75rem;
                    margin-top: 2rem;
                '>
                    <div style='display: flex; align-items: center; gap: 14px; margin-bottom: 1.25rem;'>
                        <div style='
                            width: 44px;
                            height: 44px;
                            background: linear-gradient(135deg, #1E3A5F 0%, #2E86AB 100%);
                            border-radius: 10px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                        '>
                            <span style='color: white; font-weight: 700; font-size: 0.9rem;'>AI</span>
                        </div>
                        <div>
                            <h3 style='margin: 0; color: #FFFFFF; font-size: 1.15rem; font-weight: 600;'>AI Analysis</h3>
                            <p style='margin: 2px 0 0; color: #6E7681; font-size: 0.8rem;'>Detailed assessment</p>
                        </div>
                    </div>
                    <p style='color: #8B949E; line-height: 1.75; margin: 0; font-size: 0.95rem;'>{explanation}</p>
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
                        <span style='color: #FFA500; font-weight: 500;'>Please paste both Job Description and CV to analyze.</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
