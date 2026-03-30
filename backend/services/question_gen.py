# Question Generation Service
EASY_QUESTIONS = [
    "Tell me about yourself and your professional background.",
    "Why are you interested in this position and our company?",
    "What are your key strengths that make you a good fit?",
    "Where do you see yourself in 5 years?",
    "Why are you leaving your current job?",
    "Describe your ideal work environment.",
    "What motivates you to do your best work?"
]

MEDIUM_QUESTIONS = [
    "Describe a challenging problem you solved and how you approached it.",
    "How do you stay updated with the latest technologies in your field?",
    "Tell me about a time you worked in a team under pressure.",
    "How do you handle tight deadlines and multiple priorities?",
    "Describe a situation where you had to learn something quickly.",
    "Tell me about a project you're most proud of.",
    "How do you approach debugging or troubleshooting issues?"
]

HARD_QUESTIONS = [
    "Design a scalable system for processing 1 million records daily.",
    "How would you handle model drift in a production environment?",
    "Explain the trade-offs between precision and recall in your last project.",
    "How would you architect a real-time recommendation system?",
    "What strategies would you use to reduce overfitting in a deep learning model?",
    "Describe your experience with MLOps and deployment pipelines.",
    "How would you optimize a slow-performing database query?"
]

SKILL_TEMPLATES = [
    "Tell me about a specific project where you used {skill}. What was the outcome?",
    "How confident are you with {skill} on a scale of 1-10? Give an example.",
    "What is the most complex task you have done using {skill}?",
    "How long have you been working with {skill} and what have you built?",
    "What challenges did you face while using {skill} and how did you solve them?"
]

BEHAVIORAL_TEMPLATES = [
    "Tell me about a time when you had to meet a tight deadline.",
    "Describe a situation where you had to work with a difficult team member.",
    "Give an example of a goal you reached and how you achieved it.",
    "Tell me about a time you failed and what you learned from it."
]

def generate_questions(matched_skills: list, missing_skills: list, difficulty: str, num_questions: int) -> dict:
    """Generate interview questions based on skills and difficulty"""
    gap_count = min(len(missing_skills), max(1, num_questions // 3))
    verify_count = min(len(matched_skills), max(1, num_questions // 3))
    difficulty_count = num_questions - gap_count - verify_count
    
    gap_questions = []
    for skill in missing_skills:
        gap_questions.append(
            f"You listed {skill} as a requirement. Can you walk us through your experience with {skill} "
            f"and explain how you've applied it in your work?"
        )
    
    verify_questions = []
    for i, skill in enumerate(matched_skills):
        template = SKILL_TEMPLATES[i % len(SKILL_TEMPLATES)]
        verify_questions.append(template.format(skill=skill))
    
    if difficulty == "Easy":
        difficulty_questions = EASY_QUESTIONS
    elif difficulty == "Medium":
        difficulty_questions = MEDIUM_QUESTIONS
    else:
        difficulty_questions = HARD_QUESTIONS
    
    return {
        "gap_questions": gap_questions[:gap_count],
        "verify_questions": verify_questions[:verify_count],
        "difficulty_questions": difficulty_questions[:difficulty_count],
        "gap_count": gap_count,
        "verify_count": verify_count,
        "difficulty_count": difficulty_count,
        "total": gap_count + verify_count + difficulty_count
    }
