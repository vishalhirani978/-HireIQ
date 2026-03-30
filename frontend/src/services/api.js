import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const screenCV = async (jobDesc, cvText) => {
  const response = await api.post('/screen-cv', {
    job_desc: jobDesc,
    cv_text: cvText,
  });
  return response.data;
};

export const compareCandidates = async (jobDesc, candidates) => {
  const response = await api.post('/compare-candidates', {
    job_desc: jobDesc,
    candidates: candidates,
  });
  return response.data;
};

export const generateQuestions = async (jobDesc, cvText, difficulty, numQuestions) => {
  const response = await api.post('/generate-questions', {
    job_desc: jobDesc,
    cv_text: cvText,
    difficulty: difficulty,
    num_questions: numQuestions,
  });
  return response.data;
};

export const detectBias = async (jobDesc) => {
  const response = await api.post('/detect-bias', {
    job_desc: jobDesc,
  });
  return response.data;
};

export default api;
