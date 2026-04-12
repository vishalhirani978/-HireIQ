const SKILLS_LIST = [
  "python", "sql", "java", "javascript", "typescript",
  "machine learning", "ml", "data science", "pandas", "numpy",
  "scikit-learn", "tensorflow", "keras", "pytorch", "deep learning",
  "nlp", "natural language processing", "react", "nodejs", "angular",
  "vue", "html", "css", "django", "flask", "fastapi",
  "excel", "powerpoint", "tableau", "power bi", "aws", "azure",
  "docker", "kubernetes", "git", "linux", "sql server",
  "mongodb", "postgresql", "mysql", "redis", "elasticsearch",
  "communication", "teamwork", "leadership", "problem solving",
  "management", "analysis", "project management", "agile", "scrum"
];

function extractSkills(text) {
  const found = [];
  const textLower = text.toLowerCase();
  for (const skill of SKILLS_LIST) {
    if (textLower.includes(skill)) {
      found.push(skill.charAt(0).toUpperCase() + skill.slice(1));
    }
  }
  return [...new Set(found)];
}

function tokenize(text) {
  return text.toLowerCase().split(/\W+/).filter(word => word.length > 1);
}

function termFrequency(term, tokens) {
  const count = tokens.filter(t => t === term).length;
  return count / tokens.length;
}

function inverseDocumentFrequency(term, documents) {
  const numDocsWithTerm = documents.filter(doc => doc.includes(term)).length;
  if (numDocsWithTerm === 0) return 0;
  return Math.log(documents.length / numDocsWithTerm);
}

function cosineSimilarity(vec1, vec2) {
  const allTerms = [...new Set([...Object.keys(vec1), ...Object.keys(vec2)])];
  const dotProduct = allTerms.reduce((sum, term) => sum + (vec1[term] || 0) * (vec2[term] || 0), 0);
  const mag1 = Math.sqrt(Object.values(vec1).reduce((sum, val) => sum + val * val, 0));
  const mag2 = Math.sqrt(Object.values(vec2).reduce((sum, val) => sum + val * val, 0));
  if (mag1 === 0 || mag2 === 0) return 0;
  return dotProduct / (mag1 * mag2);
}

function calculateTFIDF(text1, text2) {
  const tokens1 = tokenize(text1);
  const tokens2 = tokenize(text2);
  const documents = [text1.toLowerCase(), text2.toLowerCase()];
  
  const allTerms = [...new Set([...tokens1, ...tokens2])];
  
  const tfidf1 = {};
  const tfidf2 = {};
  
  for (const term of allTerms) {
    tfidf1[term] = termFrequency(term, tokens1) * inverseDocumentFrequency(term, documents);
    tfidf2[term] = termFrequency(term, tokens2) * inverseDocumentFrequency(term, documents);
  }
  
  return cosineSimilarity(tfidf1, tfidf2);
}

function calculateScore(jobDesc, cvText) {
  const jobSkills = extractSkills(jobDesc);
  const cvSkills = extractSkills(cvText);
  
  if (!jobSkills.length) {
    return { score: 0, percentage: 0 };
  }
  
  const matched = jobSkills.filter(s => 
    cvSkills.some(cs => cs.toLowerCase() === s.toLowerCase())
  );
  const matchedCount = matched.length;
  const totalRequired = jobSkills.length;
  
  const skillsPercentage = (matchedCount / totalRequired) * 100;
  const tfidfScore = calculateTFIDF(jobDesc, cvText) * 100;
  
  const percentage = Math.min(Math.round((skillsPercentage * 0.7 + tfidfScore * 0.3) * 10) / 10, 100);
  
  return {
    score: percentage / 100,
    percentage
  };
}

function getScoreClass(percentage) {
  if (percentage >= 70) {
    return { class: "high", label: "Strong Match", color: "#00D4AA" };
  } else if (percentage >= 40) {
    return { class: "medium", label: "Partial Match", color: "#FFA500" };
  }
  return { class: "low", label: "Weak Match", color: "#FF4B4B" };
}

function generateRecommendation(percentage, matchedSkills, missingSkills) {
  const matchedCount = matchedSkills.length;
  const missingCount = missingSkills.length;
  
  if (percentage >= 70) {
    return `STRONG HIRE - ${percentage}% Match. This candidate is an excellent fit with ${matchedCount} matched skills including ${matchedSkills.slice(0, 3).join(', ') || 'N/A'}. Recommended for immediate technical interview.`;
  } else if (percentage >= 40) {
    return `MAYBE - ${percentage}% Match. This candidate partially meets requirements with ${matchedCount} matched skills: ${matchedSkills.join(', ') || 'None'}. Missing ${missingCount} skills: ${missingSkills.join(', ') || 'None'}. Consider for interview if no stronger candidates available.`;
  }
  return `REJECT - ${percentage}% Match. This candidate does not meet minimum requirements. Only matches ${matchedCount} skills. Missing ${missingCount} critical skills. Do not proceed with this candidate.`;
}

async function generateAIAnalysis(jobDesc, cvText, matchedSkills, missingSkills, percentage, recommendation) {
  const token = process.env.HUGGINGFACE_TOKEN || process.env.NEXT_PUBLIC_HUGGINGFACE_TOKEN;
  
  if (!token || token === 'your_token_here') {
    return `Analysis complete. Match score is ${percentage}%. ${recommendation}`;
  }
  
  try {
    const analysisText = `Job requires: ${jobDesc.slice(0, 200)}. Candidate has: ${cvText.slice(0, 200)}. Matched skills: ${matchedSkills.join(', ') || 'None'}. Missing skills: ${missingSkills.join(', ') || 'None'}. Overall match score: ${percentage}%.`;
    
    const response = await fetch("https://api-inference.huggingface.co/models/facebook/bart-large-cnn", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ inputs: analysisText, parameters: { max_length: 150 } })
    });
    
    if (!response.ok) {
      throw new Error('HuggingFace API error');
    }
    
    const result = await response.json();
    return result[0]?.summary_text || `Analysis complete. Match score is ${percentage}%. ${recommendation}`;
  } catch (error) {
    console.error('AI Analysis Error:', error);
    return `Analysis complete. Match score is ${percentage}%. ${recommendation}`;
  }
}

export {
  extractSkills,
  calculateScore,
  getScoreClass,
  generateRecommendation,
  generateAIAnalysis
};
