# backend/bias_checker.py
# Bias detection logic

BIAS_DICT = {
    "Age Bias": {
        "words": [
            "young", "energetic", "fresh graduate", "recent graduate",
            "digital native", "old", "mature", "experienced only",
            "years old", "age limit", "under 30", "under 25"
        ],
        "color": "🔴",
        "suggestion": "Remove age-related language — focus on skills and experience instead!"
    },
    "Gender Bias": {
        "words": [
            "he must", "she must", "him", "her", "guys",
            "manpower", "mankind", "man the", "salesman",
            "businessman", "craftsman", "chairman", "freshman"
        ],
        "color": "🔴",
        "suggestion": "Use gender-neutral language like 'they', 'the candidate', 'team member'!"
    },
    "Origin Bias": {
        "words": [
            "native speaker", "mother tongue", "born in",
            "local candidate", "nationals only", "citizens only",
            "local residents", "must be from"
        ],
        "color": "🔴",
        "suggestion": "Focus on language proficiency level instead of origin!"
    },
    "Appearance Bias": {
        "words": [
            "well groomed", "presentable", "attractive",
            "good looking", "physically fit", "slim",
            "height", "weight", "appearance"
        ],
        "color": "🟡",
        "suggestion": "Only mention appearance if strictly necessary for the role!"
    },
    "Exclusionary Language": {
        "words": [
            "must be", "only", "exclusively", "no exceptions",
            "strictly", "mandatory background", "specific religion",
            "specific sect", "caste"
        ],
        "color": "🟡",
        "suggestion": "Use inclusive language that welcomes diverse candidates!"
    }
}


def detect_bias(text):
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

    return found_biases, fairness_score, biased_count, clean_count