import { NextResponse } from 'next/server';
import { extractSkills, calculateScore } from '@/lib/services/scorer';

function getScoreColor(score) {
  if (score >= 70) return "#00D4AA";
  if (score >= 40) return "#FFA500";
  return "#FF4B4B";
}

function getVerdict(score) {
  if (score >= 70) return "HIRE";
  if (score >= 40) return "MAYBE";
  return "REJECT";
}

export async function POST(request) {
  try {
    const { job_desc, candidates } = await request.json();
    
    if (!job_desc || !candidates || !Array.isArray(candidates)) {
      return NextResponse.json(
        { error: 'Job description and candidates array are required' },
        { status: 400 }
      );
    }
    
    const jobSkills = extractSkills(job_desc);
    const results = candidates.map(candidate => {
      const cvSkills = extractSkills(candidate.cv);
      const matched = jobSkills.filter(s => 
        cvSkills.some(cs => cs.toLowerCase() === s.toLowerCase())
      );
      const missing = jobSkills.filter(s => 
        !cvSkills.some(cs => cs.toLowerCase() === s.toLowerCase())
      );
      
      const { percentage } = calculateScore(job_desc, candidate.cv);
      
      return {
        name: candidate.name,
        score: percentage,
        matched: matched.length,
        missing: missing.length,
        verdict: getVerdict(percentage),
        score_color: getScoreColor(percentage)
      };
    });
    
    results.sort((a, b) => b.score - a.score);
    
    return NextResponse.json({ results });
  } catch (error) {
    console.error('Compare Candidates Error:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}
