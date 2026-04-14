/**
 * Bias Detector Page Component
 * Analyzes job descriptions for unconscious bias
 */

import React, { useState } from 'react';
import Header from '../components/Header';
import { detectBias } from '../services/api';

/**
 * BiasDetector Component
 * Detects and reports bias in job descriptions
 */
function BiasDetector() {
  // State management
  const [jobDescription, setJobDescription] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  /**
   * Handle form submission and API call
   */
  const handleDetect = async () => {
    // Validation
    if (!jobDescription.trim()) {
      setError('Please enter a job description.');
      return;
    }

    // Reset states
    setLoading(true);
    setError('');
    setResult(null);

    // Make API call
    const response = await detectBias(jobDescription);
    
    setLoading(false);

    if (response.success) {
      setResult(response.data);
    } else {
      setError(response.error);
    }
  };

  /**
   * Get CSS class for fairness score
   */
  const getScoreClass = (score) => {
    if (score >= 80) return 'success';
    if (score >= 60) return 'warning';
    return 'danger';
  };

  /**
   * Get verdict text based on fairness score
   */
  const getVerdictText = (score) => {
    if (score >= 80) return 'Largely bias-free';
    if (score >= 60) return 'Some bias detected';
    return 'Significant bias - major revision needed';
  };

  // All bias categories to check
  const allBiasTypes = [
    'Age Bias',
    'Gender Bias',
    'Origin Bias',
    'Appearance Bias',
    'Exclusionary Language'
  ];

  return (
    <>
      <Header title="Bias Detector" breadcrumb="Bias Detector" />
      
      {/* Input Form Card */}
      <div className="card">
        <h2 className="card-title">Detect Bias in Job Description</h2>
        
        {/* Job Description Input */}
        <div className="form-group">
          <label className="form-label">Job Description</label>
          <textarea
            className="form-textarea"
            placeholder="Enter the job description to analyze for bias..."
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            rows={6}
            disabled={loading}
          />
        </div>

        {/* Submit Button */}
        <button 
          className="btn btn-primary" 
          onClick={handleDetect}
          disabled={loading}
        >
          {loading ? 'Analyzing...' : 'Detect Bias'}
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
          <p className="loading-text">Analyzing job description for bias...</p>
        </div>
      )}

      {/* Results Display */}
      {result && !loading && (
        <>
          {/* Metrics Cards */}
          <div className="metrics-grid">
            <div className="metric-card">
              <div className={`metric-value ${getScoreClass(result.fairness_score)}`}>
                {result.fairness_score}%
              </div>
              <div className="metric-label">Fairness Score</div>
            </div>
            <div className="metric-card">
              <div className="metric-value danger">{result.biased_count}</div>
              <div className="metric-label">Bias Types Found</div>
            </div>
            <div className="metric-card">
              <div className="metric-value success">{result.clean_count}</div>
              <div className="metric-label">Clean Categories</div>
            </div>
          </div>

          {/* Overall Assessment Card */}
          <div className="card">
            <div className="result-header">
              <h2 className="card-title" style={{ marginBottom: 0 }}>
                Bias Analysis Results
              </h2>
              <div style={{
                padding: '8px 16px',
                backgroundColor: result.fairness_score >= 80 
                  ? 'rgba(0, 212, 170, 0.2)' 
                  : result.fairness_score >= 60 
                    ? 'rgba(255, 165, 0, 0.2)' 
                    : 'rgba(255, 75, 75, 0.2)',
                borderRadius: '6px',
                fontSize: '14px',
                fontWeight: 600,
                color: result.fairness_score >= 80 
                  ? 'var(--success)' 
                  : result.fairness_score >= 60 
                    ? 'var(--warning)' 
                    : 'var(--error)'
              }}>
                {getVerdictText(result.fairness_score)}
              </div>
            </div>

            {/* Progress Bar */}
            <div className="progress-bar" style={{ marginTop: '16px' }}>
              <div 
                className={`progress-fill ${getScoreClass(result.fairness_score)}`}
                style={{ width: `${result.fairness_score}%` }}
              />
            </div>
            <p style={{ fontSize: '12px', color: 'var(--text-secondary)', marginTop: '8px' }}>
              Fairness percentage: {result.fairness_score}% of categories are bias-free
            </p>
          </div>

          {/* Bias Details Cards */}
          <div>
            {allBiasTypes.map((biasType) => {
              const biasData = result.found_biases?.[biasType];
              const isFound = !!biasData;
              
              return (
                <div key={biasType} className={`bias-card ${isFound ? 'found' : 'clean'}`}>
                  <div className="bias-header">
                    <span className="bias-icon">
                      {isFound ? '\u2716' : '\u2714'}
                    </span>
                    <span className="bias-name">{biasType}</span>
                  </div>
                  
                  {/* If bias found, show details */}
                  {isFound ? (
                    <>
                      <div className="skill-badges">
                        {biasData.words.map((word, idx) => (
                          <span key={idx} className="skill-badge missing">{word}</span>
                        ))}
                      </div>
                      <p className="bias-suggestion">
                        <strong>Suggestion:</strong> {biasData.suggestion}
                      </p>
                    </>
                  ) : (
                    <p style={{ fontSize: '13px', color: 'var(--success)' }}>
                      No {biasType.toLowerCase()} detected - Good job!
                    </p>
                  )}
                </div>
              );
            })}
          </div>
        </>
      )}
    </>
  );
}

export default BiasDetector;
