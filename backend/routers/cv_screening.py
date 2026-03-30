# CV Screening Router
from fastapi import APIRouter, HTTPException
from models.schemas import CVScreenRequest, CVScreenResponse
from services.scorer import extract_skills, calculate_score, get_score_class, generate_recommendation
import os

router = APIRouter()

@router.post("/screen-cv", response_model=CVScreenResponse)
async def screen_cv(request: CVScreenRequest):
    """Screen a candidate CV against a job description"""
    try:
        score, percentage = calculate_score(request.job_desc, request.cv_text)
        job_skills = extract_skills(request.job_desc)
        cv_skills = extract_skills(request.cv_text)
        matched_skills = [s for s in job_skills if s in cv_skills]
        missing_skills = [s for s in job_skills if s not in cv_skills]
        recommendation = generate_recommendation(percentage, matched_skills, missing_skills)
        score_class, score_label, score_color = get_score_class(percentage)
        
        ai_analysis = ""
        try:
            from huggingface_hub import InferenceClient
            client = InferenceClient(token=os.getenv("HUGGINGFACE_TOKEN"))
            
            analysis_text = (
                f"Job requires: {request.job_desc[:200]}. "
                f"Candidate has: {request.cv_text[:200]}. "
                f"Matched skills: {', '.join(matched_skills) if matched_skills else 'None'}. "
                f"Missing skills: {', '.join(missing_skills) if missing_skills else 'None'}. "
                f"Overall match score: {percentage}%."
            )
            
            ai_summary = client.summarization(analysis_text, model="facebook/bart-large-cnn")
            ai_analysis = ai_summary.summary_text
        except Exception as e:
            ai_analysis = f"Analysis complete. Match score is {percentage}%. {recommendation}"
        
        return CVScreenResponse(
            score=score,
            percentage=percentage,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            recommendation=recommendation,
            ai_analysis=ai_analysis,
            score_class=score_class,
            score_label=score_label,
            score_color=score_color
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
