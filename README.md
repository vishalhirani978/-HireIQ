# HireIQ - AI-Powered Hiring Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Next.js-16.2.4-black.svg" alt="Next.js">
  <img src="https://img.shields.io/badge/React-18.3.1-61DAFB.svg" alt="React">
  <img src="https://img.shields.io/badge/Recharts-2.15.4-blue.svg" alt="Recharts">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/Built%20For-Pakistan-009900.svg" alt="Pakistan">
</p>

> **HireIQ** is a free AI-powered hiring assistant built specifically
> for Pakistani startups and SMEs — making CV screening faster,
> fairer and smarter.

**Live Demo:** https://hire-iq-xi.vercel.app/
## Demo Video
[Watch HireIQ Demo on YouTube](https://youtu.be/jg04FcyjuoM)

---

## The Problem

Every Pakistani startup and SME faces the same hiring nightmare:

| Problem | Reality |
|---|---|
| Manual CV screening | Hours wasted on each position |
| Unconscious bias | Good candidates rejected unfairly |
| No scoring system | Subjective, inconsistent decisions |
| Expensive agencies | Budgets drained on recruitment fees |

**HireIQ solves all of this — for free.**

---

## Features

### CV Screening
- Paste any CV and job description
- AI calculates match score using TF-IDF algorithm
- Identifies exactly which skills match and which are missing
- Gives clear **Hire / Maybe / Reject** verdict

### Candidate Dashboard
- Compare up to 5 candidates simultaneously
- Visual bar chart with color-coded results
- Automatic ranking by match score
- Instant top candidate recommendation

### Interview Questions Generator
- Questions auto-generated from candidate skill gaps
- 3 difficulty levels: Easy, Medium, Hard
- Skill verification and behavioral questions included
- Customizable question count

### Bias Detector
- Scans job descriptions for 5 types of bias
- Calculates fairness score
- Provides specific improvement suggestions

---

## Demo

### Home Page
![Home Page](screenshots/home.png)

### CV Screening
![CV Screening](screenshots/cv_screening.png)

### Candidate Dashboard
![Dashboard](screenshots/dashboard.png)

### Bias Detector
![Bias Detector](screenshots/bias_detector.png)

---

## How It Works

All AI processing runs entirely in the browser — no backend needed:

```
┌─────────────────────────────────────────────────────┐
│                 FRONTEND                      │
│        Next.js 16 (Pages Router)              │
│          http://localhost:3000              │
│                                              │
│  TF-IDF Algorithm           → CV matching     │
│  Bias Detection Dictionary  → Bias analysis   │
│  Question Templates       → Question gen      │
└─────────────────────────────────────────────┘
```

---

## Tech Stack

| Technology | Version |
|---|---|
| Next.js | 16.2.4 |
| React | 18.3.1 |
| Recharts | 2.15.4 |
| Lucide React | 0.294.0 |
| Axios | 1.14.0 |
| Custom CSS | Dark theme |

---

## Scoring Algorithm

```
Match Score = (Skills Match × 70%) + (Text Similarity × 30%)

Skills Matching:
- Extracts 50+ technical and soft skills
- Compares against candidate CV
- Identifies matched and missing skills

Text Similarity:
- TF-IDF vectorization
- Cosine similarity calculation
- Normalized to 0-100% scale

Recommendation Thresholds:
- 70%+ = STRONG HIRE (Green)
- 40-69% = MAYBE (Orange)
- <40% = REJECT (Red)
```

---

## Bias Detection

Scans job descriptions for 5 types of bias:

| Bias Type | Examples | Severity |
|---|---|---|
| Age Bias | "young", "under 30", "recent graduate" | High |
| Gender Bias | "he must", "salesman", "manpower" | High |
| Origin Bias | "local only", "citizen only", "lahore based" | High |
| Appearance Bias | "attractive", "well groomed", "physically fit" | Medium |
| Exclusionary Language | "must be", "no exceptions", "specific religion" | Medium |

---

## Quick Start

### Prerequisites
- Node.js 18+

### Clone & Run

```bash
git clone https://github.com/vishalhirani978/-HireIQ
cd "-HireIQ/frontend"
npm install
npm start
```

### Deploy to Vercel (Recommended)

1. Push code to GitHub
2. Import project in Vercel
3. Deploy — that's it!

---

## Project Structure

```
HireIQ/
├── frontend/
│   ├── pages/                   # Next.js pages
│   │   ├── index.js           # Home
│   │   ├── cv-screening.js  # CV screening
│   │   ├── dashboard.js    # Compare candidates
│   │   ├── interview-questions.js
│   │   └── bias-detector.js
│   ├── src/
│   │   └── styles/
│   ├── lib/services/          # AI logic
│   ├── package.json
│   └── next.config.js
├── screenshots/               # Demo images
├── backend/                  # Optional legacy
├── components/              # Streamlit legacy
└── README.md
```

---

## Design System

| Color | Hex |
|---|---|
| Primary | #1E3A5F |
| Secondary | #2E86AB |
| Accent | #00D4AA |
| Background | #0E1117 |
| Surface | #161B22 |
| Warning | #FFA500 |
| Error | #FF4B4B |

---

## Why We Built This

Pakistan has 3.2 million registered SMEs — most of them still hire manually, subjectively and with unconscious bias.

No affordable AI hiring tool existed for this market.

So we built one.

HireIQ is completely free, requires no subscription and is built specifically for Pakistani businesses.

---

## Built For

**AI & Big Data Expo — Silicon Valley Hackathon 2026**

Theme: Transforming Enterprise Through AI

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

MIT License — Free to use, modify and distribute

---

<p align="center">
  <strong>Built with passion for Pakistani Businesses</strong>
</p>
