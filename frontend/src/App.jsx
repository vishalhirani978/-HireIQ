import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import Footer from './components/Footer';
import Home from './pages/Home';
import CVScreening from './pages/CVScreening';
import Dashboard from './pages/Dashboard';
import InterviewQuestions from './pages/InterviewQuestions';
import BiasDetector from './pages/BiasDetector';
import './styles/global.css';

function App() {
  return (
    <BrowserRouter future={{ v7_relativeSplatPath: true, v7_startTransition: true }}>
      <div className="app-container">
        <Sidebar />
        <div className="main-wrapper">
          <Navbar />
          <main className="main-content">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/cv-screening" element={<CVScreening />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/interview-questions" element={<InterviewQuestions />} />
              <Route path="/bias-detector" element={<BiasDetector />} />
            </Routes>
            <Footer />
          </main>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
