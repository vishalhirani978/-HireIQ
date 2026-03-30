# Interview Questions Router
from fastapi import APIRouter, HTTPException
from models.schemas import QuestionsRequest, QuestionsResponse
from services.scorer import extract_skills
from services.question_gen import generate_questions

router = APIRouter()

@router.post("/generate-questions", response_model=QuestionsResponse)
async def generate_interview_questions(request: QuestionsRequest):
    """Generate interview questions based on job description and CV"""
    try:
        job_skills = extract_skills(request.job_desc)
        cv_skills = extract_skills(request.cv_text)
        missing_skills = [s for s in job_skills if s not in cv_skills]
        matched_skills = [s for s in job_skills if s in cv_skills]
        
        questions = generate_questions(
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            difficulty=request.difficulty,
            num_questions=request.num_questions
        )
        
        return QuestionsResponse(**questions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
