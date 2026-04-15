from services.scorer import extract_skills

DIFFICULTY_QUESTIONS = {
    "Easy": [
        "Tell me about yourself and your background.",
        "Why are you interested in this role?",
        "What are your key strengths?",
        "Where do you see yourself in 5 years?",
        "Why are you leaving your current job?",
        "What motivates you to do your best work?",
        "Describe your ideal work environment.",
        "How do you handle constructive criticism?"
    ],
    "Medium": [
        "Describe a challenging problem you solved recently.",
        "How do you stay updated with the latest industry trends?",
        "Tell me about working under pressure.",
        "How do you handle tight deadlines?",
        "Describe a time you learned a new skill quickly.",
        "How would you approach an unfamiliar project?",
        "Tell me about a time you had a conflict with a colleague.",
        "How do you prioritize tasks when everything is urgent?"
    ],
    "Hard": [
        "Design a scalable system to process 1 million records daily.",
        "How would you handle model drift in production?",
        "What are the trade-offs between precision and recall?",
        "How would you architect a recommendation system?",
        "What strategies would you use to reduce overfitting?",
        "Describe how you would optimize a slow database query.",
        "How would you design a system with zero downtime deployment?",
        "Explain how you would implement proper error handling at scale."
    ]
}

VERIFY_TEMPLATES = [
    "Tell me about a project where you used {skill}. What was the outcome?",
    "How confident are you with {skill} on a scale of 1-10? Give an example.",
    "What is the most complex task you did using {skill}?",
    "How long have you worked with {skill} and what have you built?",
    "What challenges did you face with {skill} and how did you solve them?"
]

def generate_questions(job_description: str, candidate_cv: str, difficulty: str, num_questions: int) -> dict:
    job_skills = extract_skills(job_description)
    candidate_skills = extract_skills(candidate_cv)
    
    matched_skills = list(job_skills & candidate_skills)
    missing_skills = list(job_skills - candidate_skills)
    
    gap_count = min(len(missing_skills), num_questions // 3)
    verify_count = min(len(matched_skills), num_questions // 3)
    difficulty_count = num_questions - gap_count - verify_count
    
    gap_questions = []
    for skill in missing_skills[:gap_count]:
        gap_questions.append(
            f"You listed {skill}. Can you walk us through your experience with {skill}?"
        )
    
    verify_questions = []
    for i, skill in enumerate(matched_skills[:verify_count]):
        template = VERIFY_TEMPLATES[i % len(VERIFY_TEMPLATES)]
        verify_questions.append(template.format(skill=skill))
    
    difficulty_questions = DIFFICULTY_QUESTIONS.get(difficulty, DIFFICULTY_QUESTIONS["Medium"])[
        :difficulty_count
    ]
    
    return {
        "total": len(gap_questions) + len(verify_questions) + len(difficulty_questions),
        "difficulty": difficulty,
        "gap_questions": gap_questions,
        "verify_questions": verify_questions,
        "difficulty_questions": difficulty_questions,
        "gap_count": len(gap_questions),
        "verify_count": len(verify_questions),
        "difficulty_count": len(difficulty_questions)
    }
