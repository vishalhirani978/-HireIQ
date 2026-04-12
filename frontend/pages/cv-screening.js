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
      found.push(skill.charAt(0).toUpperCase() + skill.slice(1));
    }
  }
  return [...new Set(found)];
}

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
    score: percentage / 100,
    percentage
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

export default function CVScreening() {
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
      await new Promise(r => setTimeout(r, 500));
      
      const { score, percentage } = calculateScore(jobDesc, cvText);
      const jobSkills = extractSkills(jobDesc);
      const cvSkills = extractSkills(cvText);
      
      const matchedSkills = jobSkills.filter(s => 
        cvSkills.some(cs => cs.toLowerCase() === s.toLowerCase())
      );
      const missingSkills = jobSkills.filter(s => 
        !cvSkills.some(cs => cs.toLowerCase() === s.toLowerCase())
      );
      
      const recommendation = generateRecommendation(percentage, matchedSkills, missingSkills);
      const { class: scoreClass, label: scoreLabel, color: scoreColor } = getScoreClass(percentage);
      
      setResults({
        score,
        percentage,
        matched_skills: matchedSkills,
        missing_skills: missingSkills,
        recommendation,
        ai_analysis: `Analysis complete. Match score is ${percentage}%. ${recommendation}`,
        score_class: scoreClass,
        score_label: scoreLabel,
        score_color: scoreColor
      });
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

          <div className={`score-card ${results.score_class}`}>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', textTransform: 'uppercase', letterSpacing: '1px' }}>
              Match Score
            </p>
            <h1 className={`score-value ${results.score_class}`}>{results.percentage}%</h1>
            <div className={`score-label ${results.score_class}`}>{results.score_label}</div>
          </div>

          <div className="card" style={{ marginBottom: '1.5rem' }}>
            <h3 style={{ marginBottom: '1rem' }}>Hiring Recommendation</h3>
            <p style={{ color: 'var(--text-secondary)', lineHeight: 1.7 }}>{results.recommendation}</p>
          </div>

          <div className="grid-2">
            <div className="card">
              <h4 className="card-title" style={{ marginBottom: '1rem' }}>
                <span style={{ color: 'var(--accent)', marginRight: '8px' }}>&#9679;</span>
                Matched Skills
              </h4>
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
              <h4 className="card-title" style={{ marginBottom: '1rem' }}>
                <span style={{ color: 'var(--error)', marginRight: '8px' }}>&#9679;</span>
                Missing Skills
              </h4>
              <div className="skills-container">
                {results.missing_skills && results.missing_skills.length > 0 ? (
                  results.missing_skills.map((skill, idx) => (
                    <span key={idx} className="skill-badge missing">{skill}</span>
                  ))
                ) : (
                  <div className="alert success" style={{ margin: 0 }}>No missing skills!</div>
                )}
              </div>
            </div>
          </div>

          <div className="card" style={{ marginTop: '1.5rem' }}>
            <h3 className="card-title" style={{ marginBottom: '1rem' }}>AI Analysis</h3>
            <p style={{ color: 'var(--text-secondary)', lineHeight: 1.75 }}>{results.ai_analysis}</p>
          </div>
        </div>
      )}
    </div>
  );
}