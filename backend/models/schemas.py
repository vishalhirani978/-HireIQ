from pydantic import BaseModel
from typing import List, Optional

class CVScreeningRequest(BaseModel):
    job_description: str
    candidate_cv: str

class CVScreeningResponse(BaseModel):
    score: float
    percentage: float
    matched_skills: List[str]
    missing_skills: List[str]
    matched_count: int
    missing_count: int
    recommendation: str
    ai_analysis: str
    score_class: str
    score_label: str

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

class InterviewRequest(BaseModel):
    job_description: str
    candidate_cv: str
    difficulty: str
    num_questions: int

class InterviewResponse(BaseModel):
    total: int
    difficulty: str
    gap_questions: List[str]
    verify_questions: List[str]
    difficulty_questions: List[str]
    gap_count: int
    verify_count: int
    difficulty_count: int

class BiasDetectionRequest(BaseModel):
    job_description: str

class BiasType(BaseModel):
    words: List[str]
    suggestion: str

class BiasDetectionResponse(BaseModel):
    fairness_score: int
    biased_count: int
    clean_count: int
    found_biases: dict
