# components/interview.py
import streamlit as st
from utils.helpers import extract_skills
from backend.question_gen import generate_questions

def show_interview():
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
                <span style='color: #2E86AB; font-size: 1.4rem;'>▶</span>
            </div>
            <div>
                <h1 style='font-size: 2rem; font-weight: 700; margin: 0; letter-spacing: -0.5px;'>Interview Questions Generator</h1>
                <p style='color: #8B949E; font-size: 0.95rem; margin: 4px 0 0;'>Generate smart interview questions based on job requirements and candidate gaps</p>
            </div>
        </div>
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
                    <p style='margin: 2px 0 0; color: #6E7681; font-size: 0.8rem;'>Enter role requirements</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        jd = st.text_area(
            "Paste job description here:",
            height=280,
            placeholder="e.g. We need a Python developer with ML experience...",
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
                    <p style='margin: 2px 0 0; color: #6E7681; font-size: 0.8rem;'>Enter candidate's resume</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        cv = st.text_area(
            "Paste candidate CV here:",
            height=280,
            placeholder="e.g. Ahmed Khan, Python developer, 2 years experience...",
            label_visibility="collapsed"
        )
    
    st.markdown("<hr style='margin: 1.5rem 0;'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
            border: 1px solid #30363D; 
            border-radius: 14px;
            padding: 1.25rem;
        '>
            <p style='color: #8B949E; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 0.5rem 0;'>Difficulty Level</p>
        </div>
        """, unsafe_allow_html=True)
        difficulty = st.selectbox(
            "Question Difficulty:",
            ["Easy", "Medium", "Hard"],
            index=1,
            label_visibility="collapsed"
        )
    with col2:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
            border: 1px solid #30363D; 
            border-radius: 14px;
            padding: 1.25rem;
        '>
            <p style='color: #8B949E; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 0.5rem 0;'>Number of Questions</p>
        </div>
        """, unsafe_allow_html=True)
        num_questions = st.slider(
            "Number of questions:",
            3, 10, 5,
            label_visibility="collapsed"
        )
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    col_center = st.columns([1, 2, 1])
    with col_center[1]:
        if st.button("Generate Interview Questions", use_container_width=True):
            if jd and cv:
                with st.spinner("AI is generating questions..."):
                    job_skills = extract_skills(jd)
                    cv_skills = extract_skills(cv)
                    missing_skills = [s for s in job_skills if s not in cv_skills]
                    matched_skills = [s for s in job_skills if s in cv_skills]
                    questions = generate_questions(matched_skills, missing_skills, difficulty, num_questions)

                st.markdown("<hr style='margin: 2.5rem 0;'>", unsafe_allow_html=True)
                
                st.markdown(f"""
                <div style='padding-bottom: 2rem;'>
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
                            <h2 style='font-size: 1.5rem; font-weight: 700; margin: 0;'>Generated Questions</h2>
                            <p style='color: #8B949E; font-size: 0.85rem; margin: 4px 0 0;'>Total: {num_questions} questions | Difficulty: {difficulty}</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if questions["gap"]:
                    st.markdown(f"""
                    <div style='
                        background: rgba(255, 75, 75, 0.06);
                        border: 1px solid rgba(255, 75, 75, 0.2);
                        border-radius: 14px;
                        padding: 1.5rem;
                        margin-bottom: 1.5rem;
                    '>
                        <div style='display: flex; align-items: center; gap: 12px; margin-bottom: 1.25rem;'>
                            <span style='color: #FF4B4B; font-size: 1.3rem;'>●</span>
                            <h3 style='margin: 0; color: #FFFFFF; font-size: 1.15rem; font-weight: 600;'>Skill Gap Questions</h3>
                            <span style='
                                background: rgba(255, 75, 75, 0.15);
                                color: #FF4B4B;
                                padding: 0.35rem 1rem;
                                border-radius: 20px;
                                font-size: 0.8rem;
                                font-weight: 600;
                                margin-left: auto;
                            '>{questions['gap_count']}</span>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    for i, q in enumerate(questions["gap"], 1):
                        st.markdown(f"""
                        <div style='
                            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
                            border: 1px solid #30363D;
                            border-radius: 10px;
                            padding: 1.25rem 1.5rem;
                            margin: 0.6rem 0;
                        '>
                            <span style='color: #FF4B4B; font-weight: 700; margin-right: 0.75rem;'>Q{i}.</span>
                            <span style='color: #E6EDF3; font-size: 0.95rem;'>{q}</span>
                        </div>
                        """, unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)

                if questions["verify"]:
                    st.markdown(f"""
                    <div style='
                        background: rgba(0, 212, 170, 0.06);
                        border: 1px solid rgba(0, 212, 170, 0.2);
                        border-radius: 14px;
                        padding: 1.5rem;
                        margin-bottom: 1.5rem;
                    '>
                        <div style='display: flex; align-items: center; gap: 12px; margin-bottom: 1.25rem;'>
                            <span style='color: #00D4AA; font-size: 1.3rem;'>●</span>
                            <h3 style='margin: 0; color: #FFFFFF; font-size: 1.15rem; font-weight: 600;'>Skill Verification Questions</h3>
                            <span style='
                                background: rgba(0, 212, 170, 0.15);
                                color: #00D4AA;
                                padding: 0.35rem 1rem;
                                border-radius: 20px;
                                font-size: 0.8rem;
                                font-weight: 600;
                                margin-left: auto;
                            '>{questions['verify_count']}</span>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    for i, q in enumerate(questions["verify"], 1):
                        st.markdown(f"""
                        <div style='
                            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
                            border: 1px solid #30363D;
                            border-radius: 10px;
                            padding: 1.25rem 1.5rem;
                            margin: 0.6rem 0;
                        '>
                            <span style='color: #00D4AA; font-weight: 700; margin-right: 0.75rem;'>Q{i}.</span>
                            <span style='color: #E6EDF3; font-size: 0.95rem;'>{q}</span>
                        </div>
                        """, unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)

                if questions["difficulty"]:
                    difficulty_color = {
                        "Easy": "#00D4AA",
                        "Medium": "#FFA500",
                        "Hard": "#FF4B4B"
                    }.get(difficulty, "#8B949E")
                    
                    st.markdown(f"""
                    <div style='
                        background: rgba(139, 148, 158, 0.06);
                        border: 1px solid rgba(139, 148, 158, 0.2);
                        border-radius: 14px;
                        padding: 1.5rem;
                    '>
                        <div style='display: flex; align-items: center; gap: 12px; margin-bottom: 1.25rem;'>
                            <span style='color: {difficulty_color}; font-size: 1.3rem;'>●</span>
                            <h3 style='margin: 0; color: #FFFFFF; font-size: 1.15rem; font-weight: 600;'>{difficulty} Level Questions</h3>
                            <span style='
                                background: {difficulty_color}15;
                                color: {difficulty_color};
                                padding: 0.35rem 1rem;
                                border-radius: 20px;
                                font-size: 0.8rem;
                                font-weight: 600;
                                margin-left: auto;
                            '>{questions['difficulty_count']}</span>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    for i, q in enumerate(questions["difficulty"], 1):
                        st.markdown(f"""
                        <div style='
                            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
                            border: 1px solid #30363D;
                            border-radius: 10px;
                            padding: 1.25rem 1.5rem;
                            margin: 0.6rem 0;
                        '>
                            <span style='color: {difficulty_color}; font-weight: 700; margin-right: 0.75rem;'>Q{i}.</span>
                            <span style='color: #E6EDF3; font-size: 0.95rem;'>{q}</span>
                        </div>
                        """, unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
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
                        <span style='color: #FFA500; font-weight: 500;'>Please paste both Job Description and CV</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
