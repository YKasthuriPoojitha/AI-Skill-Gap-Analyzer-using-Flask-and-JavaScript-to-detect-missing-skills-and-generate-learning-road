from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai_module.ai import extract_skills, get_missing_skills, generate_roadmap, calculate_match_score

# Flask app
app = Flask(__name__, template_folder='../Frontend', static_folder='../Frontend')
CORS(app)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Analyze API
@app.route('/analyze', methods=['POST'])
def analyze():
    try:
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

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


# Run locally
if __name__ == '__main__':
    app.run(debug=True)