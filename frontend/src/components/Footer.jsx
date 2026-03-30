import React from 'react';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-status">
        <div className="footer-dot"></div>
        <span style={{ color: 'var(--text-secondary)', fontSize: '0.85rem' }}>
          Built for Pakistani Businesses
        </span>
      </div>
      <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginBottom: '0.5rem' }}>
        Powered by AI & Hugging Face
      </p>
      <p className="footer-tagline">
        HireIQ - Making hiring faster, fairer and smarter
      </p>
    </footer>
  );
}

export default Footer;
