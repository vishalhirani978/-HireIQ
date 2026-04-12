const BIAS_DICT = {
  "Age Bias": {
    "words": [
      "young", "energetic", "fresh graduate", "recent graduate",
      "digital native", "old", "mature", "experienced only",
      "years old", "age limit", "under 30", "under 25", "recently retired"
    ],
    "color": "#FF4B4B",
    "suggestion": "Remove age-related language. Focus on skills and experience requirements instead of age or generation."
  },
  "Gender Bias": {
    "words": [
      "he must", "she must", "him", "her", "guys",
      "manpower", "mankind", "man the", "salesman",
      "businessman", "craftsman", "chairman", "freshman",
      "workforce men", "hardworking man"
    ],
    "color": "#FF4B4B",
    "suggestion": "Use gender-neutral language like 'they', 'the candidate', 'team member', 'professional'."
  },
  "Origin Bias": {
    "words": [
      "native speaker", "mother tongue", "born in",
      "local candidate", "nationals only", "citizens only",
      "local residents", "must be from", "pakistani only",
      "lahore based", "karachi based"
    ],
    "color": "#FF4B4B",
    "suggestion": "Focus on language proficiency level and skills instead of origin or location."
  },
  "Appearance Bias": {
    "words": [
      "well groomed", "presentable", "attractive",
      "good looking", "physically fit", "slim",
      "height", "weight", "appearance", "clean shaven"
    ],
    "color": "#FFA500",
    "suggestion": "Only mention appearance if strictly necessary for the role (e.g., acting, modeling)."
  },
  "Exclusionary Language": {
    "words": [
      "must be", "only", "exclusively", "no exceptions",
      "strictly", "mandatory background", "specific religion",
      "specific sect", "caste", "prefer married"
    ],
    "color": "#FFA500",
    "suggestion": "Use inclusive language that welcomes diverse candidates. Avoid absolute requirements unless essential."
  }
};

function detectBias(text) {
  const foundBiases = {};
  const textLower = text.toLowerCase();
  
  for (const [biasType, data] of Object.entries(BIAS_DICT)) {
    const foundWords = [];
    for (const word of data.words) {
      if (textLower.includes(word.toLowerCase())) {
        foundWords.push(word);
      }
    }
    if (foundWords.length > 0) {
      foundBiases[biasType] = {
        "words": foundWords,
        "color": data.color,
        "suggestion": data.suggestion
      };
    }
  }
  
  const totalChecks = Object.keys(BIAS_DICT).length;
  const biasedCount = Object.keys(foundBiases).length;
  const cleanCount = totalChecks - biasedCount;
  const fairnessScore = Math.round(((totalChecks - biasedCount) / totalChecks) * 100);
  
  let progressMessage;
  if (fairnessScore >= 80) {
    progressMessage = "This job description is largely bias-free";
  } else if (fairnessScore >= 60) {
    progressMessage = "This job description has some bias - review highlighted issues";
  } else {
    progressMessage = "This job description has significant bias - major revision needed";
  }
  
  const cleanCategories = Object.keys(BIAS_DICT).filter(biasType => !foundBiases[biasType]);
  
  return {
    foundBiases,
    fairnessScore,
    biasedCount,
    cleanCount,
    progressMessage,
    cleanCategories
  };
}

module.exports = { detectBias, BIAS_DICT };
