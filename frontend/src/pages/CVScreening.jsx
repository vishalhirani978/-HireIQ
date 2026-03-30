import React, { useState } from 'react';
import { screenCV } from '../services/api';

function CVScreening() {
  const [jobDesc, setJobDesc] = useState('');
  const [cvText, setCvText] = useState('');
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    if (!jobDesc || !cvText) {
      setError('Please paste both Job Description and CV to analyze.');
      return;
    }
    
    setLoading(true);
    setError('');
    setResults(null);
    
    try {
      const data = await screenCV(jobDesc, cvText);
      setResults(data);
    } catch (err) {
      setError('An error occurred. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <div className="page-header">
        <div className="page-header-wrapper">
          <div className="page-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
              <polyline points="14 2 14 8 20 8"></polyline>
            </svg>
          </div>
          <div>
            <h1 className="page-title">CV Screening</h1>
            <p className="page-subtitle">Analyze candidate qualifications against job requirements</p>
          </div>
        </div>
      </div>

      <div className="grid-2">
        <div className="card">
          <div className="card-header">
            <div className="card-icon secondary">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
              </svg>
            </div>
            <div>
              <h3 className="card-title">Job Description</h3>
              <p className="card-subtitle">Enter the role requirements</p>
            </div>
          </div>
          <textarea
            className="form-textarea"
            placeholder="e.g. We need a Python developer with 2 years experience in ML..."
            value={jobDesc}
            onChange={(e) => setJobDesc(e.target.value)}
            style={{ height: '200px' }}
          />
        </div>

        <div className="card">
          <div className="card-header">
            <div className="card-icon primary">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
            </div>
            <div>
              <h3 className="card-title">Candidate CV</h3>
              <p className="card-subtitle">Enter the candidate's resume</p>
            </div>
          </div>
          <textarea
            className="form-textarea"
            placeholder="e.g. John Doe, 3 years Python experience, worked on ML projects..."
            value={cvText}
            onChange={(e) => setCvText(e.target.value)}
            style={{ height: '200px' }}
          />
        </div>
      </div>

      <div style={{ textAlign: 'center', margin: '2rem 0' }}>
        <button className="btn btn-primary" onClick={handleSubmit} disabled={loading} style={{ maxWidth: '300px' }}>
          {loading ? 'Analyzing...' : 'Analyze Candidate'}
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
            <div className="page-header-wrapper">
              <div className="card-icon primary">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
              </div>
              <div>
                <h2 className="page-title">Screening Results</h2>
                <p className="page-subtitle">AI-powered candidate analysis</p>
              </div>
            </div>
          </div>

          <div className={`score-card ${results.score_class}`}>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', textTransform: 'uppercase', letterSpacing: '1px' }}>
              Match Score
            </p>
            <h1 className={`score-value ${results.score_class}`}>{results.percentage}%</h1>
            <div className={`score-label ${results.score_class}`}>{results.score_label}</div>
          </div>

          <div className="progress-container">
            <div className="progress-header">
              <span className="progress-label">Score Progress</span>
              <span style={{ color: results.score_color, fontWeight: 600 }}>{results.percentage}%</span>
            </div>
            <div className="progress-bar">
              <div className={`progress-fill ${results.score_class}`} style={{ width: `${results.percentage}%` }}></div>
            </div>
          </div>

          <div className="card" style={{ margin: '1.5rem 0' }}>
            <h3 style={{ marginBottom: '1rem' }}>Hiring Recommendation</h3>
            <p style={{ color: 'var(--text-secondary)', lineHeight: 1.7 }}>{results.recommendation}</p>
          </div>

          <div className="grid-2">
            <div className="card">
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '1rem' }}>
                <span style={{ color: 'var(--accent)', fontSize: '1.2rem' }}>&#9679;</span>
                <h4 className="card-title">Matched Skills</h4>
              </div>
              <div className="skills-container">
                {results.matched_skills && results.matched_skills.length > 0 ? (
                  results.matched_skills.map((skill, idx) => (
                    <span key={idx} className="skill-badge matched">{skill}</span>
                  ))
                ) : (
                  <p style={{ color: 'var(--text-secondary)' }}>No matched skills found.</p>
                )}
              </div>
            </div>

            <div className="card">
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '1rem' }}>
                <span style={{ color: 'var(--error)', fontSize: '1.2rem' }}>&#9679;</span>
                <h4 className="card-title">Missing Skills</h4>
              </div>
              <div className="skills-container">
                {results.missing_skills && results.missing_skills.length > 0 ? (
                  results.missing_skills.map((skill, idx) => (
                    <span key={idx} className="skill-badge missing">{skill}</span>
                  ))
                ) : (
                  <div className="alert success" style={{ margin: 0 }}>No missing skills - great candidate!</div>
                )}
              </div>
            </div>
          </div>

          <div className="card" style={{ marginTop: '1.5rem' }}>
            <div className="card-header">
              <div className="card-icon secondary" style={{ background: 'linear-gradient(135deg, var(--primary), var(--secondary))', width: '44px', height: '44px' }}>
                <span style={{ color: 'white', fontWeight: 700, fontSize: '0.9rem' }}>AI</span>
              </div>
              <div>
                <h3 className="card-title">AI Analysis</h3>
                <p className="card-subtitle">Detailed assessment</p>
              </div>
            </div>
            <p style={{ color: 'var(--text-secondary)', lineHeight: 1.75 }}>{results.ai_analysis}</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default CVScreening;
