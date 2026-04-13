import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

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

function tokenize(text) {
  return text.toLowerCase().split(/\W+/).filter(word => word.length > 1);
}

function termFrequency(term, tokens) {
  const count = tokens.filter(t => t === term).length;
  return count / tokens.length;
}

function inverseDocumentFrequency(term, documents) {
  const numDocsWithTerm = documents.filter(doc => doc.includes(term)).length;
  if (numDocsWithTerm === 0) return 0;
  return Math.log(documents.length / numDocsWithTerm);
}

function cosineSimilarity(vec1, vec2) {
  const allTerms = [...new Set([...Object.keys(vec1), ...Object.keys(vec2)])];
  const dotProduct = allTerms.reduce((sum, term) => sum + (vec1[term] || 0) * (vec2[term] || 0), 0);
  const mag1 = Math.sqrt(Object.values(vec1).reduce((sum, val) => sum + val * val, 0));
  const mag2 = Math.sqrt(Object.values(vec2).reduce((sum, val) => sum + val * val, 0));
  if (mag1 === 0 || mag2 === 0) return 0;
  return dotProduct / (mag1 * mag2);
}

function calculateTFIDF(text1, text2) {
  const tokens1 = tokenize(text1);
  const tokens2 = tokenize(text2);
  const documents = [text1.toLowerCase(), text2.toLowerCase()];
  const allTerms = [...new Set([...tokens1, ...tokens2])];
  const tfidf1 = {};
  const tfidf2 = {};
  for (const term of allTerms) {
    tfidf1[term] = termFrequency(term, tokens1) * inverseDocumentFrequency(term, documents);
    tfidf2[term] = termFrequency(term, tokens2) * inverseDocumentFrequency(term, documents);
  }
  return cosineSimilarity(tfidf1, tfidf2);
}

function extractSkills(text) {
  const found = [];
  const textLower = text.toLowerCase();
  for (const skill of SKILLS_LIST) {
    if (textLower.includes(skill)) {
      found.push(skill.charAt(0).toUpperCase() + skill.slice(1));
    }
  }
  return [...new Set(found)];
}

function calculateScore(jobDesc, cvText) {
  const jobSkills = extractSkills(jobDesc);
  const cvSkills = extractSkills(cvText);
  if (!jobSkills.length) {
    return { score: 0, percentage: 0 };
  }
  const matched = jobSkills.filter(s => 
    cvSkills.some(cs => cs.toLowerCase() === s.toLowerCase())
  );
  const matchedCount = matched.length;
  const totalRequired = jobSkills.length;
  const skillsPercentage = (matchedCount / totalRequired) * 100;
  const tfidfScore = calculateTFIDF(jobDesc, cvText) * 100;
  const percentage = Math.min(Math.round((skillsPercentage * 0.7 + tfidfScore * 0.3) * 10) / 10, 100);
  return {
    percentage,
    matchedSkills: matched,
    missingSkills: jobSkills.filter(s => !cvSkills.some(cs => cs.toLowerCase() === s.toLowerCase()))
  };
}

function getScoreClass(percentage) {
  if (percentage >= 70) {
    return { class: "high", label: "Strong Match", color: "#00D4AA" };
  } else if (percentage >= 40) {
    return { class: "medium", label: "Partial Match", color: "#FFA500" };
  }
  return { class: "low", label: "Weak Match", color: "#FF4B4B" };
}

function generateRecommendation(percentage, matchedSkills, missingSkills) {
  const matchedCount = matchedSkills?.length || 0;
  const missingCount = missingSkills?.length || 0;
  
  if (percentage >= 70) {
    return `STRONG HIRE - ${percentage}% Match. This candidate is an excellent fit with ${matchedCount} matched skills including ${matchedSkills?.slice(0, 3).join(', ') || 'N/A'}. Recommended for immediate technical interview.`;
  } else if (percentage >= 40) {
    return `MAYBE - ${percentage}% Match. This candidate partially meets requirements with ${matchedCount} matched skills: ${matchedSkills?.join(', ') || 'None'}. Missing ${missingCount} skills: ${missingSkills?.join(', ') || 'None'}. Consider for interview if no stronger candidates available.`;
  }
  return `REJECT - ${percentage}% Match. This candidate does not meet minimum requirements. Only matches ${matchedCount} skills. Missing ${missingCount} critical skills. Do not proceed with this candidate.`;
}

export default function Dashboard() {
  const [jobDesc, setJobDesc] = useState('');
  const [numCandidates, setNumCandidates] = useState(3);
  const [candidates, setCandidates] = useState(
    Array.from({ length: 3 }, () => ({ name: '', cv: '' }))
  );
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState('');

  const handleCandidateChange = (index, field, value) => {
    const updated = [...candidates];
    updated[index][field] = value;
    setCandidates(updated);
  };

  const handleNumChange = (num) => {
    setNumCandidates(num);
    setCandidates(Array.from({ length: num }, () => ({ name: '', cv: '' })));
  };

  const handleSubmit = async () => {
    if (!jobDesc || candidates.some(c => !c.name || !c.cv)) {
      setError('Please fill Job Description and ALL candidate names + CVs');
      return;
    }
    
    setLoading(true);
    setError('');
    setResults(null);
    
    try {
      await new Promise(r => setTimeout(r, 500));
      
      const compareResults = candidates.map(candidate => {
        const { percentage, matchedSkills, missingSkills } = calculateScore(jobDesc, candidate.cv);
        const { class: scoreClass, label: scoreLabel, color: scoreColor } = getScoreClass(percentage);
        
        return {
          name: candidate.name,
          score: percentage,
          matched: matchedSkills.length,
          missing: missingSkills.length,
          verdict: scoreLabel,
          score_color: scoreColor
        };
      });
      
      compareResults.sort((a, b) => b.score - a.score);
      
      setResults({ results: compareResults });
    } catch (err) {
      console.error('Dashboard error:', err);
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
              <rect x="3" y="3" width="7" height="7"></rect>
              <rect x="14" y="3" width="7" height="7"></rect>
              <rect x="14" y="14" width="7" height="7"></rect>
              <rect x="3" y="14" width="7" height="7"></rect>
            </svg>
          </div>
          <div>
            <h1 className="page-title">Candidates Dashboard</h1>
            <p className="page-subtitle">Compare multiple candidates and make data-driven hiring decisions</p>
          </div>
        </div>
      </div>

      <div className="card">
        <div className="card-header">
          <div className="card-icon secondary">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            </svg>
          </div>
          <div>
            <h3 className="card-title">Job Description</h3>
            <p className="card-subtitle">Enter the role requirements for comparison</p>
          </div>
        </div>
        <textarea
          className="form-textarea"
          placeholder="e.g. We need a Python developer with ML experience..."
          value={jobDesc}
          onChange={(e) => setJobDesc(e.target.value)}
          style={{ height: '120px' }}
        />
      </div>

      <div className="card" style={{ marginTop: '1rem' }}>
        <div className="form-group" style={{ marginBottom: 0 }}>
          <label className="form-label">Number of Candidates</label>
          <select
            className="form-select"
            value={numCandidates}
            onChange={(e) => handleNumChange(parseInt(e.target.value))}
            style={{ maxWidth: '200px' }}
          >
            <option value={2}>2 Candidates</option>
            <option value={3}>3 Candidates</option>
            <option value={4}>4 Candidates</option>
            <option value={5}>5 Candidates</option>
          </select>
        </div>
      </div>

      <hr className="divider" />

      {candidates.map((candidate, idx) => (
        <div key={idx} className="card" style={{ marginBottom: '1rem' }}>
          <h4 style={{ marginBottom: '1rem', color: 'var(--text-secondary)' }}>
            Candidate {idx + 1}
          </h4>
          <div className="grid-2">
            <div className="form-group">
              <label className="form-label">Name</label>
              <input
                type="text"
                className="form-input"
                placeholder="Enter candidate name"
                value={candidate.name}
                onChange={(e) => handleCandidateChange(idx, 'name', e.target.value)}
              />
            </div>
            <div className="form-group">
              <label className="form-label">CV</label>
              <textarea
                className="form-textarea"
                placeholder="Paste candidate CV here..."
                value={candidate.cv}
                onChange={(e) => handleCandidateChange(idx, 'cv', e.target.value)}
                style={{ height: '100px' }}
              />
            </div>
          </div>
        </div>
      ))}

      <div style={{ textAlign: 'center', margin: '2rem 0' }}>
        <button className="btn btn-primary" onClick={handleSubmit} disabled={loading} style={{ maxWidth: '300px' }}>
          {loading ? 'Comparing...' : 'Compare All Candidates'}
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
            <h2 className="page-title">Candidate Rankings</h2>
            <p className="page-subtitle">Sorted by match score</p>
          </div>

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
              {results.results.map((result, idx) => (
                <tr key={idx}>
                  <td>{idx + 1}</td>
                  <td>{result.name}</td>
                  <td style={{ color: result.score_color, fontWeight: 600 }}>{result.score}%</td>
                  <td>{result.matched}</td>
                  <td>{result.missing}</td>
                  <td>
                    <span className={`skill-badge ${result.score >= 70 ? 'matched' : 'missing'}`}>
                      {result.verdict}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          <div className="page-header" style={{ marginTop: '2rem' }}>
            <h3 style={{ fontSize: '1.2rem', fontWeight: 600 }}>Score Comparison</h3>
          </div>

          <div className="card">
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={results.results}>
                <CartesianGrid strokeDasharray="3 3" stroke="#30363D" />
                <XAxis dataKey="name" stroke="#8B949E" />
                <YAxis stroke="#8B949E" domain={[0, 100]} />
                <Tooltip
                  contentStyle={{ background: '#161B22', border: '1px solid #30363D' }}
                  labelStyle={{ color: '#FFFFFF' }}
                />
                <Bar dataKey="score" fill="#2E86AB" radius={[8, 8, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>

          <div className="card" style={{ marginTop: '1.5rem' }}>
            <h3 style={{ marginBottom: '1rem' }}>
              <span style={{ color: 'var(--warning)' }}>&#9733;</span> Top Candidate
            </h3>
            <p style={{ color: 'var(--text-secondary)' }}>
              <strong style={{ color: '#FFFFFF' }}>{results.results[0].name}</strong> is the top candidate
              with a match score of <strong style={{ color: results.results[0].score_color }}>
                {results.results[0].score}%
              </strong>
            </p>
          </div>
        </div>
      )}
    </div>
  );
}