# Backend - FastAPI Entry Point
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routers import cv_screening, dashboard, interview, bias_detector
import os

load_dotenv()

app = FastAPI(
    title="HireIQ API",
    description="AI-Powered Hiring Assistant API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cv_screening.router, prefix="/api", tags=["CV Screening"])
app.include_router(dashboard.router, prefix="/api", tags=["Dashboard"])
app.include_router(interview.router, prefix="/api", tags=["Interview"])
app.include_router(bias_detector.router, prefix="/api", tags=["Bias Detector"])

@app.get("/")
def root():
    return {"message": "HireIQ API is running", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "HireIQ API"}
