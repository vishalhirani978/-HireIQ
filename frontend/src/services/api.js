/**
 * API Service for HireIQ
 * Handles all API calls to the backend with loading and error handling
 */

import axios from 'axios';

// API base URL from environment or default to localhost
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

/**
 * Create axios instance with default configuration
 */
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 30000, // 30 second timeout
});

/**
 * API Response wrapper
 * @typedef {Object} ApiResponse
 * @property {boolean} success - Whether the API call succeeded
 * @property {*} data - Response data if successful
 * @property {string} error - Error message if failed
 */

/**
 * Screen a candidate CV against a job description
 * @param {string} jobDescription - The job description text
 * @param {string} candidateCV - The candidate's CV text
 * @returns {Promise<ApiResponse>} - API response with success/error state
 */
export const screenCV = async (jobDescription, candidateCV) => {
  try {
    const response = await api.post('/screen-cv', {
      job_description: jobDescription,
      candidate_cv: candidateCV,
    });
    return { success: true, data: response.data, error: null };
  } catch (error) {
    return handleApiError(error);
  }
};

/**
 * Compare multiple candidates against a job description
 * @param {string} jobDescription - The job description text
 * @param {Array} candidates - Array of {name, cv} objects
 * @returns {Promise<ApiResponse>} - API response with success/error state
 */
export const compareCandidates = async (jobDescription, candidates) => {
  try {
    const response = await api.post('/compare-candidates', {
      job_description: jobDescription,
      candidates: candidates,
    });
    return { success: true, data: response.data, error: null };
  } catch (error) {
    return handleApiError(error);
  }
};

/**
 * Generate interview questions based on job and candidate
 * @param {string} jobDescription - The job description text
 * @param {string} candidateCV - The candidate's CV text
 * @param {string} difficulty - Question difficulty (Easy/Medium/Hard)
 * @param {number} numQuestions - Number of questions to generate
 * @returns {Promise<ApiResponse>} - API response with success/error state
 */
export const generateQuestions = async (jobDescription, candidateCV, difficulty, numQuestions) => {
  try {
    const response = await api.post('/generate-questions', {
      job_description: jobDescription,
      candidate_cv: candidateCV,
      difficulty: difficulty,
      num_questions: numQuestions,
    });
    return { success: true, data: response.data, error: null };
  } catch (error) {
    return handleApiError(error);
  }
};

/**
 * Detect bias in a job description
 * @param {string} jobDescription - The job description to analyze
 * @returns {Promise<ApiResponse>} - API response with success/error state
 */
export const detectBias = async (jobDescription) => {
  try {
    const response = await api.post('/detect-bias', {
      job_description: jobDescription,
    });
    return { success: true, data: response.data, error: null };
  } catch (error) {
    return handleApiError(error);
  }
};

/**
 * Handle API errors and return standardized error message
 * @param {Error} error - The axios error object
 * @returns {ApiResponse} - Standardized error response
 */
const handleApiError = (error) => {
  // Handle network errors
  if (!error.response) {
    return {
      success: false,
      data: null,
      error: 'Unable to connect to the server. Please check your internet connection.',
    };
  }

  // Handle server errors
  if (error.response.status >= 500) {
    return {
      success: false,
      data: null,
      error: 'Server error. Please try again later.',
    };
  }

  // Handle validation and client errors
  const errorMessage = error.response?.data?.detail || 'An unexpected error occurred.';
  return {
    success: false,
    data: null,
    error: errorMessage,
  };
};

/**
 * Check if the API server is online
 * @returns {Promise<boolean>} - True if server is reachable
 */
export const checkServerHealth = async () => {
  try {
    const baseUrl = API_BASE_URL.replace('/api', '');
    await axios.get(`${baseUrl}/health`, { timeout: 5000 });
    return true;
  } catch {
    return false;
  }
};

export default api;
