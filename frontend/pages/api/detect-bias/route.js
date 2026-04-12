import { NextResponse } from 'next/server';
import { detectBias } from '@/lib/services/biasChecker';

export async function POST(request) {
  try {
    const { job_desc } = await request.json();
    
    if (!job_desc) {
      return NextResponse.json(
        { error: 'Job description is required' },
        { status: 400 }
      );
    }
    
    const result = detectBias(job_desc);
    
    return NextResponse.json(result);
  } catch (error) {
    console.error('Detect Bias Error:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}
