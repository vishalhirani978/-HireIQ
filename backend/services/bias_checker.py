# Bias Detection Service
BIAS_DICT = {
    "Age Bias": {
        "words": [
            "young", "energetic", "fresh graduate", "recent graduate",
            "digital native", "old", "mature", "experienced only",
            "years old", "age limit", "under 30", "under 25", "recently retired"
        ],
        "color": "#FF4B4B",
        "suggestion": "Remove age-related language. Focus on skills and experience requirements instead of age or generation."
    },
    "Gender Bias": {
        "words": [
            "he must", "she must", "him", "her", "guys",
            "manpower", "mankind", "man the", "salesman",
            "businessman", "craftsman", "chairman", "freshman",
            "workforce men", "hardworking man"
        ],
        "color": "#FF4B4B",
        "suggestion": "Use gender-neutral language like 'they', 'the candidate', 'team member', 'professional'."
    },
    "Origin Bias": {
        "words": [
            "native speaker", "mother tongue", "born in",
            "local candidate", "nationals only", "citizens only",
            "local residents", "must be from", "pakistani only",
            "lahore based", "karachi based"
        ],
        "color": "#FF4B4B",
        "suggestion": "Focus on language proficiency level and skills instead of origin or location."
    },
    "Appearance Bias": {
        "words": [
            "well groomed", "presentable", "attractive",
            "good looking", "physically fit", "slim",
            "height", "weight", "appearance", "clean shaven"
        ],
        "color": "#FFA500",
        "suggestion": "Only mention appearance if strictly necessary for the role (e.g., acting, modeling)."
    },
    "Exclusionary Language": {
        "words": [
            "must be", "only", "exclusively", "no exceptions",
            "strictly", "mandatory background", "specific religion",
            "specific sect", "caste", "prefer married"
        ],
        "color": "#FFA500",
        "suggestion": "Use inclusive language that welcomes diverse candidates. Avoid absolute requirements unless essential."
    }
}

def detect_bias(text: str) -> tuple:
    """Detect bias in job description text"""
    found_biases = {}
    text_lower = text.lower()
    
    for bias_type, data in BIAS_DICT.items():
        found_words = []
        for word in data["words"]:
            if word.lower() in text_lower:
                found_words.append(word)
        if found_words:
            found_biases[bias_type] = {
                "words": found_words,
                "color": data["color"],
                "suggestion": data["suggestion"]
            }
    
    total_checks = len(BIAS_DICT)
    biased_count = len(found_biases)
    clean_count = total_checks - biased_count
    fairness_score = round(((total_checks - biased_count) / total_checks) * 100)
    
    if fairness_score >= 80:
        progress_message = "This job description is largely bias-free"
    elif fairness_score >= 60:
        progress_message = "This job description has some bias - review highlighted issues"
    else:
        progress_message = "This job description has significant bias - major revision needed"
    
    clean_categories = [bias_type for bias_type in BIAS_DICT if bias_type not in found_biases]
    
    return found_biases, fairness_score, biased_count, clean_count, progress_message, clean_categories
