# HireIQ - Vercel Deployment Guide

## Prerequisites
- Node.js 18+
- Vercel account
- HuggingFace API token (free)

## Deployment Steps

### 1. Get HuggingFace Token
1. Go to https://huggingface.co/settings/tokens
2. Create a new token (read access is sufficient)
3. Copy the token

### 2. Deploy to Vercel

**Option A: Deploy via Vercel CLI**
```bash
cd frontend
npm install -g vercel
vercel login
vercel
```
Follow the prompts. When asked for environment variables, add:
- Name: `HUGGINGFACE_TOKEN`
- Value: your HuggingFace token

**Option B: Deploy via GitHub**
1. Push this project to GitHub
2. Go to https://vercel.com/new
3. Import the repository
4. Add environment variable:
   - Name: `HUGGINGFACE_TOKEN`
   - Value: your HuggingFace token
5. Click Deploy

### 3. Configure Environment Variables on Vercel

If deploying via GitHub or need to update later:
1. Go to your Vercel dashboard
2. Select your project
3. Go to Settings > Environment Variables
4. Add:
   - Name: `HUGGINGFACE_TOKEN`
   - Value: hf_xxxxxxxxxxxxx

### 4. Rebuild (if needed)

After adding environment variables:
1. Go to Deployments
2. Click the three dots on the latest deployment
3. Select "Redeploy"

## Local Development

```bash
cd frontend
npm install
npm run dev
```

## Project Structure (Frontend)

```
frontend/
├── pages/
│   ├── api/
│   │   ├── screen-cv/route.js
│   │   ├── compare-candidates/route.js
│   │   ├── generate-questions/route.js
│   │   └── detect-bias/route.js
│   ├── index.js
│   ├── cv-screening.js
│   ├── dashboard.js
│   ├── interview-questions.js
│   └── bias-detector.js
├── components/
│   └── Layout.js
├── lib/
│   └── services/
│       ├── scorer.js
│       ├── biasChecker.js
│       └── questionGen.js
├── services/
│   └── api.js
├── styles/
│   └── global.css
└── package.json
```

## Features

- **CV Screening**: AI-powered candidate analysis using TF-IDF
- **Candidate Dashboard**: Compare up to 5 candidates
- **Bias Detector**: Detect biased language in job descriptions
- **Interview Questions**: Generate questions based on skills gaps

## Tech Stack

- Next.js 14 (App Router)
- React 18
- Recharts
- HuggingFace API (BART-large-CNN)
