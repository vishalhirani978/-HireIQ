import React, { useState } from 'react';
import { detectBias } from '../services/api';

function BiasDetector() {
  const [jobDesc, setJobDesc] = useState('');
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState('');
  const [expandedBias, setExpandedBias] = useState(null);

  const handleSubmit = async () => {
    if (!jobDesc) {
      setError('Please paste a job description first');
      return;
    }
    
    setLoading(true);
    setError('');
    setResults(null);
    
    try {
      const data = await detectBias(jobDesc);
      setResults(data);
    } catch (err) {
      setError('An error occurred. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const toggleBias = (biasType) => {
    setExpandedBias(expandedBias === biasType ? null : biasType);
  };

  const getProgressColor = () => {
    if (!results) return 'var(--text-secondary)';
    if (results.fairness_score >= 80) return 'var(--accent)';
    if (results.fairness_score >= 60) return 'var(--warning)';
    return 'var(--error)';
  };

  const getProgressClass = () => {
    if (!results) return '';
    if (results.fairness_score >= 80) return 'high';
    if (results.fairness_score >= 60) return 'medium';
    return 'low';
  };

  return (
    <div>
      <div className="page-header">
        <div className="page-header-wrapper">
          <div className="page-icon" style={{ background: 'linear-gradient(135deg, rgba(255,165,0,0.2), rgba(255,165,0,0.1))', borderColor: 'rgba(255,165,0,0.3)' }}>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
            </svg>
          </div>
          <div>
            <h1 className="page-title">Bias Detector</h1>
            <p className="page-subtitle">Detect biased language in job descriptions to ensure fair hiring</p>
          </div>
        </div>
      </div>

      <div className="card">
        <div className="card-header">
          <div className="card-icon" style={{ background: 'rgba(255, 165, 0, 0.15)', color: 'var(--warning)' }}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
            </svg>
          </div>
          <div>
            <h3 className="card-title">Job Description Analysis</h3>
          </div>
        </div>
        <textarea
          className="form-textarea"
          placeholder="Paste your job description here..."
          value={jobDesc}
          onChange={(e) => setJobDesc(e.target.value)}
          style={{ height: '200px' }}
        />
      </div>

      <div style={{ textAlign: 'center', margin: '2rem 0' }}>
        <button className="btn btn-primary" onClick={handleSubmit} disabled={loading} style={{ maxWidth: '300px' }}>
          {loading ? 'Detecting...' : 'Detect Bias'}
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
              Analysis Results
            </h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
              Comprehensive bias detection report
            </p>
          </div>

          <div className="metrics-grid">
            <div className="metric-card">
              <div className="metric-label">Fairness Score</div>
              <div className="metric-value">{results.fairness_score}%</div>
            </div>
            <div className="metric-card">
              <div className="metric-label">Bias Types Found</div>
              <div className="metric-value" style={{ color: 'var(--error)' }}>{results.biased_count}</div>
            </div>
            <div className="metric-card">
              <div className="metric-label">Clean Categories</div>
              <div className="metric-value" style={{ color: 'var(--accent)' }}>{results.clean_count}</div>
            </div>
          </div>

          <div className="progress-container">
            <div className="progress-header">
              <span className="progress-label">Bias-Free Progress</span>
              <span style={{ color: getProgressColor(), fontWeight: 600 }}>{results.fairness_score}%</span>
            </div>
            <div className="progress-bar">
              <div className={`progress-fill ${getProgressClass()}`} style={{ width: `${results.fairness_score}%` }}></div>
            </div>
            <p style={{ color: getProgressColor(), marginTop: '1rem', fontWeight: 500 }}>
              {results.progress_message}
            </p>
          </div>

          <hr className="divider" />

          {results.found_biases && Object.keys(results.found_biases).length > 0 ? (
            <>
              <div className="page-header">
                <h3 style={{ fontSize: '1.2rem', fontWeight: 600, marginBottom: '0.25rem' }}>
                  <span style={{ color: 'var(--error)' }}>&#9679;</span> Bias Detected
                </h3>
                <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
                  {Object.keys(results.found_biases).length} issue(s) found that should be addressed
                </p>
              </div>

              {Object.entries(results.found_biases).map(([biasType, data]) => (
                <div key={biasType} className={`expander ${expandedBias === biasType ? 'active' : ''}`}>
                  <div className="expander-header" onClick={() => toggleBias(biasType)}>
                    <span>
                      {biasType} - Found: {data.words.slice(0, 3).join(', ')}
                      {data.words.length > 3 ? '...' : ''}
                    </span>
                    <span>&#9660;</span>
                  </div>
                  <div className="expander-content">
                    <p style={{ color: 'var(--text-secondary)', fontSize: '0.85rem', textTransform: 'uppercase', letterSpacing: '0.5px', marginBottom: '0.5rem' }}>
                      Biased Words
                    </p>
                    <div className="skills-container">
                      {data.words.map((word, idx) => (
                        <span key={idx} className="bias-word">{word}</span>
                      ))}
                    </div>
                    <div className="suggestion-box">
                      <p style={{ color: 'var(--accent)', fontWeight: 600, fontSize: '0.85rem', textTransform: 'uppercase', letterSpacing: '0.5px', marginBottom: '0.5rem' }}>
                        &#8594; Suggestion
                      </p>
                      <p style={{ color: 'var(--text-secondary)', lineHeight: 1.6 }}>{data.suggestion}</p>
                    </div>
                  </div>
                </div>
              ))}
            </>
          ) : (
            <div className="card" style={{ textAlign: 'center', padding: '3rem' }}>
              <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>
                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" strokeWidth="2" style={{ margin: '0 auto' }}>
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
              </div>
              <h3 style={{ color: 'var(--accent)', margin: '0 0 0.5rem 0' }}>No Bias Detected</h3>
              <p style={{ color: 'var(--text-secondary)', margin: 0 }}>This is a fair and inclusive job description</p>
            </div>
          )}

          <hr className="divider" />

          <div className="page-header">
            <h3 style={{ fontSize: '1.2rem', fontWeight: 600, marginBottom: '0.25rem' }}>
              <span style={{ color: 'var(--accent)' }}>&#9679;</span> Clean Categories
            </h3>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
              Categories that passed bias checks
            </p>
          </div>

          {results.clean_categories && results.clean_categories.map((cat, idx) => (
            <div key={idx} className="clean-item">
              <span style={{ color: 'var(--accent)', fontSize: '1.2rem' }}>&#9679;</span>
              <span>{cat}</span>
              <span className="clean-status">No bias detected</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default BiasDetector;
