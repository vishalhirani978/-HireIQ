from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.question_gen import generate_questions

router = APIRouter()

class InterviewRequest(BaseModel):
    job_description: str
    candidate_cv: str
    difficulty: str
    num_questions: int

class InterviewResponse(BaseModel):
    total: int
    difficulty: str
    gap_questions: list[str]
    verify_questions: list[str]
    difficulty_questions: list[str]
    gap_count: int
    verify_count: int
    difficulty_count: int

@router.post("/generate-questions", response_model=InterviewResponse)
async def generate_interview_questions(request: InterviewRequest):
    try:
        if not request.job_description.strip():
            raise HTTPException(status_code=400, detail="Job description is required")
        if not request.candidate_cv.strip():
            raise HTTPException(status_code=400, detail="Candidate CV is required")
        if request.difficulty not in ["Easy", "Medium", "Hard"]:
            raise HTTPException(status_code=400, detail="Difficulty must be Easy, Medium, or Hard")
        if request.num_questions < 3 or request.num_questions > 10:
            raise HTTPException(status_code=400, detail="Number of questions must be between 3 and 10")
        
        result = generate_questions(
            request.job_description,
            request.candidate_cv,
            request.difficulty,
            request.num_questions
        )
        
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
