import { NextResponse } from 'next/server';
import { extractSkills } from '../../../lib/services/scorer';
import { generateQuestions } from '../../../lib/services/questionGen';

export async function POST(request) {
  try {
    const { job_desc, cv_text, difficulty = 'Medium', num_questions = 5 } = await request.json();
    
    if (!job_desc || !cv_text) {
      return NextResponse.json(
        { error: 'Job description and CV text are required' },
        { status: 400 }
      );
    }
    
    const jobSkills = extractSkills(job_desc);
    const cvSkills = extractSkills(cv_text);
    
    const matchedSkills = jobSkills.filter(s => 
      cvSkills.some(cs => cs.toLowerCase() === s.toLowerCase())
    );
    const missingSkills = jobSkills.filter(s => 
      !cvSkills.some(cs => cs.toLowerCase() === s.toLowerCase())
    );
    
    const questions = generateQuestions(matchedSkills, missingSkills, difficulty, num_questions);
    
    return NextResponse.json(questions);
  } catch (error) {
    console.error('Generate Questions Error:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}
