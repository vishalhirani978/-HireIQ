import { NextResponse } from 'next/server';

export async function POST(request) {
  try {
    const body = await request.json();
    return NextResponse.json({ 
      success: true, 
      job_desc: body.job_desc,
      cv_text: body.cv_text,
      percentage: 50,
      matched_skills: [],
      missing_skills: [],
      recommendation: "Test - working",
      ai_analysis: "Test working",
      score_class: "medium",
      score_label: "Test",
      score_color: "#FFA500"
    });
  } catch (e) {
    return NextResponse.json({ error: e.message }, { status: 500 });
  }
}