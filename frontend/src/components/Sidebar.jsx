/**
 * Sidebar Component
 * Main navigation sidebar with logo, nav items, and status indicator
 */

import React from 'react';
import { NavLink } from 'react-router-dom';

/**
 * Sidebar Component
 * Provides navigation to all application pages
 */
function Sidebar() {
  return (
    <aside className="sidebar">
      {/* Logo Section */}
      <div className="sidebar-logo">
        <div className="logo-icon">IQ</div>
        <div className="logo-text">Hire<span>IQ</span></div>
        <div className="logo-subtitle">AI-Powered</div>
        <div className="logo-tagline">Hiring Assistant</div>
      </div>
      
      {/* Navigation Links */}
      <nav className="sidebar-nav">
        <div className="nav-label">Navigation</div>
        
        {/* Home Link */}
        <NavLink 
          to="/" 
          className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`} 
          end
        >
          <span className="nav-icon">&#8962;</span>
          <span>Home</span>
        </NavLink>
        
        {/* CV Screening Link */}
        <NavLink 
          to="/cv-screening" 
          className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}
        >
          <span className="nav-icon">&#128196;</span>
          <span>CV Screening</span>
        </NavLink>
        
        {/* Dashboard Link */}
        <NavLink 
          to="/dashboard" 
          className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}
        >
          <span className="nav-icon">&#128202;</span>
          <span>Dashboard</span>
        </NavLink>
        
        {/* Interview Questions Link */}
        <NavLink 
          to="/interview-questions" 
          className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}
        >
          <span className="nav-icon">&#10067;</span>
          <span>Interview Questions</span>
        </NavLink>
        
        {/* Bias Detector Link */}
        <NavLink 
          to="/bias-detector" 
          className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}
        >
          <span className="nav-icon">&#128737;</span>
          <span>Bias Detector</span>
        </NavLink>
      </nav>
      
      {/* Footer Status Indicator */}
      <div className="sidebar-footer">
        <div className="status-indicator">
          <span className="status-dot"></span>
          <span>System Online</span>
        </div>
        <div style={{ fontSize: '10px', color: 'var(--text-secondary)', marginTop: '4px' }}>
          Powered by AI
        </div>
      </div>
    </aside>
  );
}

export default Sidebar;
