# frontend/server.py - Flask Backend for HireIQ HTML Frontend
from flask import Flask, render_template, request, jsonify
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.helpers import extract_skills, get_match_score, get_recommendation
from backend.question_gen import generate_questions
from backend.bias_checker import detect_bias, BIAS_DICT

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('home.html', active_page='home')

@app.route('/cv-screening')
def cv_screening():
    return render_template('cv_screening.html', active_page='cv_screening')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', active_page='dashboard')

@app.route('/interview')
def interview():
    return render_template('interview.html', active_page='interview')

@app.route('/bias-detector')
def bias_detector():
    return render_template('bias_detector.html', active_page='bias_detector')

@app.route('/api/analyze-cv', methods=['POST'])
def analyze_cv():
    data = request.json
    job_desc = data.get('job_desc', data.get('job_description', ''))
    cv = data.get('cv_text', data.get('cv', ''))
    
    score, percentage = get_match_score(job_desc, cv)
    job_skills = extract_skills(job_desc)
    cv_skills = extract_skills(cv)
    matched_skills = [s for s in job_skills if s in cv_skills]
    missing_skills = [s for s in job_skills if s not in cv_skills]
    recommendation = get_recommendation(percentage, matched_skills, missing_skills)
    
    if percentage >= 70:
        score_class = 'high'
        score_label = 'Strong Match'
        score_color = '#00D4AA'
    elif percentage >= 40:
        score_class = 'medium'
        score_label = 'Partial Match'
        score_color = '#FFA500'
    else:
        score_class = 'low'
        score_label = 'Weak Match'
        score_color = '#FF4B4B'
    
    analysis_text = (
        f"Job requires: {job_desc[:300]}. "
        f"Candidate has: {cv[:300]}. "
        f"Matched skills: {', '.join(matched_skills)}. "
        f"Missing skills: {', '.join(missing_skills)}. "
        f"Overall match score: {percentage}%."
    )
    
    try:
        from huggingface_hub import InferenceClient
        client = InferenceClient(token=os.getenv("HUGGINGFACE_TOKEN"))
        ai_summary = client.summarization(analysis_text, model="facebook/bart-large-cnn")
        ai_analysis = ai_summary.summary_text
    except Exception as e:
        ai_analysis = f"Analysis complete. Match score is {percentage}%. {recommendation}"
    
    return jsonify({
        'percentage': percentage,
        'score_class': score_class,
        'score_label': score_label,
        'score_color': score_color,
        'matched_skills': matched_skills,
        'missing_skills': missing_skills,
        'recommendation': recommendation,
        'ai_analysis': ai_analysis
    })

@app.route('/api/screen-cv', methods=['POST'])
def screen_cv():
    data = request.json
    job_desc = data.get('job_desc', '')
    cv_text = data.get('cv_text', '')
    
    score, percentage = get_match_score(job_desc, cv_text)
    job_skills = extract_skills(job_desc)
    cv_skills = extract_skills(cv_text)
    matched_skills = [s for s in job_skills if s in cv_skills]
    missing_skills = [s for s in job_skills if s not in cv_skills]
    recommendation = get_recommendation(percentage, matched_skills, missing_skills)
    
    if percentage >= 70:
        score_class = 'high'
        score_label = 'Strong Match'
        score_color = '#00D4AA'
    elif percentage >= 40:
        score_class = 'medium'
        score_label = 'Partial Match'
        score_color = '#FFA500'
    else:
        score_class = 'low'
        score_label = 'Weak Match'
        score_color = '#FF4B4B'
    
    analysis_text = (
        f"Job requires: {job_desc[:300]}. "
        f"Candidate has: {cv_text[:300]}. "
        f"Matched skills: {', '.join(matched_skills)}. "
        f"Missing skills: {', '.join(missing_skills)}. "
        f"Overall match score: {percentage}%."
    )
    
    try:
        from huggingface_hub import InferenceClient
        client = InferenceClient(token=os.getenv("HUGGINGFACE_TOKEN"))
        ai_summary = client.summarization(analysis_text, model="facebook/bart-large-cnn")
        ai_analysis = ai_summary.summary_text
    except Exception as e:
        ai_analysis = f"Analysis complete. Match score is {percentage}%. {recommendation}"
    
    return jsonify({
        'percentage': percentage,
        'score_class': score_class,
        'score_label': score_label,
        'score_color': score_color,
        'matched_skills': matched_skills,
        'missing_skills': missing_skills,
        'recommendation': recommendation,
        'ai_analysis': ai_analysis
    })

@app.route('/api/compare-candidates', methods=['POST'])
def compare_candidates():
    data = request.json
    job_desc = data.get('job_desc', data.get('job_description', ''))
    candidates = data.get('candidates', [])
    
    results = []
    for candidate in candidates:
        score, percentage = get_match_score(job_desc, candidate['cv'])
        job_skills = extract_skills(job_desc)
        cv_skills = extract_skills(candidate['cv'])
        matched = [s for s in job_skills if s in cv_skills]
        missing = [s for s in job_skills if s not in cv_skills]
        
        if percentage >= 70:
            verdict = "HIRE"
            score_color = "#00D4AA"
        elif percentage >= 40:
            verdict = "MAYBE"
            score_color = "#FFA500"
        else:
            verdict = "REJECT"
            score_color = "#FF4B4B"
        
        results.append({
            'name': candidate['name'],
            'score': percentage,
            'matched': len(matched),
            'missing': len(missing),
            'verdict': verdict,
            'score_color': score_color
        })
    
    results.sort(key=lambda x: x['score'], reverse=True)
    
    return jsonify({'results': results})

@app.route('/api/generate-questions', methods=['POST'])
def api_generate_questions():
    data = request.json
    jd = data.get('job_desc', data.get('job_description', ''))
    cv = data.get('cv_text', data.get('cv', ''))
    difficulty = data.get('difficulty', 'Medium')
    num_questions = data.get('num_questions', 5)
    
    job_skills = extract_skills(jd)
    cv_skills = extract_skills(cv)
    missing_skills = [s for s in job_skills if s not in cv_skills]
    matched_skills = [s for s in job_skills if s in cv_skills]
    
    questions = generate_questions(matched_skills, missing_skills, difficulty, num_questions)
    
    total = questions['gap_count'] + questions['verify_count'] + questions['difficulty_count']
    
    return jsonify({
        'gap_questions': questions['gap'],
        'verify_questions': questions['verify'],
        'difficulty_questions': questions['difficulty'],
        'gap_count': questions['gap_count'],
        'verify_count': questions['verify_count'],
        'difficulty_count': questions['difficulty_count'],
        'total': total
    })

@app.route('/api/detect-bias', methods=['POST'])
def api_detect_bias():
    data = request.json
    job_desc = data.get('job_desc', data.get('job_description', ''))
    
    found_biases, fairness_score, biased_count, clean_count = detect_bias(job_desc)
    
    if fairness_score >= 80:
        progress_message = "This job description is largely bias-free"
    elif fairness_score >= 60:
        progress_message = "This job description has some bias — review highlighted issues"
    else:
        progress_message = "This job description has significant bias — major revision needed"
    
    clean_categories = [bias_type for bias_type in BIAS_DICT if bias_type not in found_biases]
    
    return jsonify({
        'fairness_score': fairness_score,
        'biased_count': biased_count,
        'clean_count': clean_count,
        'found_biases': found_biases,
        'progress_message': progress_message,
        'clean_categories': clean_categories
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
