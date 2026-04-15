from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.scorer import score_candidate
from services.summarizer import get_ai_analysis

router = APIRouter()

class CVScreeningRequest(BaseModel):
    job_description: str
    candidate_cv: str

class CVScreeningResponse(BaseModel):
    score: float
    percentage: float
    matched_skills: list[str]
    missing_skills: list[str]
    matched_count: int
    missing_count: int
    recommendation: str
    ai_analysis: str
    score_class: str
    score_label: str

@router.post("/screen-cv", response_model=CVScreeningResponse)
async def screen_cv(request: CVScreeningRequest):
    try:
        if not request.job_description.strip():
            raise HTTPException(status_code=400, detail="Job description is required")
        if not request.candidate_cv.strip():
            raise HTTPException(status_code=400, detail="Candidate CV is required")
        
        result = score_candidate(request.job_description, request.candidate_cv)
        
        ai_analysis = get_ai_analysis(request.job_description, request.candidate_cv)
        result["ai_analysis"] = ai_analysis
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
