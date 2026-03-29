# pages/bias_detector.py
import streamlit as st
from backend.bias_checker import detect_bias, BIAS_DICT

def show_bias_detector():
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
                found_biases, fairness_score, biased_count, clean_count = detect_bias(job_desc_bias)

            st.divider()
            st.subheader("📊 Bias Analysis Results")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("🎯 Fairness Score", f"{fairness_score}%")
            with col2:
                st.metric("⚠️ Bias Types Found", biased_count)
            with col3:
                st.metric("✅ Clean Categories", clean_count)

            st.progress(fairness_score / 100)

            if fairness_score >= 80:
                st.success("✅ This job description is largely bias-free!")
            elif fairness_score >= 60:
                st.warning("⚠️ This job description has some bias — review highlighted issues!")
            else:
                st.error("❌ This job description has significant bias — major revision needed!")

            st.divider()

            if found_biases:
                st.subheader("⚠️ Bias Found:")
                for bias_type, data in found_biases.items():
                    with st.expander(f"{data['color']} {bias_type} — Found: {', '.join(data['words'])}"):
                        st.write(f"**Biased words found:** {', '.join(data['words'])}")
                        st.write(f"**💡 Suggestion:** {data['suggestion']}")
            else:
                st.success("🎉 No bias detected! This is a fair and inclusive job description!")

            st.subheader("✅ Clean Categories:")
            for bias_type in BIAS_DICT:
                if bias_type not in found_biases:
                    st.success(f"✅ {bias_type} — No bias detected!")
        else:
            st.warning("⚠️ Please paste a job description first!")



