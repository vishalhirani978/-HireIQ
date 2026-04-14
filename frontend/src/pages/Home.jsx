/**
 * Home Page Component
 * Main landing page for HireIQ application
 */

import React from 'react';
import Header from '../components/Header';

/**
 * Home Component
 * Displays hero section, statistics, features overview, and how-it-works steps
 */
function Home() {
  return (
    <>
      <Header title="Welcome" breadcrumb="Home" />
      
      {/* Hero Section - Main landing area */}
      <div className="hero-section">
        <div className="hero-icon">IQ</div>
        <h1 className="hero-title">
          Hire<span>IQ</span>
        </h1>
        <p className="hero-subtitle">AI-Powered Hiring Assistant</p>
        <p className="hero-desc">
          Screen CVs faster, fairer and smarter powered by advanced AI technology 
          designed for Pakistani startups and SMEs.
        </p>
      </div>
      
      {/* Statistics Cards */}
      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-value">80%</div>
          <div className="stat-label">Time Saved</div>
        </div>
        <div className="stat-card">
          <div className="stat-value">95%</div>
          <div className="stat-label">Accuracy</div>
        </div>
        <div className="stat-card">
          <div className="stat-value">5</div>
          <div className="stat-label">Bias Checks</div>
        </div>
        <div className="stat-card">
          <div className="stat-value">Free</div>
          <div className="stat-label">No Subscription</div>
        </div>
      </div>
      
      {/* Platform Features */}
      <div className="features-grid">
        <div className="feature-card">
          <div className="feature-icon">&#128196;</div>
          <h3 className="feature-title">CV Screening</h3>
          <p className="feature-desc">
            Analyze candidate CVs against job descriptions using AI-powered matching.
          </p>
          <ul className="feature-list">
            <li>TF-IDF + Skill matching</li>
            <li>AI-generated analysis</li>
            <li>Instant recommendations</li>
          </ul>
        </div>
        
        <div className="feature-card">
          <div className="feature-icon">&#128202;</div>
          <h3 className="feature-title">Candidate Dashboard</h3>
          <p className="feature-desc">
            Compare multiple candidates side-by-side with visual analytics.
          </p>
          <ul className="feature-list">
            <li>Ranked comparisons</li>
            <li>Bar chart visualization</li>
            <li>Best candidate highlight</li>
          </ul>
        </div>
        
        <div className="feature-card">
          <div className="feature-icon">&#10067;</div>
          <h3 className="feature-title">Interview Questions</h3>
          <p className="feature-desc">
            Generate tailored interview questions based on skill gaps.
          </p>
          <ul className="feature-list">
            <li>Gap-filling questions</li>
            <li>Skill verification</li>
            <li>Difficulty levels</li>
          </ul>
        </div>
        
        <div className="feature-card">
          <div className="feature-icon">&#128737;</div>
          <h3 className="feature-title">Bias Detector</h3>
          <p className="feature-desc">
            Identify and eliminate unconscious bias from job descriptions.
          </p>
          <ul className="feature-list">
            <li>5 bias categories</li>
            <li>Fairness scoring</li>
            <li>Improvement suggestions</li>
          </ul>
        </div>
      </div>
      
      {/* How It Works Steps */}
      <div className="steps-container">
        <div className="step-item">
          <div className="step-number">1</div>
          <h3 className="step-title">Input Data</h3>
          <p className="step-desc">Enter job description and candidate CVs</p>
        </div>
        <div className="step-item">
          <div className="step-number">2</div>
          <h3 className="step-title">AI Analysis</h3>
          <p className="step-desc">Our AI processes and analyzes the data</p>
        </div>
        <div className="step-item">
          <div className="step-number">3</div>
          <h3 className="step-title">Get Results</h3>
          <p className="step-desc">Receive detailed insights and recommendations</p>
        </div>
      </div>
    </>
  );
}

export default Home;
