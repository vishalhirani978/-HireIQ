# Bias Detector Router
from fastapi import APIRouter, HTTPException
from models.schemas import BiasRequest, BiasResponse
from services.bias_checker import detect_bias

router = APIRouter()

@router.post("/detect-bias", response_model=BiasResponse)
async def detect_bias_in_jd(request: BiasRequest):
    """Detect bias in a job description"""
    try:
        found_biases, fairness_score, biased_count, clean_count, progress_message, clean_categories = detect_bias(request.job_desc)
        
        return BiasResponse(
            found_biases=found_biases,
            fairness_score=fairness_score,
            biased_count=biased_count,
            clean_count=clean_count,
            progress_message=progress_message,
            clean_categories=clean_categories
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
