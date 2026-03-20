import sys
import os

# 🔥 Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_module.ai import extract_skills, get_missing_skills, generate_roadmap

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend running 🚀"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json

    resume = data.get("resume", "")
    job_role = data.get("job_role", "")

    skills = extract_skills(resume)
    missing = get_missing_skills(skills, job_role)
    roadmap = generate_roadmap(missing)

    return jsonify({
        "missing_skills": missing,
        "roadmap": roadmap
    })

if __name__ == '__main__':
    app.run(debug=True)