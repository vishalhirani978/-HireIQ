/**
 * Dashboard Page Component
 * Compares multiple candidates against a job description
 */

import React, { useState } from 'react';
import Header from '../components/Header';
import { compareCandidates } from '../services/api';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from 'recharts';

/**
 * Dashboard Component
 * Allows comparing 2-5 candidates with visual analytics
 */
function Dashboard() {
  // State management
  const [jobDescription, setJobDescription] = useState('');
  const [numCandidates, setNumCandidates] = useState(2);
  const [candidates, setCandidates] = useState([
    { name: '', cv: '' },
    { name: '', cv: '' }
  ]);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState('');

  /**
   * Update number of candidate inputs
   */
  const handleNumChange = (num) => {
    const newNum = Math.max(2, Math.min(5, num));
    setNumCandidates(newNum);
    
    const newCandidates = [...candidates];
    while (newCandidates.length < newNum) {
      newCandidates.push({ name: '', cv: '' });
    }
    while (newCandidates.length > newNum) {
      newCandidates.pop();
    }
    setCandidates(newCandidates);
  };

  /**
   * Update candidate input field
   */
  const handleCandidateChange = (index, field, value) => {
    const newCandidates = [...candidates];
    newCandidates[index][field] = value;
    setCandidates(newCandidates);
  };

  /**
   * Handle form submission and API call
   */
  const handleCompare = async () => {
    // Validation
    if (!jobDescription.trim()) {
      setError('Please enter a job description.');
      return;
    }

    const validCandidates = candidates.filter(c => c.name.trim() && c.cv.trim());
    if (validCandidates.length < 2) {
      setError('Please enter at least 2 candidates with name and CV.');
      return;
    }

    // Reset states
    setLoading(true);
    setError('');
    setResults(null);

    // Make API call
    const response = await compareCandidates(jobDescription, validCandidates);
    
    setLoading(false);

    if (response.success) {
      setResults(response.data);
    } else {
      setError(response.error);
    }
  };

  /**
   * Get color for score visualization
   */
  const getScoreColor = (score) => {
    if (score >= 70) return '#00D4AA';
    if (score >= 40) return '#FFA500';
    return '#FF4B4B';
  };

  /**
   * Get CSS class for verdict badge
   */
  const getVerdictClass = (verdict) => {
    if (verdict === 'STRONG HIRE') return 'success';
    if (verdict === 'MAYBE') return 'warning';
    return 'danger';
  };

  /**
   * Get CSS class for rank badge
   */
  const getRankClass = (rank) => {
    if (rank === 1) return 'gold';
    if (rank === 2) return 'silver';
    if (rank === 3) return 'bronze';
    return '';
  };

  // Prepare chart data
  const chartData = results?.results?.map((r) => ({
    name: r.name,
    score: Math.round(r.score),
    fill: getScoreColor(r.score)
  })) || [];

  return (
    <>
      <Header title="Candidate Dashboard" breadcrumb="Dashboard" />
      
      {/* Input Form Card */}
      <div className="card">
        <h2 className="card-title">Compare Candidates</h2>
        
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

        {/* Number of Candidates Selector */}
        <div className="form-group">
          <label className="form-label">Number of Candidates (2-5)</label>
          <select
            className="form-select"
            value={numCandidates}
            onChange={(e) => handleNumChange(parseInt(e.target.value))}
            disabled={loading}
          >
            <option value={2}>2 Candidates</option>
            <option value={3}>3 Candidates</option>
            <option value={4}>4 Candidates</option>
            <option value={5}>5 Candidates</option>
          </select>
        </div>

        {/* Candidate Input Cards */}
        <div className="candidate-inputs">
          {candidates.map((candidate, idx) => (
            <div key={idx} className="candidate-card">
              <div className="candidate-header">
                <span className="candidate-number">Candidate {idx + 1}</span>
              </div>
              
              {/* Name Input */}
              <div className="form-group">
                <label className="form-label">Name</label>
                <input
                  type="text"
                  className="form-input"
                  placeholder="Enter candidate name"
                  value={candidate.name}
                  onChange={(e) => handleCandidateChange(idx, 'name', e.target.value)}
                  disabled={loading}
                />
              </div>
              
              {/* CV Input */}
              <div className="form-group" style={{ marginBottom: 0 }}>
                <label className="form-label">CV</label>
                <textarea
                  className="form-textarea"
                  placeholder="Paste candidate CV here..."
                  value={candidate.cv}
                  onChange={(e) => handleCandidateChange(idx, 'cv', e.target.value)}
                  rows={3}
                  disabled={loading}
                />
              </div>
            </div>
          ))}
        </div>

        {/* Submit Button */}
        <button 
          className="btn btn-primary btn-block" 
          onClick={handleCompare}
          disabled={loading}
          style={{ marginTop: '20px' }}
        >
          {loading ? 'Comparing...' : 'Compare All Candidates'}
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
          <p className="loading-text">Comparing candidates...</p>
        </div>
      )}

      {/* Results Display */}
      {results && !loading && (
        <>
          {/* Top Candidate Highlight Card */}
          {results.results && results.results.length > 0 && (
            <div className="top-candidate-card">
              <div className="top-candidate-label">Top Candidate</div>
              <div className="top-candidate-name">{results.results[0].name}</div>
              <div className="top-candidate-stats">
                <div className="top-stat">
                  <div className="top-stat-value">{Math.round(results.results[0].score)}%</div>
                  <div className="top-stat-label">Match Score</div>
                </div>
                <div className="top-stat">
                  <div className="top-stat-value">{results.results[0].matched}</div>
                  <div className="top-stat-label">Skills Matched</div>
                </div>
                <div className="top-stat">
                  <div className="top-stat-value">{results.results[0].missing}</div>
                  <div className="top-stat-label">Skills Missing</div>
                </div>
              </div>
            </div>
          )}

          {/* Rankings Table */}
          <div className="card">
            <h2 className="card-title">Rankings</h2>
            <div className="table-container">
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Rank</th>
                    <th>Name</th>
                    <th>Match Score</th>
                    <th>Matched</th>
                    <th>Missing</th>
                    <th>Verdict</th>
                  </tr>
                </thead>
                <tbody>
                  {results.results?.map((result, idx) => (
                    <tr key={idx}>
                      <td>
                        <span className={`rank-badge ${getRankClass(idx + 1)}`}>
                          {idx + 1}
                        </span>
                      </td>
                      <td style={{ fontWeight: 600 }}>{result.name}</td>
                      <td>
                        <span style={{ 
                          color: getScoreColor(result.score),
                          fontWeight: 700 
                        }}>
                          {Math.round(result.score)}%
                        </span>
                      </td>
                      <td>{result.matched}</td>
                      <td>{result.missing}</td>
                      <td>
                        <span className={`verdict-badge ${getVerdictClass(result.verdict)}`}>
                          {result.verdict}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          {/* Score Comparison Chart */}
          <div className="chart-container">
            <h3 className="chart-title">Score Comparison</h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={chartData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                <XAxis 
                  dataKey="name" 
                  tick={{ fill: '#8B949E', fontSize: 12 }}
                  axisLine={{ stroke: '#2D333B' }}
                />
                <YAxis 
                  tick={{ fill: '#8B949E', fontSize: 12 }}
                  axisLine={{ stroke: '#2D333B' }}
                  domain={[0, 100]}
                />
                <Tooltip 
                  contentStyle={{ 
                    backgroundColor: '#161B22', 
                    border: '1px solid #2D333B',
                    borderRadius: '8px',
                    color: '#FFFFFF'
                  }}
                />
                <Bar dataKey="score" radius={[8, 8, 0, 0]}>
                  {chartData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.fill} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </>
      )}
    </>
  );
}

export default Dashboard;
