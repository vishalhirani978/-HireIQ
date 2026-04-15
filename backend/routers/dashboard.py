from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from services.scorer import score_candidate

router = APIRouter()

class CandidateInput(BaseModel):
    name: str
    cv: str

class CompareCandidatesRequest(BaseModel):
    job_description: str
    candidates: List[CandidateInput]

class CandidateResult(BaseModel):
    name: str
    score: float
    matched: int
    missing: int
    matched_skills: List[str]
    missing_skills: List[str]
    verdict: str

class CompareCandidatesResponse(BaseModel):
    results: List[CandidateResult]

@router.post("/compare-candidates", response_model=CompareCandidatesResponse)
async def compare_candidates(request: CompareCandidatesRequest):
    try:
        if not request.job_description.strip():
            raise HTTPException(status_code=400, detail="Job description is required")
        if not request.candidates:
            raise HTTPException(status_code=400, detail="At least one candidate is required")
        
        results = []
        for candidate in request.candidates:
            if not candidate.name.strip():
                raise HTTPException(status_code=400, detail="Candidate name is required")
            if not candidate.cv.strip():
                raise HTTPException(status_code=400, detail=f"CV for {candidate.name} is required")
            
            result = score_candidate(request.job_description, candidate.cv)
            results.append({
                "name": candidate.name,
                "score": result["percentage"],
                "matched": result["matched_count"],
                "missing": result["missing_count"],
                "matched_skills": result["matched_skills"],
                "missing_skills": result["missing_skills"],
                "verdict": result["recommendation"]
            })
        
        results.sort(key=lambda x: x["score"], reverse=True)
        
        return {"results": results}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
