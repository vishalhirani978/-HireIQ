# Pydantic Schemas
from pydantic import BaseModel
from typing import List, Optional

class CVScreenRequest(BaseModel):
    job_desc: str
    cv_text: str

class CVScreenResponse(BaseModel):
    score: float
    percentage: float
    matched_skills: List[str]
    missing_skills: List[str]
    recommendation: str
    ai_analysis: str
    score_class: str
    score_label: str
    score_color: str

class Candidate(BaseModel):
    name: str
    cv: str

class CompareRequest(BaseModel):
    job_desc: str
    candidates: List[Candidate]

class CandidateResult(BaseModel):
    name: str
    score: float
    matched: int
    missing: int
    verdict: str
    score_color: str

class CompareResponse(BaseModel):
    results: List[CandidateResult]

class QuestionsRequest(BaseModel):
    job_desc: str
    cv_text: str
    difficulty: str = "Medium"
    num_questions: int = 5

class QuestionsResponse(BaseModel):
    gap_questions: List[str]
    verify_questions: List[str]
    difficulty_questions: List[str]
    gap_count: int
    verify_count: int
    difficulty_count: int
    total: int

class BiasRequest(BaseModel):
    job_desc: str

class BiasWord(BaseModel):
    words: List[str]
    suggestion: str

class BiasResponse(BaseModel):
    found_biases: dict
    fairness_score: float
    biased_count: int
    clean_count: int
    progress_message: str
    clean_categories: List[str]
