import Head from 'next/head';
import Link from 'next/link';

export default function Layout({ children }) {
  return (
    <>
      <Head>
        <title>HireIQ - AI Hiring Assistant</title>
        <meta name="description" content="AI-Powered Hiring Assistant for Pakistani startups and SMEs" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <div className="app-container">
        <aside className="sidebar">
          <div className="logo-container">
            <div className="logo-wrapper">
              <div className="logo-icon">
                <div className="logo-outer"></div>
                <div className="logo-inner"></div>
              </div>
              <div className="logo-text">
                <span className="logo-hire">Hire</span><span className="logo-iq">IQ</span>
              </div>
            </div>
            <div className="logo-subtitle">
              <div className="subtitle-line1">AI-Powered</div>
              <div className="subtitle-line2">Hiring Assistant</div>
            </div>
          </div>
          
          <nav className="nav-menu">
            <Link href="/" className="nav-item">Home</Link>
            <Link href="/cv-screening" className="nav-item">CV Screening</Link>
            <Link href="/dashboard" className="nav-item">Dashboard</Link>
            <Link href="/interview-questions" className="nav-item">Interview Questions</Link>
            <Link href="/bias-detector" className="nav-item">Bias Detector</Link>
          </nav>
          
          <div className="sidebar-footer">
            <div className="sidebar-footer-status">
              <div className="sidebar-footer-dot"></div>
              <span className="sidebar-footer-text">System Online</span>
            </div>
            <div className="sidebar-footer-credit">Powered by AI & Hugging Face</div>
          </div>
        </aside>
        
        <div className="main-wrapper">
          <header className="navbar">
            <div className="navbar-brand">HireIQ</div>
            <div className="navbar-links">
              <Link href="/" className="navbar-link">Home</Link>
              <Link href="/cv-screening" className="navbar-link">CV Screening</Link>
              <Link href="/bias-detector" className="navbar-link">Bias Detector</Link>
            </div>
          </header>
          
          <main className="main-content">
            {children}
          </main>
          
          <footer className="footer">
            <p>Built with passion for Pakistani Businesses | AI & Big Data Expo Hackathon 2026</p>
          </footer>
        </div>
      </div>
    </>
  );
}
