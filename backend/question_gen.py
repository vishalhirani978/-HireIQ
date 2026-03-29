# backend/question_gen.py
# Interview question generation logic

EASY_QUESTIONS = [
    "Tell me about yourself and your background.",
    "Why are you interested in this position?",
    "What are your key strengths?",
    "Where do you see yourself in 5 years?",
    "Why are you leaving your current job?",
]

MEDIUM_QUESTIONS = [
    "Describe a challenging problem you solved and how you approached it.",
    "How do you stay updated with the latest technologies in your field?",
    "Tell me about a time you worked in a team under pressure.",
    "How do you handle tight deadlines and multiple priorities?",
    "Describe a situation where you had to learn something quickly.",
]

HARD_QUESTIONS = [
    "Design a scalable ML pipeline for processing 1 million records daily.",
    "How would you handle model drift in a production environment?",
    "Explain the trade-offs between precision and recall in your last project.",
    "How would you architect a real-time recommendation system?",
    "What strategies would you use to reduce overfitting in a deep learning model?",
]

SKILL_TEMPLATES = [
    "Tell me about a specific project where you used {}. What was the outcome?",
    "How confident are you with {} on a scale of 1-10? Give an example.",
    "What is the most complex task you have done using {}?",
    "How long have you been working with {} and what have you built?",
    "What challenges did you face while using {} and how did you solve them?"
]


def generate_questions(matched_skills, missing_skills, difficulty, num_questions):
    """Generate interview questions based on skills and difficulty"""

    gap_count = min(len(missing_skills), max(1, num_questions // 3))
    verify_count = min(len(matched_skills), max(1, num_questions // 3))
    difficulty_count = num_questions - gap_count - verify_count

    # Gap questions
    gap_questions = []
    for skill in missing_skills:
        gap_questions.append(
            f"You listed {skill} as a requirement but it's not clear in the CV. "
            f"Can you walk us through your experience with {skill}?"
        )

    # Verify questions
    verify_questions = []
    for i, skill in enumerate(matched_skills):
        template = SKILL_TEMPLATES[i % len(SKILL_TEMPLATES)]
        verify_questions.append(template.format(skill))

    # Difficulty questions
    if difficulty == "Easy":
        difficulty_questions = EASY_QUESTIONS
    elif difficulty == "Medium":
        difficulty_questions = MEDIUM_QUESTIONS
    else:
        difficulty_questions = HARD_QUESTIONS

    return {
        "gap": gap_questions[:gap_count],
        "verify": verify_questions[:verify_count],
        "difficulty": difficulty_questions[:difficulty_count],
        "gap_count": gap_count,
        "verify_count": verify_count,
        "difficulty_count": difficulty_count
    }