from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder="../Frontend")
CORS(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()

        resume = data.get("resume", "")
        job_role = data.get("jobRole", "")

        # SIMPLE LOGIC (no ai_module dependency)
        skills = [s.strip() for s in resume.lower().split(",")]

        required = ["html", "css", "javascript", "react", "node"]
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


if __name__ == "__main__":
    app.run(debug=True)