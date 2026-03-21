from flask import Flask, request, jsonify, render_template
import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai_module.ai import extract_skills, get_missing_skills, generate_roadmap, calculate_match_score

app = Flask(__name__, template_folder='../Frontend')

# 👇 CHANGE THIS PART
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json

    resume = data.get("resume", "")
    job_role = data.get("jobRole", "")

    skills = extract_skills(resume)
    missing = get_missing_skills(skills, job_role)
    roadmap = generate_roadmap(missing)
    score = calculate_match_score(skills, missing)

    return jsonify({
        "skills": skills,
        "missing_skills": missing,
        "roadmap": roadmap,
        "score": score
    })