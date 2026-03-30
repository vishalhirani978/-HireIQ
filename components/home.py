# components/home.py
import streamlit as st

def show_home():
    # Hero Section
    st.markdown("""
    <div style='
        text-align: center; 
        padding: 2rem 0 3rem;
        position: relative;
    '>
        <div style='
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 300px;
            height: 300px;
            background: radial-gradient(circle, rgba(0,212,170,0.08) 0%, transparent 70%);
            pointer-events: none;
        '></div>
        <div style='
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #1E3A5F 0%, #2E86AB 100%);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 2rem;
            box-shadow: 0 8px 32px rgba(46, 134, 171, 0.4), 0 0 60px rgba(46, 134, 171, 0.2);
        '>
            <div style='
                position: relative;
                width: 40px;
                height: 40px;
            '>
                <div style='
                    position: absolute;
                    width: 36px;
                    height: 36px;
                    border: 3px solid rgba(255,255,255,0.9);
                    border-radius: 50%;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                '></div>
                <div style='
                    position: absolute;
                    width: 12px;
                    height: 12px;
                    background: #00D4AA;
                    border-radius: 50%;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    box-shadow: 0 0 15px #00D4AA;
                '></div>
            </div>
        </div>
        <h1 style='
            font-size: 3.5rem; 
            font-weight: 800; 
            margin-bottom: 0.75rem;
            letter-spacing: -2px;
            position: relative;
        '>
            <span style='color: #FFFFFF;'>Hire</span><span style='color: #00D4AA;'>IQ</span>
        </h1>
        <p style='
            font-size: 1.4rem; 
            color: #8B949E; 
            margin-bottom: 1.25rem;
            font-weight: 400;
        '>AI-Powered Hiring Assistant</p>
        <p style='
            font-size: 1.05rem; 
            color: #6E7681;
            max-width: 650px;
            margin: 0 auto;
            line-height: 1.7;
        '>Screen CVs faster, fairer and smarter — powered by advanced AI technology designed for Pakistani startups and SMEs</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Time Saved", "80%", "vs manual screening")
    with col2:
        st.metric("Accuracy", "95%", "skill matching")
    with col3:
        st.metric("Bias Checks", "5 Types", "detected automatically")
    with col4:
        st.metric("Cost", "FREE", "no subscription needed")
    
    st.markdown("<hr style='margin: 3rem 0 2.5rem;'>", unsafe_allow_html=True)
    
    # Features Section
    st.markdown("""
    <div style='padding: 0 0 2rem;'>
        <div style='text-align: center; margin-bottom: 2.5rem;'>
            <h2 style='font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;'>Platform Capabilities</h2>
            <p style='color: #8B949E; font-size: 1rem;'>Everything you need for smarter hiring decisions</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
            border: 1px solid #30363D; 
            border-radius: 16px; 
            padding: 2rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        '>
            <div style='
                position: absolute;
                top: 0;
                right: 0;
                width: 150px;
                height: 150px;
                background: radial-gradient(circle, rgba(0,212,170,0.06) 0%, transparent 70%);
                pointer-events: none;
            '></div>
            <div style='display: flex; align-items: center; gap: 16px; margin-bottom: 1.5rem;'>
                <div style='
                    width: 52px; 
                    height: 52px; 
                    background: rgba(0, 212, 170, 0.12);
                    border: 1px solid rgba(0, 212, 170, 0.2);
                    border-radius: 12px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                '>
                    <span style='color: #00D4AA; font-size: 1.4rem;'>◆</span>
                </div>
                <div>
                    <h3 style='margin: 0; font-size: 1.3rem; color: #FFFFFF; font-weight: 600;'>CV Screening</h3>
                    <p style='margin: 4px 0 0; color: #6E7681; font-size: 0.85rem;'>AI-powered candidate analysis</p>
                </div>
            </div>
            <ul style='color: #8B949E; line-height: 2.1; margin: 0; padding-left: 1.5rem; font-size: 0.95rem;'>
                <li>Paste CV + Job Description</li>
                <li>AI scores candidate match</li>
                <li>Shows matched & missing skills</li>
                <li>Gives Hire/Maybe/Reject verdict</li>
                <li>Full analysis with explanations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
            border: 1px solid #30363D; 
            border-radius: 16px; 
            padding: 2rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        '>
            <div style='
                position: absolute;
                top: 0;
                right: 0;
                width: 150px;
                height: 150px;
                background: radial-gradient(circle, rgba(46,134,171,0.06) 0%, transparent 70%);
                pointer-events: none;
            '></div>
            <div style='display: flex; align-items: center; gap: 16px; margin-bottom: 1.5rem;'>
                <div style='
                    width: 52px; 
                    height: 52px; 
                    background: rgba(46, 134, 171, 0.12);
                    border: 1px solid rgba(46, 134, 171, 0.2);
                    border-radius: 12px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                '>
                    <span style='color: #2E86AB; font-size: 1.4rem;'>○</span>
                </div>
                <div>
                    <h3 style='margin: 0; font-size: 1.3rem; color: #FFFFFF; font-weight: 600;'>Candidate Dashboard</h3>
                    <p style='margin: 4px 0 0; color: #6E7681; font-size: 0.85rem;'>Compare multiple candidates</p>
                </div>
            </div>
            <ul style='color: #8B949E; line-height: 2.1; margin: 0; padding-left: 1.5rem; font-size: 0.95rem;'>
                <li>Compare up to 5 candidates</li>
                <li>Visual bar chart comparison</li>
                <li>Automatic ranking by score</li>
                <li>Side by side skill analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
            border: 1px solid #30363D; 
            border-radius: 16px; 
            padding: 2rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        '>
            <div style='
                position: absolute;
                top: 0;
                right: 0;
                width: 150px;
                height: 150px;
                background: radial-gradient(circle, rgba(46,134,171,0.06) 0%, transparent 70%);
                pointer-events: none;
            '></div>
            <div style='display: flex; align-items: center; gap: 16px; margin-bottom: 1.5rem;'>
                <div style='
                    width: 52px; 
                    height: 52px; 
                    background: rgba(46, 134, 171, 0.12);
                    border: 1px solid rgba(46, 134, 171, 0.2);
                    border-radius: 12px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                '>
                    <span style='color: #2E86AB; font-size: 1.4rem;'>▶</span>
                </div>
                <div>
                    <h3 style='margin: 0; font-size: 1.3rem; color: #FFFFFF; font-weight: 600;'>Interview Questions</h3>
                    <p style='margin: 4px 0 0; color: #6E7681; font-size: 0.85rem;'>Smart question generation</p>
                </div>
            </div>
            <ul style='color: #8B949E; line-height: 2.1; margin: 0; padding-left: 1.5rem; font-size: 0.95rem;'>
                <li>Auto-generated from CV gaps</li>
                <li>3 difficulty levels</li>
                <li>Skill verification questions</li>
                <li>Behavioral questions included</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
            border: 1px solid #30363D; 
            border-radius: 16px; 
            padding: 2rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        '>
            <div style='
                position: absolute;
                top: 0;
                right: 0;
                width: 150px;
                height: 150px;
                background: radial-gradient(circle, rgba(255,165,0,0.06) 0%, transparent 70%);
                pointer-events: none;
            '></div>
            <div style='display: flex; align-items: center; gap: 16px; margin-bottom: 1.5rem;'>
                <div style='
                    width: 52px; 
                    height: 52px; 
                    background: rgba(255, 165, 0, 0.12);
                    border: 1px solid rgba(255, 165, 0, 0.2);
                    border-radius: 12px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                '>
                    <span style='color: #FFA500; font-size: 1.4rem;'>◇</span>
                </div>
                <div>
                    <h3 style='margin: 0; font-size: 1.3rem; color: #FFFFFF; font-weight: 600;'>Bias Detector</h3>
                    <p style='margin: 4px 0 0; color: #6E7681; font-size: 0.85rem;'>Ensure fair hiring practices</p>
                </div>
            </div>
            <ul style='color: #8B949E; line-height: 2.1; margin: 0; padding-left: 1.5rem; font-size: 0.95rem;'>
                <li>Detects 5 types of bias</li>
                <li>Age, Gender, Origin detection</li>
                <li>Fairness score calculated</li>
                <li>Improvement suggestions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr style='margin: 3rem 0 2.5rem;'>", unsafe_allow_html=True)
    
    # How it works
    st.markdown("""
    <div style='padding: 0 0 2rem; text-align: center;'>
        <h2 style='font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;'>How It Works</h2>
        <p style='color: #8B949E; font-size: 1rem;'>Three simple steps to better hiring</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
            border: 1px solid #30363D; 
            border-radius: 16px; 
            padding: 2.5rem 2rem;
            text-align: center;
            height: 100%;
            position: relative;
        '>
            <div style='
                position: absolute;
                top: 1rem;
                right: 1rem;
                color: #30363D;
                font-size: 2rem;
                font-weight: 700;
            '>01</div>
            <div style='
                width: 70px; 
                height: 70px; 
                background: linear-gradient(135deg, #1E3A5F 0%, #2E86AB 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 1.5rem;
                box-shadow: 0 8px 24px rgba(46, 134, 171, 0.3);
            '>
                <span style='color: white; font-size: 1.6rem; font-weight: 600;'>1</span>
            </div>
            <h3 style='color: #FFFFFF; margin-bottom: 0.75rem; font-weight: 600;'>Input Data</h3>
            <p style='color: #8B949E; line-height: 1.7; margin: 0; font-size: 0.95rem;'>Paste your Job Description and Candidate CV into the system</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
            border: 1px solid #30363D; 
            border-radius: 16px; 
            padding: 2.5rem 2rem;
            text-align: center;
            height: 100%;
            position: relative;
        '>
            <div style='
                position: absolute;
                top: 1rem;
                right: 1rem;
                color: #30363D;
                font-size: 2rem;
                font-weight: 700;
            '>02</div>
            <div style='
                width: 70px; 
                height: 70px; 
                background: linear-gradient(135deg, #1E3A5F 0%, #2E86AB 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 1.5rem;
                box-shadow: 0 8px 24px rgba(46, 134, 171, 0.3);
            '>
                <span style='color: white; font-size: 1.6rem; font-weight: 600;'>2</span>
            </div>
            <h3 style='color: #FFFFFF; margin-bottom: 0.75rem; font-weight: 600;'>AI Analysis</h3>
            <p style='color: #8B949E; line-height: 1.7; margin: 0; font-size: 0.95rem;'>Our AI analyzes skills, scores the match, and detects potential bias</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
            border: 1px solid #30363D; 
            border-radius: 16px; 
            padding: 2.5rem 2rem;
            text-align: center;
            height: 100%;
            position: relative;
        '>
            <div style='
                position: absolute;
                top: 1rem;
                right: 1rem;
                color: #30363D;
                font-size: 2rem;
                font-weight: 700;
            '>03</div>
            <div style='
                width: 70px; 
                height: 70px; 
                background: linear-gradient(135deg, #00D4AA 0%, #00B894 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 1.5rem;
                box-shadow: 0 8px 24px rgba(0, 212, 170, 0.3);
            '>
                <span style='color: white; font-size: 1.6rem; font-weight: 600;'>3</span>
            </div>
            <h3 style='color: #FFFFFF; margin-bottom: 0.75rem; font-weight: 600;'>Get Results</h3>
            <p style='color: #8B949E; line-height: 1.7; margin: 0; font-size: 0.95rem;'>Receive instant Hire/Maybe/Reject recommendations with full explanations</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr style='margin: 3rem 0 2rem;'>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style='
        text-align: center; 
        padding: 2rem;
        background: linear-gradient(145deg, #161B22 0%, #0E1117 100%);
        border: 1px solid #30363D;
        border-radius: 16px;
    '>
        <div style='display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 1rem;'>
            <div style='width: 8px; height: 8px; background: #00D4AA; border-radius: 50%; box-shadow: 0 0 10px #00D4AA;'></div>
            <span style='color: #8B949E; font-size: 0.85rem;'>Built for Pakistani Businesses</span>
        </div>
        <p style='color: #6E7681; font-size: 0.9rem; margin-bottom: 0.5rem;'>
            Powered by AI & Hugging Face
        </p>
        <p style='color: #00D4AA; font-size: 1.1rem; font-weight: 600;'>
            HireIQ — Making hiring faster, fairer and smarter
        </p>
    </div>
    """, unsafe_allow_html=True)
