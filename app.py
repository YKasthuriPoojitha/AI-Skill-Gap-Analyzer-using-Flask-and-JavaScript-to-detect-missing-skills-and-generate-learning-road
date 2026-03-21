from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()

        resume = data.get("resume", "").lower()

        skills = [s.strip() for s in resume.replace("and", ",").split(",")]

        required = ["python", "sql", "excel", "power bi"]

        missing = [skill for skill in required if skill not in skills]

        roadmap = ["Learn " + skill for skill in missing]

        score = int((len(skills) / (len(skills) + len(missing))) * 100) if (len(skills)+len(missing)) else 0

        return jsonify({
            "skills": skills,
            "missing_skills": missing,
            "roadmap": roadmap,
            "score": score
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 1000))
    app.run(host='0.0.0.0', port=port)