# components/bias_detector.py
import streamlit as st
from backend.bias_checker import detect_bias, BIAS_DICT

def show_bias_detector():
    st.markdown("""
    <div style='padding-bottom: 2rem;'>
        <div style='display: flex; align-items: center; gap: 16px; margin-bottom: 0.75rem;'>
            <div style='
                width: 48px;
                height: 48px;
                background: linear-gradient(135deg, rgba(255,165,0,0.2) 0%, rgba(255,165,0,0.1) 100%);
                border: 1px solid rgba(255,165,0,0.3);
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
            '>
                <span style='color: #FFA500; font-size: 1.4rem;'>◇</span>
            </div>
            <div>
                <h1 style='font-size: 2rem; font-weight: 700; margin: 0; letter-spacing: -0.5px;'>Bias Detector</h1>
                <p style='color: #8B949E; font-size: 0.95rem; margin: 4px 0 0;'>Detect biased language in job descriptions to ensure fair hiring</p>
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
                background: rgba(255, 165, 0, 0.15);
                border: 1px solid rgba(255, 165, 0, 0.2);
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
            '>
                <span style='color: #FFA500;'>◇</span>
            </div>
            <div>
                <h3 style='margin: 0; color: #FFFFFF; font-size: 1.15rem; font-weight: 600;'>Job Description Analysis</h3>
                <p style='margin: 2px 0 0; color: #6E7681; font-size: 0.8rem;'>Paste your job description below</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    job_desc_bias = st.text_area(
        "Paste job description to analyze:",
        height=280,
        placeholder="Paste your job description here...",
        label_visibility="collapsed"
    )
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    col_center = st.columns([1, 2, 1])
    with col_center[1]:
        if st.button("Detect Bias", use_container_width=True):
            if job_desc_bias:
                with st.spinner("Analyzing for bias..."):
                    found_biases, fairness_score, biased_count, clean_count = detect_bias(job_desc_bias)

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
                            <h2 style='font-size: 1.5rem; font-weight: 700; margin: 0;'>Analysis Results</h2>
                            <p style='color: #8B949E; font-size: 0.85rem; margin: 4px 0 0;'>Comprehensive bias detection report</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Fairness Score", f"{fairness_score}%")
                with col2:
                    st.metric("Bias Types Found", biased_count)
                with col3:
                    st.metric("Clean Categories", clean_count)
                
                if fairness_score >= 80:
                    progress_color = "#00D4AA"
                    progress_label = "This job description is largely bias-free"
                    progress_bg = "rgba(0,212,170,0.08)"
                    progress_border = "rgba(0,212,170,0.2)"
                elif fairness_score >= 60:
                    progress_color = "#FFA500"
                    progress_label = "This job description has some bias — review highlighted issues"
                    progress_bg = "rgba(255,165,0,0.08)"
                    progress_border = "rgba(255,165,0,0.2)"
                else:
                    progress_color = "#FF4B4B"
                    progress_label = "This job description has significant bias — major revision needed"
                    progress_bg = "rgba(255,75,75,0.08)"
                    progress_border = "rgba(255,75,75,0.2)"
                
                st.markdown(f"""
                <div style='
                    background: {progress_bg};
                    border: 1px solid {progress_border};
                    border-radius: 14px;
                    padding: 1.5rem;
                    margin: 2rem 0;
                '>
                    <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
                        <span style='color: #8B949E; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.5px;'>Bias-Free Progress</span>
                        <span style='color: {progress_color}; font-weight: 700; font-size: 1.1rem;'>{fairness_score}%</span>
                    </div>
                    <div style='
                        background: #30363D;
                        border-radius: 8px;
                        height: 14px;
                        overflow: hidden;
                    '>
                        <div style='
                            background: linear-gradient(90deg, {progress_color} 0%, {progress_color}CC 100%);
                            width: {fairness_score}%;
                            height: 100%;
                            border-radius: 8px;
                            transition: width 0.5s ease;
                            box-shadow: 0 0 15px {progress_color}50;
                        '></div>
                    </div>
                    <p style='color: {progress_color}; margin: 1.25rem 0 0 0; font-weight: 600; font-size: 0.95rem;'>{progress_label}</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("<hr style='margin: 2.5rem 0;'>", unsafe_allow_html=True)

                if found_biases:
                    st.markdown(f"""
                    <div style='padding-bottom: 1.5rem;'>
                        <div style='display: flex; align-items: center; gap: 12px;'>
                            <span style='color: #FF4B4B; font-size: 1.3rem;'>●</span>
                            <h3 style='font-size: 1.2rem; font-weight: 600; color: #FFFFFF; margin: 0;'>Bias Detected</h3>
                            <span style='
                                background: rgba(255, 75, 75, 0.15);
                                color: #FF4B4B;
                                padding: 0.35rem 1rem;
                                border-radius: 20px;
                                font-size: 0.8rem;
                                font-weight: 600;
                                margin-left: auto;
                            '>{len(found_biases)} issue(s)</span>
                        </div>
                        <p style='color: #8B949E; font-size: 0.85rem; margin: 0.5rem 0 0 2rem;'>Issues that should be addressed</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    for bias_type, data in found_biases.items():
                        bias_color = data.get('color', '#FF4B4B')
                        with st.expander(f"{bias_type}"):
                            st.markdown(f"""
                            <div style='padding: 0.75rem 0;'>
                                <div style='margin-bottom: 1.25rem;'>
                                    <span style='color: #8B949E; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px; font-weight: 600;'>Biased Words Found</span>
                                    <div style='margin-top: 0.75rem;'>
                            """, unsafe_allow_html=True)
                            
                            for word in data['words']:
                                st.markdown(f"""
                                <span style='
                                    display: inline-block;
                                    background: rgba(255, 75, 75, 0.12);
                                    border: 1px solid rgba(255, 75, 75, 0.25);
                                    border-radius: 6px;
                                    padding: 0.4rem 0.9rem;
                                    margin: 0.3rem;
                                    color: #FF4B4B;
                                    font-size: 0.9rem;
                                    font-weight: 500;
                                '>{word}</span>
                                """, unsafe_allow_html=True)
                            
                            st.markdown("""
                                    </div>
                                </div>
                                <div style='
                                    background: rgba(0, 212, 170, 0.08);
                                    border: 1px solid rgba(0, 212, 170, 0.15);
                                    border-radius: 10px;
                                    padding: 1.25rem;
                                    margin-top: 1rem;
                                '>
                                    <div style='display: flex; align-items: flex-start; gap: 12px;'>
                                        <span style='color: #00D4AA; font-size: 1.1rem; margin-top: 2px;'>-></span>
                                        <div>
                                            <span style='color: #00D4AA; font-weight: 600; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px;'>Suggestion</span>
                                            <p style='color: #8B949E; margin: 0.5rem 0 0 0; line-height: 1.7;'>{data['suggestion']}</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style='
                        background: rgba(0, 212, 170, 0.08);
                        border: 1px solid rgba(0, 212, 170, 0.2);
                        border-radius: 16px;
                        padding: 3rem 2rem;
                        text-align: center;
                    '>
                        <div style='
                            width: 64px;
                            height: 64px;
                            background: rgba(0, 212, 170, 0.15);
                            border: 2px solid #00D4AA;
                            border-radius: 50%;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            margin: 0 auto 1.5rem;
                            font-size: 1.8rem;
                            color: #00D4AA;
                        '>
                            <span style='color: #00D4AA; font-weight: 700;'>*</span>
                        </div>
                        <h3 style='color: #00D4AA; margin: 0 0 0.75rem 0; font-size: 1.4rem; font-weight: 700;'>No Bias Detected</h3>
                        <p style='color: #8B949E; margin: 0; font-size: 1rem;'>This is a fair and inclusive job description</p>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("<hr style='margin: 2.5rem 0;'>", unsafe_allow_html=True)
                
                st.markdown("""
                <div style='padding-bottom: 1.5rem;'>
                    <div style='display: flex; align-items: center; gap: 12px;'>
                        <span style='color: #00D4AA; font-size: 1.3rem;'>●</span>
                        <h3 style='font-size: 1.2rem; font-weight: 600; color: #FFFFFF; margin: 0;'>Clean Categories</h3>
                        <span style='
                            background: rgba(0, 212, 170, 0.15);
                            color: #00D4AA;
                            padding: 0.35rem 1rem;
                            border-radius: 20px;
                            font-size: 0.8rem;
                            font-weight: 600;
                            margin-left: auto;
                        '>Passed</span>
                    </div>
                    <p style='color: #8B949E; font-size: 0.85rem; margin: 0.5rem 0 0 2rem;'>Categories that passed bias checks</p>
                </div>
                """, unsafe_allow_html=True)
                
                clean_cats = [bias_type for bias_type in BIAS_DICT if bias_type not in found_biases]
                
                if clean_cats:
                    for bias_type in clean_cats:
                        st.markdown(f"""
                        <div style='
                            background: linear-gradient(145deg, #161B22 0%, #1C2128 100%);
                            border: 1px solid #30363D;
                            border-radius: 10px;
                            padding: 1.25rem 1.5rem;
                            margin: 0.6rem 0;
                            display: flex;
                            align-items: center;
                            gap: 14px;
                        '>
                            <div style='
                                width: 32px;
                                height: 32px;
                                background: rgba(0, 212, 170, 0.12);
                                border: 1px solid rgba(0, 212, 170, 0.2);
                                border-radius: 8px;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                            '>
                                <span style='color: #00D4AA; font-size: 0.9rem;'>*</span>
                            </div>
                            <span style='color: #E6EDF3; font-weight: 500;'>{bias_type}</span>
                            <span style='color: #00D4AA; margin-left: auto; font-size: 0.85rem; font-weight: 500;'>No bias detected</span>
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
                        <span style='color: #FFA500; font-weight: 500;'>Please paste a job description first</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
