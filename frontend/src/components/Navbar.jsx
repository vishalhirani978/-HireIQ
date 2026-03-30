import React from 'react';
import { useLocation } from 'react-router-dom';

const pageTitles = {
  '/': 'Home',
  '/cv-screening': 'CV Screening',
  '/dashboard': 'Candidate Dashboard',
  '/interview-questions': 'Interview Questions',
  '/bias-detector': 'Bias Detector'
};

function Navbar() {
  const location = useLocation();
  const title = pageTitles[location.pathname] || 'HireIQ';

  return (
    <nav className="navbar">
      <h1 className="navbar-title">{title}</h1>
      <div className="navbar-actions">
        <span style={{ color: 'var(--text-secondary)', fontSize: '0.85rem' }}>
          AI-Powered Hiring Assistant
        </span>
      </div>
    </nav>
  );
}

export default Navbar;
