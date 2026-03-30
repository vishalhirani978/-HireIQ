# Dashboard Router
from fastapi import APIRouter, HTTPException
from models.schemas import CompareRequest, CompareResponse, CandidateResult
from services.scorer import extract_skills, calculate_score, get_score_class

router = APIRouter()

@router.post("/compare-candidates", response_model=CompareResponse)
async def compare_candidates(request: CompareRequest):
    """Compare multiple candidates against a job description"""
    try:
        results = []
        
        for candidate in request.candidates:
            score, percentage = calculate_score(request.job_desc, candidate.cv)
            job_skills = extract_skills(request.job_desc)
            cv_skills = extract_skills(candidate.cv)
            matched = [s for s in job_skills if s in cv_skills]
            missing = [s for s in job_skills if s not in cv_skills]
            
            if percentage >= 70:
                verdict = "HIRE"
                score_color = "#00D4AA"
            elif percentage >= 40:
                verdict = "MAYBE"
                score_color = "#FFA500"
            else:
                verdict = "REJECT"
                score_color = "#FF4B4B"
            
            results.append(CandidateResult(
                name=candidate.name,
                score=percentage,
                matched=len(matched),
                missing=len(missing),
                verdict=verdict,
                score_color=score_color
            ))
        
        results.sort(key=lambda x: x.score, reverse=True)
        
        return CompareResponse(results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
