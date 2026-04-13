import React, { useState } from 'react';

const SKILLS_LIST = [
  "python", "sql", "java", "javascript", "typescript",
  "machine learning", "ml", "data science", "pandas", "numpy",
  "scikit-learn", "tensorflow", "keras", "pytorch", "deep learning",
  "nlp", "natural language processing", "react", "nodejs", "angular",
  "vue", "html", "css", "django", "flask", "fastapi",
  "excel", "powerpoint", "tableau", "power bi", "aws", "azure",
  "docker", "kubernetes", "git", "linux", "sql server",
  "mongodb", "postgresql", "mysql", "redis", "elasticsearch",
  "communication", "teamwork", "leadership", "problem solving",
  "management", "analysis", "project management", "agile", "scrum"
];

function extractSkills(text) {
  const found = [];
  const textLower = text.toLowerCase();
  for (const skill of SKILLS_LIST) {
    if (textLower.includes(skill)) {
      found.push(skill);
    }
  }
  return [...new Set(found)];
}

const EASY_QUESTIONS = [
  "Tell me about yourself and your professional background.",
  "Why are you interested in this position and our company?",
  "What are your key strengths that make you a good fit?",
  "Where do you see yourself in 5 years?",
  "Why are you leaving your current job?",
  "Describe your ideal work environment.",
  "What motivates you to do your best work?"
];

const MEDIUM_QUESTIONS = [
  "Describe a challenging problem you solved and how you approached it.",
  "How do you stay updated with the latest technologies in your field?",
  "Tell me about a time you worked in a team under pressure.",
  "How do you handle tight deadlines and multiple priorities?",
  "Describe a situation where you had to learn something quickly.",
  "Tell me about a project you're most proud of.",
  "How do you approach debugging or troubleshooting issues?"
];

const HARD_QUESTIONS = [
  "Design a scalable system for processing 1 million records daily.",
  "How would you handle model drift in a production environment?",
  "Explain the trade-offs between precision and recall in your last project.",
  "How would you architect a real-time recommendation system?",
  "What strategies would you use to reduce overfitting in a deep learning model?",
  "Describe your experience with MLOps and deployment pipelines.",
  "How would you optimize a slow-performing database query?"
];

const SKILL_TEMPLATES = [
  "Tell me about a specific project where you used {skill}. What was the outcome?",
  "How confident are you with {skill} on a scale of 1-10? Give an example.",
  "What is the most complex task you have done using {skill}?",
  "How long have you been working with {skill} and what have you built?",
  "What challenges did you face while using {skill} and how did you solve them?"
];

function generateQuestions(matchedSkills, missingSkills, difficulty, numQuestions) {
  const gapCount = Math.min(missingSkills.length, Math.max(1, Math.floor(numQuestions / 3)));
  const verifyCount = Math.min(matchedSkills.length, Math.max(1, Math.floor(numQuestions / 3)));
  const difficultyCount = numQuestions - gapCount - verifyCount;
  
  const gapQuestions = missingSkills.slice(0, gapCount).map(skill =>
    `You listed ${skill} as a requirement. Can you walk us through your experience with ${skill} and explain how you've applied it in your work?`
  );
  
  const verifyQuestions = matchedSkills.slice(0, verifyCount).map((skill, i) => {
    const template = SKILL_TEMPLATES[i % SKILL_TEMPLATES.length];
    return template.replace('{skill}', skill);
  });
  
  let difficultyQuestions;
  if (difficulty === "Easy") {
    difficultyQuestions = EASY_QUESTIONS;
  } else if (difficulty === "Medium") {
    difficultyQuestions = MEDIUM_QUESTIONS;
  } else {
    difficultyQuestions = HARD_QUESTIONS;
  }
  
  return {
    gap_questions: gapQuestions,
    verify_questions: verifyQuestions,
    difficulty_questions: difficultyQuestions.slice(0, difficultyCount),
    gap_count: gapCount,
    verify_count: verifyCount,
    difficulty_count: difficultyCount,
    total: gapCount + verifyCount + difficultyCount
  };
}

export default function InterviewQuestions() {
  const [jobDesc, setJobDesc] = useState('');
  const [cvText, setCvText] = useState('');
  const [difficulty, setDifficulty] = useState('Medium');
  const [numQuestions, setNumQuestions] = useState(5);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    if (!jobDesc || !cvText) {
      setError('Please paste both Job Description and CV');
      return;
    }
    
    setLoading(true);
    setError('');
    setResults(null);
    
    try {
      await new Promise(r => setTimeout(r, 500));
      
      const jobSkills = extractSkills(jobDesc);
      const cvSkills = extractSkills(cvText);
      const matchedSkills = cvSkills.filter(s => jobSkills.includes(s));
      const missingSkills = jobSkills.filter(s => !cvSkills.includes(s));
      
      const data = generateQuestions(matchedSkills, missingSkills, difficulty, numQuestions);
      setResults(data);
    } catch (err) {
      setError('An error occurred. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const getDifficultyColor = () => {
    switch (difficulty) {
      case 'Easy': return 'var(--accent)';
      case 'Medium': return 'var(--warning)';
      case 'Hard': return 'var(--error)';
      default: return 'var(--text-secondary)';
    }
  };

  return (
    <div>
      <div className="page-header">
        <div className="page-header-wrapper">
          <div className="page-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <circle cx="12" cy="12" r="10"></circle>
              <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
              <line x1="12" y1="17" x2="12.01" y2="17"></line>
            </svg>
          </div>
          <div>
            <h1 className="page-title">Interview Questions Generator</h1>
            <p className="page-subtitle">Generate smart interview questions based on job requirements and candidate gaps</p>
          </div>
        </div>
      </div>

      <div className="grid-2">
        <div className="card">
          <div className="card-header">
            <div className="card-icon secondary">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
              </svg>
            </div>
            <div>
              <h3 className="card-title">Job Description</h3>
            </div>
          </div>
          <textarea
            className="form-textarea"
            placeholder="e.g. We need a Python developer with ML experience..."
            value={jobDesc}
            onChange={(e) => setJobDesc(e.target.value)}
            style={{ height: '180px' }}
          />
        </div>

        <div className="card">
          <div className="card-header">
            <div className="card-icon secondary">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
            </div>
            <div>
              <h3 className="card-title">Candidate CV</h3>
            </div>
          </div>
          <textarea
            className="form-textarea"
            placeholder="e.g. Ahmed Khan, Python developer, 2 years experience..."
            value={cvText}
            onChange={(e) => setCvText(e.target.value)}
            style={{ height: '180px' }}
          />
        </div>
      </div>

      <hr className="divider" />

      <div className="grid-2" style={{ maxWidth: '500px', margin: '0 auto' }}>
        <div className="form-group">
          <label className="form-label">Question Difficulty</label>
          <select
            className="form-select"
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value)}
          >
            <option value="Easy">Easy</option>
            <option value="Medium">Medium</option>
            <option value="Hard">Hard</option>
          </select>
        </div>
        <div className="form-group">
          <label className="form-label">Number of Questions</label>
          <select
            className="form-select"
            value={numQuestions}
            onChange={(e) => setNumQuestions(parseInt(e.target.value))}
          >
            <option value={3}>3 Questions</option>
            <option value={5}>5 Questions</option>
            <option value={7}>7 Questions</option>
            <option value={10}>10 Questions</option>
          </select>
        </div>
      </div>

      <div style={{ textAlign: 'center', margin: '2rem 0' }}>
        <button className="btn btn-primary" onClick={handleSubmit} disabled={loading} style={{ maxWidth: '300px' }}>
          {loading ? 'Generating...' : 'Generate Interview Questions'}
        </button>
      </div>

      {loading && (
        <div className="spinner">
          <div className="spinner-ring"></div>
        </div>
      )}

      {error && (
        <div className="alert warning">
          <span>{error}</span>
        </div>
      )}

      {results && (
        <div>
          <hr className="divider" />

          <div className="page-header">
            <h2 style={{ fontSize: '1.5rem', fontWeight: 600, marginBottom: '0.25rem' }}>
              Generated Questions
            </h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
              Total: {results.total} questions | Difficulty: {difficulty}
            </p>
          </div>

          {results.gap_questions && results.gap_questions.length > 0 && (
            <div className="question-section gap">
              <div className="question-header">
                <span style={{ color: 'var(--error)', fontSize: '1.2rem' }}>&#9679;</span>
                <h3 className="question-title">Skill Gap Questions</h3>
                <span className="question-count gap">{results.gap_count}</span>
              </div>
              {results.gap_questions.map((q, idx) => (
                <div key={idx} className="question-card">
                  <span style={{ color: 'var(--error)', fontWeight: 600, marginRight: '0.5rem' }}>
                    Q{idx + 1}.
                  </span>
                  {q}
                </div>
              ))}
            </div>
          )}

          {results.verify_questions && results.verify_questions.length > 0 && (
            <div className="question-section verify">
              <div className="question-header">
                <span style={{ color: 'var(--accent)', fontSize: '1.2rem' }}>&#9679;</span>
                <h3 className="question-title">Skill Verification Questions</h3>
                <span className="question-count verify">{results.verify_count}</span>
              </div>
              {results.verify_questions.map((q, idx) => (
                <div key={idx} className="question-card">
                  <span style={{ color: 'var(--accent)', fontWeight: 600, marginRight: '0.5rem' }}>
                    Q{idx + 1}.
                  </span>
                  {q}
                </div>
              ))}
            </div>
          )}

          {results.difficulty_questions && results.difficulty_questions.length > 0 && (
            <div className="question-section difficulty">
              <div className="question-header">
                <span style={{ color: getDifficultyColor(), fontSize: '1.2rem' }}>&#9679;</span>
                <h3 className="question-title">{difficulty} Level Questions</h3>
                <span className="question-count difficulty">{results.difficulty_count}</span>
              </div>
              {results.difficulty_questions.map((q, idx) => (
                <div key={idx} className="question-card">
                  <span style={{ color: getDifficultyColor(), fontWeight: 600, marginRight: '0.5rem' }}>
                    Q{idx + 1}.
                  </span>
                  {q}
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}