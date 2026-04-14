from services.scorer import extract_skills, SKILLS_LIST

BIAS_PATTERNS = {
    "Age Bias": {
        "words": ["young", "energetic", "fresh graduate", "digital native", "old", 
                  "mature", "years old", "age limit", "under 30", "under 25",
                  "recent graduate", "new generation"],
        "suggestion": "Remove age-related language. Focus on skills and experience instead."
    },
    "Gender Bias": {
        "words": ["he must", "she must", "him", "her", "guys", "manpower", 
                  "mankind", "man the", "salesman", "businessman", "craftsman", "chairman",
                  "waiter", "secretary"],
        "suggestion": "Use gender-neutral language like 'they', 'the candidate', 'team member'."
    },
    "Origin Bias": {
        "words": ["native speaker", "mother tongue", "born in", "local candidate",
                  "nationals only", "citizens only", "local residents", "must be from",
                  "from lahore", "from karachi", "from islamabad", "pakistani only"],
        "suggestion": "Focus on language proficiency level instead of origin."
    },
    "Appearance Bias": {
        "words": ["well groomed", "presentable", "attractive", "good looking",
                  "physically fit", "slim", "height", "weight", "appearance",
                  "good looking", "beautiful", "handsome"],
        "suggestion": "Only mention appearance if strictly relevant to the role."
    },
    "Exclusionary Language": {
        "words": ["must be", "only", "exclusively", "no exceptions", "strictly",
                  "mandatory background", "specific religion", "caste", "no freshers",
                  "no beginners", "experienced only"],
        "suggestion": "Use inclusive language that welcomes diverse candidates."
    }
}

def detect_bias(job_description: str) -> dict:
    text_lower = job_description.lower()
    found_biases = {}
    biased_count = 0
    clean_count = 0
    
    for bias_type, pattern in BIAS_PATTERNS.items():
        found_words = []
        for word in pattern["words"]:
            if word in text_lower:
                found_words.append(word)
        
        if found_words:
            found_biases[bias_type] = {
                "words": found_words,
                "suggestion": pattern["suggestion"]
            }
            biased_count += 1
        else:
            clean_count += 1
    
    total_categories = len(BIAS_PATTERNS)
    fairness_score = int(((total_categories - biased_count) / total_categories) * 100)
    
    if fairness_score >= 80:
        verdict = "Largely bias-free"
    elif fairness_score >= 60:
        verdict = "Some bias detected"
    else:
        verdict = "Significant bias - major revision needed"
    
    return {
        "fairness_score": fairness_score,
        "biased_count": biased_count,
        "clean_count": clean_count,
        "found_biases": found_biases,
        "verdict": verdict
    }
