/**
 * App Component
 * Main application entry point with routing configuration
 */

import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Footer from './components/Footer';
import Home from './pages/Home';
import CVScreening from './pages/CVScreening';
import Dashboard from './pages/Dashboard';
import InterviewQuestions from './pages/InterviewQuestions';
import BiasDetector from './pages/BiasDetector';
import './styles/global.css';

/**
 * App Component
 * Sets up routing and main layout structure
 */
function App() {
  return (
    <BrowserRouter>
      <div className="app-container">
        {/* Sidebar Navigation */}
        <Sidebar />
        
        {/* Main Content Area */}
        <main className="main-content">
          <div className="page-container">
            {/* Route Definitions */}
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/cv-screening" element={<CVScreening />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/interview-questions" element={<InterviewQuestions />} />
              <Route path="/bias-detector" element={<BiasDetector />} />
            </Routes>
          </div>
          
          {/* Footer */}
          <Footer />
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
