import React from 'react';
import Footer from '../components/Footer';

function Home() {
  return (
    <div>
      <div className="hero">
        <div className="hero-icon">
          <div className="hero-outer"></div>
          <div className="hero-inner"></div>
        </div>
        <h1 className="hero-title">
          <span className="hire">Hire</span>
          <span className="iq">IQ</span>
        </h1>
        <p className="hero-subtitle">AI-Powered Hiring Assistant</p>
        <p className="hero-description">
          Screen CVs faster, fairer and smarter - powered by advanced AI technology designed for Pakistani startups and SMEs
        </p>
      </div>

      <div className="metrics-grid">
        <div className="metric-card">
          <div className="metric-label">Time Saved</div>
          <div className="metric-value">80%</div>
          <div className="metric-delta">vs manual screening</div>
        </div>
        <div className="metric-card">
          <div className="metric-label">Accuracy</div>
          <div className="metric-value">HIGH</div>
          <div className="metric-delta">skill matching</div>
        </div>
        <div className="metric-card">
          <div className="metric-label">Bias Checks</div>
          <div className="metric-value">5 Types</div>
          <div className="metric-delta">detected automatically</div>
        </div>
        <div className="metric-card">
          <div className="metric-label">Cost</div>
          <div className="metric-value">FREE</div>
          <div className="metric-delta">no subscription needed</div>
        </div>
      </div>

      <hr className="divider" />

      <div className="page-header" style={{ textAlign: 'center' }}>
        <h2 style={{ fontSize: '2rem', fontWeight: 700, marginBottom: '0.5rem' }}>
          Platform Capabilities
        </h2>
        <p style={{ color: 'var(--text-secondary)' }}>
          Everything you need for smarter hiring decisions
        </p>
      </div>

      <div className="grid-2">
        <div className="feature-card">
          <div className="feature-header">
            <div className="feature-icon accent">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
              </svg>
            </div>
            <div>
              <h3 className="feature-title">CV Screening</h3>
              <p className="feature-subtitle">AI-powered candidate analysis</p>
            </div>
          </div>
          <ul className="feature-list">
            <li>Paste CV + Job Description</li>
            <li>AI scores candidate match</li>
            <li>Shows matched & missing skills</li>
            <li>Gives Hire/Maybe/Reject verdict</li>
            <li>Full analysis with explanations</li>
          </ul>
        </div>

        <div className="feature-card">
          <div className="feature-header">
            <div className="feature-icon secondary">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <rect x="3" y="3" width="7" height="7"></rect>
                <rect x="14" y="3" width="7" height="7"></rect>
                <rect x="14" y="14" width="7" height="7"></rect>
                <rect x="3" y="14" width="7" height="7"></rect>
              </svg>
            </div>
            <div>
              <h3 className="feature-title">Candidate Dashboard</h3>
              <p className="feature-subtitle">Compare multiple candidates</p>
            </div>
          </div>
          <ul className="feature-list">
            <li>Compare up to 5 candidates</li>
            <li>Visual bar chart comparison</li>
            <li>Automatic ranking by score</li>
            <li>Side by side skill analysis</li>
          </ul>
        </div>

        <div className="feature-card">
          <div className="feature-header">
            <div className="feature-icon secondary">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
                <line x1="12" y1="17" x2="12.01" y2="17"></line>
              </svg>
            </div>
            <div>
              <h3 className="feature-title">Interview Questions</h3>
              <p className="feature-subtitle">Smart question generation</p>
            </div>
          </div>
          <ul className="feature-list">
            <li>Auto-generated from CV gaps</li>
            <li>3 difficulty levels</li>
            <li>Skill verification questions</li>
            <li>Behavioral questions included</li>
          </ul>
        </div>

        <div className="feature-card">
          <div className="feature-header">
            <div className="feature-icon warning">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
              </svg>
            </div>
            <div>
              <h3 className="feature-title">Bias Detector</h3>
              <p className="feature-subtitle">Ensure fair hiring practices</p>
            </div>
          </div>
          <ul className="feature-list">
            <li>Detects 5 types of bias</li>
            <li>Age, Gender, Origin detection</li>
            <li>Fairness score calculated</li>
            <li>Improvement suggestions</li>
          </ul>
        </div>
      </div>

      <hr className="divider" />

      <div className="page-header" style={{ textAlign: 'center' }}>
        <h2 style={{ fontSize: '2rem', fontWeight: 700, marginBottom: '0.5rem' }}>
          How It Works
        </h2>
        <p style={{ color: 'var(--text-secondary)' }}>
          Three simple steps to better hiring
        </p>
      </div>

      <div className="grid-3">
        <div className="step-card">
          <div className="step-number">01</div>
          <div className="step-icon primary">1</div>
          <h3 className="step-title">Input Data</h3>
          <p className="step-description">
            Paste your Job Description and Candidate CV into the system
          </p>
        </div>

        <div className="step-card">
          <div className="step-number">02</div>
          <div className="step-icon primary">2</div>
          <h3 className="step-title">AI Analysis</h3>
          <p className="step-description">
            Our AI analyzes skills, scores the match, and detects potential bias
          </p>
        </div>

        <div className="step-card">
          <div className="step-number">03</div>
          <div className="step-icon accent">3</div>
          <h3 className="step-title">Get Results</h3>
          <p className="step-description">
            Receive instant Hire/Maybe/Reject recommendations with full explanations
          </p>
        </div>
      </div>

      <Footer />
    </div>
  );
}

export default Home;
