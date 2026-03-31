# HireIQ - AI-Powered Hiring Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.104-green.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/React-18-61DAFB.svg" alt="React">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/HuggingFace-Inference-FFD21E.svg" alt="HuggingFace">
  <img src="https://img.shields.io/badge/Built%20For-Pakistan-009900.svg" alt="Pakistan">
</p>

> **HireIQ** is a free AI-powered hiring assistant built for Pakistani 
> startups and SMEs — making CV screening faster, fairer and smarter.

---

## The Problem We Solve

Hiring is a major challenge for startups and SMEs in Pakistan:

- Hours wasted screening CVs manually
- Unconscious bias in job descriptions and decisions
- No standardized scoring system — subjective and inconsistent
- Expensive recruitment agencies draining limited budgets

**HireIQ** addresses this with AI-powered analysis that is fast, 
fair and actionable.

---

## Features

| Feature | Description |
|---|---|
| CV Screening | Match a CV against a job description — get skill analysis and a clear verdict |
| Candidate Dashboard | Compare up to 5 candidates side by side with visual charts |
| Interview Questions | Auto-generate questions based on skill gaps and difficulty level |
| Bias Detector | Detect 5 types of bias in job descriptions with improvement suggestions |

---

## How It Works
```
┌─────────────────┐     ┌──────────────────────┐     ┌─────────────────┐
│   1. INPUT      │     │   2. AI ENGINE        │     │   3. RESULTS    │
│                 │     │                        │     │                 │
│  Job Desc + CV  │ ──► │  TF-IDF Scoring       │ ──► │  Score + Report │
│                 │     │  + Skill Extraction    │     │                 │
│                 │     │  + HuggingFace AI      │     │                 │
└─────────────────┘     └──────────────────────┘     └─────────────────┘
```

---

## Tech Stack

### Frontend
| Technology | Purpose |
|---|---|
| React 18 | UI Framework |
| React Router | Navigation |
| Axios | API calls |
| Recharts | Data visualization |
| Custom CSS | Dark theme styling |

### Backend
| Technology | Purpose |
|---|---|
| FastAPI | REST API framework |
| Python 3.11 | Core language |
| Hugging Face API | AI text summarization |
| Scikit-learn | TF-IDF scoring |
| Pandas | Data handling |
| python-dotenv | Environment variables |

### Architecture
```
┌──────────────────────────────────────────────────────┐
│                    FRONTEND                           │
│         React 18 + Recharts + Custom CSS             │
└────────────────────────┬─────────────────────────────┘
                         │ HTTP/REST
┌────────────────────────▼─────────────────────────────┐
│                    BACKEND                            │
│         FastAPI + Python 3.11                        │
│                                                      │
│  /api/screen-cv          CV vs Job matching          │
│  /api/compare-candidates Multi-candidate ranking     │
│  /api/generate-questions Interview question gen      │
│  /api/detect-bias        Bias analysis               │
└──────────────────────────────────────────────────────┘
```

---

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- HuggingFace API Token (free)

### 1. Clone the Repository
```bash
git clone https://github.com/vishalhirani978/-HireIQ
cd HireIQ
```

### 2. Backend Setup
```bash
cd backend
pip install -r requirements.txt
```

### 3. Create .env file
```
HUGGINGFACE_TOKEN=your_token_here
```
Get your free token at: https://huggingface.co/settings/tokens

### 4. Start Backend
```bash
uvicorn main:app --reload --port 8000
```
API docs available at: http://localhost:8000/docs

### 5. Frontend Setup
```bash
cd frontend
npm install
npm start
```
App runs at: http://localhost:3000

### 6. Or Run Everything Together (Windows)
```bash
run.bat
```

---

## API Endpoints

### CV Screening
```http
POST /api/screen-cv
Content-Type: application/json

{
  "job_desc": "We need a Python developer with ML experience...",
  "cv_text": "Python developer with 3 years experience in ML..."
}
```

**Response:**
```json
{
  "percentage": 65.4,
  "matched_skills": ["Python", "Machine Learning", "Pandas"],
  "missing_skills": ["TensorFlow", "Deep Learning"],
  "recommendation": "MAYBE - 65.4% Match...",
  "ai_analysis": "Candidate partially meets requirements..."
}
```

### Compare Candidates
```http
POST /api/compare-candidates
Content-Type: application/json

{
  "job_desc": "Senior Python Developer...",
  "candidates": [
    {"name": "Ahmed Khan", "cv": "..."},
    {"name": "Sara Ali", "cv": "..."}
  ]
}
```

### Generate Interview Questions
```http
POST /api/generate-questions
Content-Type: application/json

{
  "job_desc": "Python Developer role...",
  "cv_text": "Ahmed Khan CV...",
  "difficulty": "Medium",
  "num_questions": 5
}
```

### Detect Bias
```http
POST /api/detect-bias
Content-Type: application/json

{
  "job_desc": "Looking for young energetic developer..."
}
```

---

## Project Structure
```
HireIQ/
├── backend/
│   ├── main.py              # FastAPI entry point
│   ├── routers/             # API route handlers
│   │   ├── cv_screening.py
│   │   ├── dashboard.py
│   │   ├── interview.py
│   │   └── bias_detector.py
│   ├── services/            # Business logic
│   │   ├── scorer.py
│   │   ├── bias_checker.py
│   │   └── question_gen.py
│   ├── models/              # Pydantic schemas
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/           # Page components
│   │   │   ├── Home.jsx
│   │   │   ├── CVScreening.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── InterviewQuestions.jsx
│   │   │   └── BiasDetector.jsx
│   │   ├── services/        # API service calls
│   │   └── styles/          # CSS files
│   └── package.json
│
├── components/              # Streamlit version
├── utils/                   # Shared utilities
├── app.py                   # Streamlit entry point
├── run.bat                  # Windows startup script
└── .env                     # API keys (not committed)
```

---

## Design System

| Color | Hex | Usage |
|---|---|---|
| Primary | #1E3A5F | Navigation, headers |
| Secondary | #2E86AB | Interactive elements |
| Accent | #00D4AA | Success states |
| Background | #0E1117 | Main background |
| Warning | #FFA500 | Caution indicators |
| Error | #FF4B4B | Error states |

---

## Why HireIQ?

Pakistani SMEs face unique challenges:
- No affordable AI hiring tools exist for the local market
- Bias in hiring affects diverse talent from being considered
- Manual screening is time consuming and inconsistent

HireIQ is built specifically for this market — completely free 
with no subscription required.

---

## Built For

**AI & Big Data Expo — Silicon Valley Hackathon 2026**

Theme: Transforming Enterprise Through AI

---

## Acknowledgments

- HuggingFace for providing free AI inference API
- Scikit-learn for machine learning utilities
- FastAPI for the excellent Python web framework
- React team for the modern UI library

---

## License

MIT License — Free to use and modify

---

<p align="center">
  <strong>Built with passion for Pakistani Businesses</strong>
  <br>
  <sub>Powered by AI and Hugging Face</sub>
</p>
```

---

## Key Changes I Made:

| Removed | Why |
|---|---|
| "80% time saved" | Fake metric |
| "95% accuracy" | Unproven claim |
| "Why HireIQ Wins" | Arrogant |
| Contributing guide | Unnecessary for hackathon |

| Added | Why |
|---|---|
| Pakistan badge | Shows local focus |
| Honest API response | Matches real output |
| Streamlit mention | Honest about both versions |
| Realistic claims | Judges will respect honesty |

