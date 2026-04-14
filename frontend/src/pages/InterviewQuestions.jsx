/**
 * Interview Questions Page Component
 * Generates tailored interview questions based on job and candidate
 */

import React, { useState } from 'react';
import Header from '../components/Header';
import { generateQuestions } from '../services/api';

/**
 * InterviewQuestions Component
 * Creates interview questions with skill gap analysis
 */
function InterviewQuestions() {
  // State management
  const [jobDescription, setJobDescription] = useState('');
  const [candidateCV, setCandidateCV] = useState('');
  const [difficulty, setDifficulty] = useState('Medium');
  const [numQuestions, setNumQuestions] = useState(5);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  /**
   * Handle form submission and API call
   */
  const handleGenerate = async () => {
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
    const response = await generateQuestions(jobDescription, candidateCV, difficulty, numQuestions);
    
    setLoading(false);

    if (response.success) {
      setResult(response.data);
    } else {
      setError(response.error);
    }
  };

  /**
   * Get CSS class for difficulty badge
   */
  const getDifficultyBadgeClass = () => {
    if (difficulty === 'Easy') return 'verify';
    if (difficulty === 'Medium') return 'difficulty';
    return 'gap';
  };

  // Calculate total questions generated
  let totalGenerated = 0;
  if (result) {
    totalGenerated = (result.gap_questions?.length || 0) + 
                     (result.verify_questions?.length || 0) + 
                     (result.difficulty_questions?.length || 0);
  }

  return (
    <>
      <Header title="Interview Questions" breadcrumb="Interview Questions" />
      
      {/* Input Form Card */}
      <div className="card">
        <h2 className="card-title">Generate Interview Questions</h2>
        
        {/* Job Description Input */}
        <div className="form-group">
          <label className="form-label">Job Description</label>
          <textarea
            className="form-textarea"
            placeholder="Enter the job description here..."
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            rows={4}
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
            rows={4}
            disabled={loading}
          />
        </div>

        {/* Options Grid */}
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', 
          gap: '20px' 
        }}>
          {/* Difficulty Selector */}
          <div className="form-group">
            <label className="form-label">Question Difficulty</label>
            <select
              className="form-select"
              value={difficulty}
              onChange={(e) => setDifficulty(e.target.value)}
              disabled={loading}
            >
              <option value="Easy">Easy</option>
              <option value="Medium">Medium</option>
              <option value="Hard">Hard</option>
            </select>
          </div>

          {/* Number of Questions Selector */}
          <div className="form-group">
            <label className="form-label">Number of Questions (3-10)</label>
            <select
              className="form-select"
              value={numQuestions}
              onChange={(e) => setNumQuestions(parseInt(e.target.value))}
              disabled={loading}
            >
              {[3, 4, 5, 6, 7, 8, 9, 10].map(n => (
                <option key={n} value={n}>{n} Questions</option>
              ))}
            </select>
          </div>
        </div>

        {/* Submit Button */}
        <button 
          className="btn btn-primary" 
          onClick={handleGenerate}
          disabled={loading}
        >
          {loading ? 'Generating...' : 'Generate Interview Questions'}
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
          <p className="loading-text">Generating tailored interview questions...</p>
        </div>
      )}

      {/* Results Display */}
      {result && !loading && (
        <div className="card">
          {/* Results Header */}
          <div className="result-header">
            <h2 className="card-title" style={{ marginBottom: 0 }}>
              Generated Questions
            </h2>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <span style={{ fontSize: '14px', color: 'var(--text-secondary)' }}>
                Total: {totalGenerated} questions
              </span>
              <span className={`question-category ${getDifficultyBadgeClass()}`}>
                {difficulty}
              </span>
            </div>
          </div>

          {/* Questions Grid - Three Columns */}
          <div className="questions-grid">
            {/* Skill Gap Questions Column */}
            <div>
              <h3 style={{ 
                fontSize: '14px', 
                color: 'var(--error)', 
                marginBottom: '12px',
                display: 'flex',
                alignItems: 'center',
                gap: '8px'
              }}>
                <span>&#9888;</span> Skill Gap Questions ({result.gap_count})
              </h3>
              {result.gap_questions?.length > 0 ? (
                result.gap_questions.map((q, idx) => (
                  <div key={`gap-${idx}`} className="question-card gap">
                    <div className="question-header">
                      <span className="question-number">Q{idx + 1}</span>
                      <span className="question-category gap">Gap</span>
                    </div>
                    <p className="question-text">{q}</p>
                  </div>
                ))
              ) : (
                <p style={{ fontSize: '13px', color: 'var(--text-secondary)' }}>
                  No skill gaps identified
                </p>
              )}
            </div>

            {/* Skill Verification Questions Column */}
            <div>
              <h3 style={{ 
                fontSize: '14px', 
                color: 'var(--success)', 
                marginBottom: '12px',
                display: 'flex',
                alignItems: 'center',
                gap: '8px'
              }}>
                <span>&#10004;</span> Skill Verification ({result.verify_count})
              </h3>
              {result.verify_questions?.length > 0 ? (
                result.verify_questions.map((q, idx) => (
                  <div key={`verify-${idx}`} className="question-card verify">
                    <div className="question-header">
                      <span className="question-number">
                        Q{result.gap_count + idx + 1}
                      </span>
                      <span className="question-category verify">Verify</span>
                    </div>
                    <p className="question-text">{q}</p>
                  </div>
                ))
              ) : (
                <p style={{ fontSize: '13px', color: 'var(--text-secondary)' }}>
                  No matching skills to verify
                </p>
              )}
            </div>

            {/* Difficulty Level Questions Column */}
            <div>
              <h3 style={{ 
                fontSize: '14px', 
                color: 'var(--warning)', 
                marginBottom: '12px',
                display: 'flex',
                alignItems: 'center',
                gap: '8px'
              }}>
                <span>&#9878;</span> Difficulty Level ({result.difficulty_count})
              </h3>
              {result.difficulty_questions?.length > 0 ? (
                result.difficulty_questions.map((q, idx) => (
                  <div key={`diff-${idx}`} className="question-card difficulty">
                    <div className="question-header">
                      <span className="question-number">
                        Q{result.gap_count + result.verify_count + idx + 1}
                      </span>
                      <span className="question-category difficulty">Level</span>
                    </div>
                    <p className="question-text">{q}</p>
                  </div>
                ))
              ) : (
                <p style={{ fontSize: '13px', color: 'var(--text-secondary)' }}>
                  No difficulty questions generated
                </p>
              )}
            </div>
          </div>
        </div>
      )}
    </>
  );
}

export default InterviewQuestions;
