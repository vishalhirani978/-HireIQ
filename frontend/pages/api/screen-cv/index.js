import { NextResponse } from 'next/server';
import { extractSkills, calculateScore, getScoreClass, generateRecommendation, generateAIAnalysis } from '../../../lib/services/scorer';

export async function POST(request) {
  try {
    const { job_desc, cv_text } = await request.json();
    
    if (!job_desc || !cv_text) {
      return NextResponse.json(
        { error: 'Job description and CV text are required' },
        { status: 400 }
      );
    }
    
    const { score, percentage } = calculateScore(job_desc, cv_text);
    const jobSkills = extractSkills(job_desc);
    const cvSkills = extractSkills(cv_text);
    
    const matchedSkills = jobSkills.filter(s => 
      cvSkills.some(cs => cs.toLowerCase() === s.toLowerCase())
    );
    const missingSkills = jobSkills.filter(s => 
      !cvSkills.some(cs => cs.toLowerCase() === s.toLowerCase())
    );
    
    const recommendation = generateRecommendation(percentage, matchedSkills, missingSkills);
    const { class: scoreClass, label: scoreLabel, color: scoreColor } = getScoreClass(percentage);
    
    const aiAnalysis = await generateAIAnalysis(job_desc, cv_text, matchedSkills, missingSkills, percentage, recommendation);
    
    return NextResponse.json({
      score,
      percentage,
      matched_skills: matchedSkills,
      missing_skills: missingSkills,
      recommendation,
      ai_analysis: aiAnalysis,
      score_class: scoreClass,
      score_label: scoreLabel,
      score_color: scoreColor
    });
  } catch (error) {
    console.error('CV Screening Error:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}
