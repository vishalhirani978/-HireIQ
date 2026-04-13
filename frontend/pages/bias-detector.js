import React, { useState } from 'react';

const BIAS_DICT = {
  "Age Bias": {
    words: [
      "young", "energetic", "fresh graduate", "recent graduate",
      "digital native", "old", "mature", "experienced only",
      "years old", "age limit", "under 30", "under 25", "recently retired"
    ],
    color: "#FF4B4B",
    suggestion: "Remove age-related language. Focus on skills and experience requirements instead of age or generation."
  },
  "Gender Bias": {
    words: [
      "he must", "she must", "him", "her", "guys",
      "manpower", "mankind", "man the", "salesman",
      "businessman", "craftsman", "chairman", "freshman",
      "workforce men", "hardworking man"
    ],
    color: "#FF4B4B",
    suggestion: "Use gender-neutral language like 'they', 'the candidate', 'team member', 'professional'."
  },
  "Origin Bias": {
    words: [
      "native speaker", "mother tongue", "born in",
      "local candidate", "nationals only", "citizens only",
      "local residents", "must be from", "pakistani only",
      "lahore based", "karachi based"
    ],
    color: "#FF4B4B",
    suggestion: "Focus on language proficiency level and skills instead of origin or location."
  },
  "Appearance Bias": {
    words: [
      "well groomed", "presentable", "attractive",
      "good looking", "physically fit", "slim",
      "height", "weight", "appearance", "clean shaven"
    ],
    color: "#FFA500",
    suggestion: "Only mention appearance if strictly necessary for the role (e.g., acting, modeling)."
  },
  "Exclusionary Language": {
    words: [
      "must be", "only", "exclusively", "no exceptions",
      "strictly", "mandatory background", "specific religion",
      "specific sect", "caste", "prefer married"
    ],
    color: "#FFA500",
    suggestion: "Use inclusive language that welcomes diverse candidates. Avoid absolute requirements unless essential."
  }
};

function detectBias(text) {
  const foundBiases = {};
  const textLower = text.toLowerCase();
  
  for (const [biasType, data] of Object.entries(BIAS_DICT)) {
    const foundWords = [];
    for (const word of data.words) {
      if (textLower.includes(word)) {
        foundWords.push(word);
      }
    }
    if (foundWords.length > 0) {
      foundBiases[biasType] = {
        words: foundWords,
        color: data.color,
        suggestion: data.suggestion
      };
    }
  }
  
  const totalChecks = Object.keys(BIAS_DICT).length;
  const biasedCount = Object.keys(foundBiases).length;
  const cleanCount = totalChecks - biasedCount;
  const fairnessScore = Math.round(((totalChecks - biasedCount) / totalChecks) * 100);
  
  let progressMessage;
  if (fairnessScore >= 80) {
    progressMessage = "This job description is largely bias-free";
  } else if (fairnessScore >= 60) {
    progressMessage = "This job description has some bias - review highlighted issues";
  } else {
    progressMessage = "This job description has significant bias - major revision needed";
  }
  
  const cleanCategories = Object.keys(BIAS_DICT).filter(type => !(type in foundBiases));
  
  return {
    found_biases: foundBiases,
    fairness_score: fairnessScore,
    biased_count: biasedCount,
    clean_count: cleanCount,
    progress_message: progressMessage,
    clean_categories: cleanCategories
  };
}

export default function BiasDetector() {
  const [jobDesc, setJobDesc] = useState('');
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    if (!jobDesc) {
      setError('Please paste a job description first');
      return;
    }
    
    setLoading(true);
    setError('');
    setResults(null);
    
    try {
      await new Promise(r => setTimeout(r, 500));
      const data = detectBias(jobDesc);
      setResults(data);
    } catch (err) {
      setError('An error occurred. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const getProgressColor = () => {
    if (!results) return 'var(--text-secondary)';
    if (results.fairness_score >= 80) return 'var(--accent)';
    if (results.fairness_score >= 60) return 'var(--warning)';
    return 'var(--error)';
  };

  return (
    <div>
      <div className="page-header">
        <div className="page-header-wrapper">
          <div className="page-icon" style={{ background: 'rgba(255,165,0,0.2)', borderColor: 'rgba(255,165,0,0.3)' }}>
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

          <div className="metrics-grid">
            <div className="metric-card">
              <div className="metric-label">Fairness Score</div>
              <div className="metric-value" style={{ color: getProgressColor() }}>{results.fairness_score}%</div>
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
              <div 
                className={`progress-fill ${results.fairness_score >= 80 ? 'high' : results.fairness_score >= 60 ? 'medium' : 'low'}`} 
                style={{ width: `${results.fairness_score}%` }}
              ></div>
            </div>
            <p style={{ color: getProgressColor(), marginTop: '1rem', fontWeight: 500 }}>
              {results.progress_message}
            </p>
          </div>

          <hr className="divider" />

          {results.found_biases && Object.keys(results.found_biases).length > 0 ? (
            <div>
              <h3 style={{ marginBottom: '1rem' }}>
                <span style={{ color: 'var(--error)' }}>&#9679;</span> Bias Detected
              </h3>
              {Object.entries(results.found_biases).map(([biasType, data]) => (
                <div key={biasType} className="card" style={{ marginBottom: '1rem' }}>
                  <h4 style={{ marginBottom: '0.75rem' }}>{biasType}</h4>
                  <div className="skills-container" style={{ marginBottom: '1rem' }}>
                    {data.words.map((word, idx) => (
                      <span key={idx} className="bias-word">{word}</span>
                    ))}
                  </div>
                  <div className="suggestion-box">
                    <p style={{ color: 'var(--accent)', fontWeight: 600, fontSize: '0.85rem', marginBottom: '0.5rem' }}>
                      &#8594; Suggestion
                    </p>
                    <p style={{ color: 'var(--text-secondary)' }}>{data.suggestion}</p>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="card" style={{ textAlign: 'center', padding: '3rem' }}>
              <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>&#10004;</div>
              <h3 style={{ color: 'var(--accent)', margin: '0 0 0.5rem 0' }}>No Bias Detected</h3>
              <p style={{ color: 'var(--text-secondary)', margin: 0 }}>This is a fair and inclusive job description</p>
            </div>
          )}

          <hr className="divider" />

          <h3 style={{ marginBottom: '1rem' }}>
            <span style={{ color: 'var(--accent)' }}>&#9679;</span> Clean Categories
          </h3>
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