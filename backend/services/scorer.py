# CV Scoring Service
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS_LIST = [
    "python", "sql", "java", "javascript", "typescript",
    "machine learning", "ml", "data science", "pandas", "numpy",
    "scikit-learn", "tensorflow", "keras", "pytorch", "deep learning",
    "nlp", "natural language processing", "react", "nodejs", "angular",
    "vue", "html", "css", "django", "flask", "fastapi",
    "excel", "powerpoint", "tableau", "power bi", "aws", "azure",
    "docker", "kubernetes", "git", "linux", "sql server",
    "mongodb", "postgresql", "mysql", "redis", "elasticsearch",
    "communication", "teamwork", "leadership", "problem solving",
    "management", "analysis", "project management", "agile", "scrum"
]

def extract_skills(text: str) -> list:
    """Extract technical and soft skills from text"""
    found = []
    text_lower = text.lower()
    for skill in SKILLS_LIST:
        if skill in text_lower:
            found.append(skill.title())
    return list(set(found))

def calculate_score(job_desc: str, cv_text: str) -> tuple:
    """Calculate score based on skills matching"""
    job_skills = extract_skills(job_desc)
    cv_skills = extract_skills(cv_text)
    
    if not job_skills:
        return 0.0, 0.0
    
    matched = [s for s in job_skills if s.lower() in [cs.lower() for cs in cv_skills]]
    matched_count = len(matched)
    total_required = len(job_skills)
    
    skills_percentage = (matched_count / total_required) * 100
    
    vectorizer = TfidfVectorizer()
    try:
        vectors = vectorizer.fit_transform([job_desc, cv_text])
        tfidf_score = cosine_similarity(vectors[0], vectors[1])[0][0] * 100
    except:
        tfidf_score = 0
    
    percentage = round((skills_percentage * 0.7) + (tfidf_score * 0.3), 1)
    percentage = min(percentage, 100)
    
    return percentage / 100, percentage

def get_score_class(percentage: float) -> tuple:
    """Get score classification"""
    if percentage >= 70:
        return "high", "Strong Match", "#00D4AA"
    elif percentage >= 40:
        return "medium", "Partial Match", "#FFA500"
    else:
        return "low", "Weak Match", "#FF4B4B"

def generate_recommendation(percentage: float, matched_skills: list, missing_skills: list) -> str:
    """Generate hiring recommendation based on score"""
    matched_count = len(matched_skills)
    missing_count = len(missing_skills)
    
    if percentage >= 70:
        return f"STRONG HIRE - {percentage}% Match. This candidate is an excellent fit with {matched_count} matched skills including {', '.join(matched_skills[:3]) if matched_skills else 'N/A'}. Recommended for immediate technical interview."
    elif percentage >= 40:
        return f"MAYBE - {percentage}% Match. This candidate partially meets requirements with {matched_count} matched skills: {', '.join(matched_skills) if matched_skills else 'None'}. Missing {missing_count} skills: {', '.join(missing_skills) if missing_skills else 'None'}. Consider for interview if no stronger candidates available."
    else:
        return f"REJECT - {percentage}% Match. This candidate does not meet minimum requirements. Only matches {matched_count} skills. Missing {missing_count} critical skills. Do not proceed with this candidate."
