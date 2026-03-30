# HireIQ - AI-Powered Hiring Assistant

An intelligent hiring assistant that helps Pakistani startups and SMEs screen candidates faster, fairer, and smarter.

## Features

- **CV Screening** - AI-powered candidate analysis against job descriptions
- **Candidate Dashboard** - Compare multiple candidates with visual charts
- **Interview Questions** - Auto-generate smart questions based on skill gaps
- **Bias Detector** - Ensure fair and inclusive job descriptions

## Tech Stack

### Frontend
- React 18
- React Router
- Axios
- Recharts
- Custom CSS (no Tailwind)

### Backend
- FastAPI
- Python 3.11
- Hugging Face Hub
- Scikit-learn

## Setup Instructions

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## Environment Variables

Create a `.env` file in the backend directory:

```
HUGGINGFACE_TOKEN=your_token_here
```

## API Endpoints

- `POST /api/screen-cv` - Screen a candidate CV
- `POST /api/compare-candidates` - Compare multiple candidates
- `POST /api/generate-questions` - Generate interview questions
- `POST /api/detect-bias` - Detect bias in job descriptions

## Color Scheme

- Primary: #1E3A5F (dark navy)
- Secondary: #2E86AB (teal)
- Accent: #00D4AA (mint green)
- Background: #0E1117 (dark)
- Success: #00D4AA
- Warning: #FFA500
- Error: #FF4B4B

## License

MIT
