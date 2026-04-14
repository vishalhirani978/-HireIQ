from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from services.bias_checker import detect_bias

router = APIRouter()

class BiasDetectionRequest(BaseModel):
    job_description: str

class BiasType(BaseModel):
    words: List[str]
    suggestion: str

class BiasDetectionResponse(BaseModel):
    fairness_score: int
    biased_count: int
    clean_count: int
    found_biases: Dict[str, BiasType]

@router.post("/detect-bias", response_model=BiasDetectionResponse)
async def detect_job_bias(request: BiasDetectionRequest):
    try:
        if not request.job_description.strip():
            raise HTTPException(status_code=400, detail="Job description is required")
        
        result = detect_bias(request.job_description)
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
