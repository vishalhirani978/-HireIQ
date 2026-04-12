import Head from 'next/head';
import Link from 'next/link';

export default function Home() {
  return (
    <>
      <Head>
        <title>HireIQ - AI-Powered Hiring Assistant</title>
      </Head>
      
      <div className="hero">
        <div className="hero-icon">
          <div className="hero-outer"></div>
          <div className="hero-inner"></div>
        </div>
        <h1 className="hero-title">
          <span className="hire">Hire</span><span className="iq">IQ</span>
        </h1>
        <p className="hero-subtitle">AI-Powered Hiring Assistant for Pakistani Startups</p>
        <p className="hero-description">
          Make smarter hiring decisions with AI-powered CV screening, bias detection, 
          and interview question generation — completely free for Pakistani businesses.
        </p>
        <Link href="/cv-screening" className="btn btn-primary">
          Start Screening CVs
        </Link>
      </div>

      <hr className="divider" />

      <div className="grid-3">
        <div className="feature-card">
          <div className="feature-header">
            <div className="feature-icon secondary">
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
            <li>TF-IDF skill matching</li>
            <li>Match percentage scoring</li>
            <li>Missing skills identification</li>
            <li>AI-generated recommendations</li>
          </ul>
          <Link href="/cv-screening" className="btn btn-secondary" style={{ marginTop: '1rem', width: '100%' }}>
            Try Now
          </Link>
        </div>

        <div className="feature-card">
          <div className="feature-header">
            <div className="feature-icon accent">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <rect x="3" y="3" width="7" height="7"></rect>
                <rect x="14" y="3" width="7" height="7"></rect>
                <rect x="14" y="14" width="7" height="7"></rect>
                <rect x="3" y="14" width="7" height="7"></rect>
              </svg>
            </div>
            <div>
              <h3 className="feature-title">Dashboard</h3>
              <p className="feature-subtitle">Compare multiple candidates</p>
            </div>
          </div>
          <ul className="feature-list">
            <li>Compare up to 5 candidates</li>
            <li>Visual bar chart comparison</li>
            <li>Automatic ranking</li>
            <li>Top candidate recommendation</li>
          </ul>
          <Link href="/dashboard" className="btn btn-secondary" style={{ marginTop: '1rem', width: '100%' }}>
            Compare Now
          </Link>
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
              <p className="feature-subtitle">Ensure fair hiring</p>
            </div>
          </div>
          <ul className="feature-list">
            <li>Age bias detection</li>
            <li>Gender bias detection</li>
            <li>Origin bias detection</li>
            <li>Fairness score calculation</li>
          </ul>
          <Link href="/bias-detector" className="btn btn-secondary" style={{ marginTop: '1rem', width: '100%' }}>
            Check Now
          </Link>
        </div>
      </div>

      <hr className="divider" />

      <div className="page-header">
        <h2 style={{ fontSize: '1.5rem', fontWeight: 600, marginBottom: '1rem' }}>
          How It Works
        </h2>
      </div>

      <div className="grid-3">
        <div className="step-card">
          <span className="step-number">1</span>
          <div className="step-icon primary">1</div>
          <h4 className="step-title">Paste Job & CV</h4>
          <p className="step-description">
            Enter the job description and paste candidate CV to analyze
          </p>
        </div>

        <div className="step-card">
          <span className="step-number">2</span>
          <div className="step-icon accent">2</div>
          <h4 className="step-title">AI Analyzes</h4>
          <p className="step-description">
            Our AI uses TF-IDF to match skills and calculate match percentage
          </p>
        </div>

        <div className="step-card">
          <span className="step-number">3</span>
          <div className="step-icon primary">3</div>
          <h4 className="step-title">Get Results</h4>
          <p className="step-description">
            Receive instant HIRE/MAYBE/REJECT recommendation with analysis
          </p>
        </div>
      </div>
    </>
  );
}
