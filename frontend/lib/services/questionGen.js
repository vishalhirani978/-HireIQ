const EASY_QUESTIONS = [
  "Tell me about yourself and your professional background.",
  "Why are you interested in this position and our company?",
  "What are your key strengths that make you a good fit?",
  "Where do you see yourself in 5 years?",
  "Why are you leaving your current job?",
  "Describe your ideal work environment.",
  "What motivates you to do your best work?"
];

const MEDIUM_QUESTIONS = [
  "Describe a challenging problem you solved and how you approached it.",
  "How do you stay updated with the latest technologies in your field?",
  "Tell me about a time you worked in a team under pressure.",
  "How do you handle tight deadlines and multiple priorities?",
  "Describe a situation where you had to learn something quickly.",
  "Tell me about a project you're most proud of.",
  "How do you approach debugging or troubleshooting issues?"
];

const HARD_QUESTIONS = [
  "Design a scalable system for processing 1 million records daily.",
  "How would you handle model drift in a production environment?",
  "Explain the trade-offs between precision and recall in your last project.",
  "How would you architect a real-time recommendation system?",
  "What strategies would you use to reduce overfitting in a deep learning model?",
  "Describe your experience with MLOps and deployment pipelines.",
  "How would you optimize a slow-performing database query?"
];

const SKILL_TEMPLATES = [
  "Tell me about a specific project where you used {skill}. What was the outcome?",
  "How confident are you with {skill} on a scale of 1-10? Give an example.",
  "What is the most complex task you have done using {skill}?",
  "How long have you been working with {skill} and what have you built?",
  "What challenges did you face while using {skill} and how did you solve them?"
];

function generateQuestions(matchedSkills, missingSkills, difficulty, numQuestions) {
  const gapCount = Math.min(missingSkills.length, Math.max(1, Math.floor(numQuestions / 3)));
  const verifyCount = Math.min(matchedSkills.length, Math.max(1, Math.floor(numQuestions / 3)));
  const difficultyCount = numQuestions - gapCount - verifyCount;
  
  const gapQuestions = missingSkills.slice(0, gapCount).map(skill =>
    `You listed ${skill} as a requirement. Can you walk us through your experience with ${skill} and explain how you've applied it in your work?`
  );
  
  const verifyQuestions = matchedSkills.slice(0, verifyCount).map((skill, i) => {
    const template = SKILL_TEMPLATES[i % SKILL_TEMPLATES.length];
    return template.replace('{skill}', skill);
  });
  
  let difficultyQuestions;
  if (difficulty === "Easy") {
    difficultyQuestions = EASY_QUESTIONS;
  } else if (difficulty === "Medium") {
    difficultyQuestions = MEDIUM_QUESTIONS;
  } else {
    difficultyQuestions = HARD_QUESTIONS;
  }
  
  return {
    gap_questions: gapQuestions,
    verify_questions: verifyQuestions,
    difficulty_questions: difficultyQuestions.slice(0, difficultyCount),
    gap_count: gapCount,
    verify_count: verifyCount,
    difficulty_count: difficultyCount,
    total: gapCount + verifyCount + difficultyCount
  };
}

module.exports = { generateQuestions };
