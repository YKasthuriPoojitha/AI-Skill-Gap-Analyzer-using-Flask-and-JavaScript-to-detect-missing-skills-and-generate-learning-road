from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder="Frontend")
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()

        resume = data.get("resume", "")
        job_role = data.get("jobRole", "")

        skills = [s.strip() for s in resume.lower().split(",")]

        required = ["html", "css", "javascript", "react", "node"]

        missing = [skill for skill in required if skill not in skills]

        roadmap = ["Learn " + skill for skill in missing]

        score = int((len(skills) / (len(skils := skills) + len(missing))) * 100) if (len(skills)+len(missing)) else 0

        return jsonify({
            "skills": skills,
            "missing_skills": missing,
            "roadmap": roadmap,
            "score": score
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 🔥 IMPORTANT FOR RENDER
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)