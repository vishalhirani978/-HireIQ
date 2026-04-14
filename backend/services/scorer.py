from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

SKILLS_LIST = [
    "python", "sql", "java", "machine learning", "ml",
    "data science", "pandas", "numpy", "scikit-learn",
    "tensorflow", "keras", "deep learning", "nlp",
    "communication", "teamwork", "leadership",
    "javascript", "react", "nodejs", "html", "css",
    "excel", "powerpoint", "management", "analysis"
]

def extract_skills(text: str) -> set:
    text_lower = text.lower()
    found = set()
    for skill in SKILLS_LIST:
        if skill in text_lower:
            found.add(skill)
    return found

def calculate_tfidf_similarity(text1: str, text2: str) -> float:
    try:
        vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        tfidf_matrix = vectorizer.fit_transform([text1, text2])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return float(similarity)
    except:
        return 0.0

def calculate_skill_match_ratio(job_skills: set, candidate_skills: set) -> float:
    if not job_skills:
        return 0.0
    matched = len(job_skills & candidate_skills)
    return matched / len(job_skills)

def get_recommendation(score: float) -> tuple[str, str, str]:
    if score >= 70:
        return "STRONG HIRE", "success", "Strong Match"
    elif score >= 40:
        return "MAYBE", "warning", "Partial Match"
    else:
        return "REJECT", "danger", "Low Match"

def score_candidate(job_description: str, candidate_cv: str) -> dict:
    job_skills = extract_skills(job_description)
    candidate_skills = extract_skills(candidate_cv)
    
    matched_skills = list(job_skills & candidate_skills)
    missing_skills = list(job_skills - candidate_skills)
    
    tfidf_score = calculate_tfidf_similarity(job_description, candidate_cv)
    skill_ratio = calculate_skill_match_ratio(job_skills, candidate_skills)
    
    final_score = (tfidf_score * 0.4) + (skill_ratio * 0.6)
    percentage = min(100, round(final_score * 100, 1))
    
    recommendation, score_class, score_label = get_recommendation(percentage)
    
    return {
        "score": final_score,
        "percentage": percentage,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "matched_count": len(matched_skills),
        "missing_count": len(missing_skills),
        "recommendation": recommendation,
        "ai_analysis": "",
        "score_class": score_class,
        "score_label": score_label
    }
