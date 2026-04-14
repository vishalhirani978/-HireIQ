from transformers import pipeline
import os
import warnings
warnings.filterwarnings('ignore')

summarizer = None

def get_summarizer():
    global summarizer
    if summarizer is None:
        token = os.getenv("HUGGINGFACE_TOKEN")
        if token and token != "your_token_here":
            try:
                summarizer = pipeline(
                    "summarization",
                    model="facebook/bart-large-cnn",
                    token=token
                )
            except Exception:
                summarizer = None
    return summarizer

def get_ai_analysis(job_description: str, candidate_cv: str) -> str:
    try:
        model = get_summarizer()
        if model is None:
            return generate_fallback_analysis(job_description, candidate_cv)
        
        input_text = f"""
        Job Requirements: {job_description[:500]}
        
        Candidate Profile: {candidate_cv[:500]}
        
        Please provide a brief analysis of how well this candidate matches the job requirements.
        """
        
        result = model(input_text, max_length=200, min_length=50, do_sample=False)
        return result[0]['summary_text']
    except Exception:
        return generate_fallback_analysis(job_description, candidate_cv)

def generate_fallback_analysis(job_description: str, candidate_cv: str) -> str:
    job_lower = job_description.lower()
    cv_lower = candidate_cv.lower()
    
    skills_found = []
    common_skills = ["python", "java", "sql", "communication", "teamwork", "leadership", 
                     "analysis", "management", "excel", "javascript", "react"]
    
    for skill in common_skills:
        if skill in cv_lower:
            skills_found.append(skill)
    
    analysis = f"Based on the analysis, this candidate demonstrates "
    
    if len(skills_found) >= 4:
        analysis += f"strong alignment with the role requirements, showing proficiency in {', '.join(skills_found[:4])}. "
    elif len(skills_found) >= 1:
        analysis += f"some relevant skills including {', '.join(skills_found)}. "
    else:
        analysis += "limited direct alignment with the stated requirements. "
    
    analysis += "The candidate's experience should be verified through an interview to assess practical knowledge and cultural fit."
    
    return analysis
