import React, { useState } from 'react';
import { generateQuestions } from '../services/api';

function InterviewQuestions() {
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
      const data = await generateQuestions(jobDesc, cvText, difficulty, numQuestions);
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
        <div className="form-group" style={{ marginBottom: 0 }}>
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
        <div className="form-group" style={{ marginBottom: 0 }}>
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

export default InterviewQuestions;
