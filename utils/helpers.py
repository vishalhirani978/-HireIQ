# utils/helpers.py
# Shared helper functions used across all pages

def extract_skills(text):
    """Extract technical and soft skills from text"""
    skills = [
        "python", "sql", "java", "machine learning", "ml",
        "data science", "pandas", "numpy", "scikit-learn",
        "tensorflow", "keras", "deep learning", "nlp",
        "communication", "teamwork", "leadership",
        "javascript", "react", "nodejs", "html", "css",
        "excel", "powerpoint", "management", "analysis"
    ]
    found = []
    text_lower = text.lower()
    for skill in skills:
        if skill in text_lower:
            found.append(skill.title())
    return found


def get_match_score(job_desc, cv_text):
    """Calculate TF-IDF cosine similarity score between job and CV"""
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([job_desc, cv_text])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    percentage = round(score * 100, 1)
    return score, percentage


def get_recommendation(percentage, matched_skills, missing_skills):
    """Generate hiring recommendation based on score"""
    matched_count = len(matched_skills)
    missing_count = len(missing_skills)

    if percentage >= 70:
        return f"""
**[STRONG HIRE] — {percentage}% Match**

This candidate is an excellent fit for the role!

**Why Hire:**
- Matches {matched_count} out of {matched_count + missing_count} required skills
- Matched Skills: {', '.join(matched_skills) if matched_skills else 'N/A'}
- Score above 70% indicates strong alignment

**Suggested Action:** Invite for technical interview immediately!
        """
    elif percentage >= 40:
        return f"""
**[MAYBE] — {percentage}% Match**

This candidate partially meets the requirements.

**Why Consider:**
- Matches {matched_count} key skills: {', '.join(matched_skills) if matched_skills else 'None'}
- Shows potential in core areas

**Why Hesitate:**
- Missing {missing_count} skills: {', '.join(missing_skills) if missing_skills else 'None'}
- May need additional training

**Suggested Action:** Consider for interview only if no stronger candidates available.
        """
    else:
        return f"""
**[REJECT] — {percentage}% Match**

This candidate does not meet the minimum requirements.

**Why Reject:**
- Only matches {matched_count} skills: {', '.join(matched_skills) if matched_skills else 'None'}
- Missing {missing_count} critical skills: {', '.join(missing_skills) if missing_skills else 'None'}
- Score below 40% indicates poor alignment

**Suggested Action:** Do not proceed. Look for stronger candidates.
        """