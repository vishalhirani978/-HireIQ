/**
 * CV Screening Page Component
 * Analyzes candidate CVs against job descriptions
 */

import React, { useState } from 'react';
import Header from '../components/Header';
import { screenCV } from '../services/api';

/**
 * CVScreening Component
 * Allows users to input job description and candidate CV for analysis
 */
function CVScreening() {
  // State management
  const [jobDescription, setJobDescription] = useState('');
  const [candidateCV, setCandidateCV] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  /**
   * Handle form submission and API call
   */
  const handleAnalyze = async () => {
    // Validation
    if (!jobDescription.trim() || !candidateCV.trim()) {
      setError('Please enter both job description and candidate CV.');
      return;
    }

    // Reset states
    setLoading(true);
    setError('');
    setResult(null);

    // Make API call
    const response = await screenCV(jobDescription, candidateCV);
    
    setLoading(false);

    if (response.success) {
      setResult(response.data);
    } else {
      setError(response.error);
    }
  };

  /**
   * Get CSS class for score based on percentage
   */
  const getScoreClass = (score) => {
    if (score >= 70) return 'success';
    if (score >= 40) return 'warning';
    return 'danger';
  };

  /**
   * Get CSS class for verdict badge
   */
  const getVerdictClass = (recommendation) => {
    if (recommendation === 'STRONG HIRE') return 'success';
    if (recommendation === 'MAYBE') return 'warning';
    return 'danger';
  };

  return (
    <>
      <Header title="CV Screening" breadcrumb="CV Screening" />
      
      {/* Input Form Card */}
      <div className="card">
        <h2 className="card-title">Analyze Candidate</h2>
        
        {/* Job Description Input */}
        <div className="form-group">
          <label className="form-label">Job Description</label>
          <textarea
            className="form-textarea"
            placeholder="Enter the job description here..."
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            rows={5}
            disabled={loading}
          />
        </div>

        {/* Candidate CV Input */}
        <div className="form-group">
          <label className="form-label">Candidate CV</label>
          <textarea
            className="form-textarea"
            placeholder="Paste the candidate's CV here..."
            value={candidateCV}
            onChange={(e) => setCandidateCV(e.target.value)}
            rows={5}
            disabled={loading}
          />
        </div>

        {/* Submit Button */}
        <button 
          className="btn btn-primary" 
          onClick={handleAnalyze}
          disabled={loading}
        >
          {loading ? 'Analyzing...' : 'Analyze Candidate'}
        </button>

        {/* Error Message Display */}
        {error && (
          <div className="error-message">
            <span className="error-icon">!</span>
            {error}
          </div>
        )}
      </div>

      {/* Loading State */}
      {loading && (
        <div className="loading-container">
          <div className="spinner"></div>
          <p className="loading-text">Analyzing candidate profile...</p>
        </div>
      )}

      {/* Results Display */}
      {result && !loading && (
        <div className="result-card">
          {/* Results Header with Verdict */}
          <div className="result-header">
            <h2 className="card-title" style={{ marginBottom: 0 }}>
              Analysis Results
            </h2>
            <span className={`verdict-badge ${getVerdictClass(result.recommendation)}`}>
              {result.recommendation}
            </span>
          </div>

          {/* Score Display */}
          <div className="score-display">
            <div className={`score-percentage ${getScoreClass(result.percentage)}`}>
              {result.percentage}%
            </div>
            <div className="score-label">{result.score_label}</div>
            <div className="progress-bar">
              <div 
                className={`progress-fill ${getScoreClass(result.percentage)}`}
                style={{ width: `${result.percentage}%` }}
              />
            </div>
          </div>

          {/* Skills Comparison Grid */}
          <div style={{ 
            display: 'grid', 
            gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', 
            gap: '20px', 
            marginTop: '24px' 
          }}>
            {/* Matched Skills */}
            <div>
              <h3 style={{ fontSize: '14px', color: 'var(--text-secondary)', marginBottom: '12px' }}>
                Matched Skills ({result.matched_count})
              </h3>
              <div className="skill-badges">
                {result.matched_skills.length > 0 ? (
                  result.matched_skills.map((skill, idx) => (
                    <span key={idx} className="skill-badge matched">{skill}</span>
                  ))
                ) : (
                  <span style={{ fontSize: '13px', color: 'var(--text-secondary)' }}>
                    No matching skills found
                  </span>
                )}
              </div>
            </div>

            {/* Missing Skills */}
            <div>
              <h3 style={{ fontSize: '14px', color: 'var(--text-secondary)', marginBottom: '12px' }}>
                Missing Skills ({result.missing_count})
              </h3>
              <div className="skill-badges">
                {result.missing_skills.length > 0 ? (
                  result.missing_skills.map((skill, idx) => (
                    <span key={idx} className="skill-badge missing">{skill}</span>
                  ))
                ) : (
                  <span style={{ fontSize: '13px', color: 'var(--success)' }}>
                    All required skills matched
                  </span>
                )}
              </div>
            </div>
          </div>

          {/* AI Analysis Section */}
          {result.ai_analysis && (
            <div className="ai-analysis">
              <div className="ai-analysis-title">
                <span>&#10024;</span> AI Analysis
              </div>
              <p className="ai-analysis-text">{result.ai_analysis}</p>
            </div>
          )}
        </div>
      )}
    </>
  );
}

export default CVScreening;
