import os
from typing import Optional

def get_ai_analysis(job_description: str, candidate_cv: str) -> str:
    """Generate AI analysis using Hugging Face summarization model"""
    try:
        from huggingface_hub import InferenceClient
        
        token = os.getenv("HUGGINGFACE_TOKEN")
        if not token or token == "your_token_here":
            return generate_fallback_analysis(job_description, candidate_cv)
        
        client = InferenceClient("facebook/bart-large-cnn", token=token)
        
        prompt = f"""Job Requirements:
{job_description}

Candidate Profile:
{candidate_cv}

Analyze the candidate's suitability for this role. Focus on:
1. Skills match
2. Experience alignment
3. Key strengths
4. Potential gaps
5. Overall assessment

Provide a concise analysis (2-3 sentences):"""
        
        response = client.summarization(prompt, max_length=200, min_length=50)
        return response[0]["summary_text"]
        
    except Exception as e:
        return generate_fallback_analysis(job_description, candidate_cv)

def generate_fallback_analysis(job_description: str, candidate_cv: str) -> str:
    """Generate basic analysis when AI is unavailable"""
    from services.scorer import extract_skills, calculate_match_score
    
    job_skills = extract_skills(job_description)
    cv_skills = extract_skills(candidate_cv)
    matched = [s for s in job_skills if s in cv_skills]
    missing = [s for s in job_skills if s not in cv_skills]
    
    score, _, _ = calculate_match_score(job_description, candidate_cv)
    
    analysis = f"The candidate shows a {'strong' if score >= 0.7 else 'moderate' if score >= 0.4 else 'limited'} match for this position. "
    
    if matched:
        analysis += f"Key strengths include: {', '.join(matched[:5])}. "
    
    if missing:
        analysis += f"Areas that may need development: {', '.join(missing[:3])}. "
    
    analysis += "Consider conducting a technical interview to verify claimed skills."
    
    return analysis
