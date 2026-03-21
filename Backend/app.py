from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="../Frontend", static_url_path="/")
CORS(app)

# Serve frontend
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

# API
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()

        resume = data.get("resume", "")
        job_role = data.get("jobRole", "").lower()

        skills = [s.strip() for s in resume.lower().split(",") if s.strip()]

        job_roles = {
            "data analyst": ["python", "sql", "excel", "power bi"],
            "web developer": ["html", "css", "javascript"],
            "full stack developer": ["html", "css", "javascript", "react", "node", "mongodb"]
        }

        required = job_roles.get(job_role, [])

        missing = [skill for skill in required if skill not in skills]

        roadmap = [f"Learn {skill}" for skill in missing] if missing else ["You are well prepared 🎉"]

        total = len(required)
        score = int(((total - len(missing)) / total) * 100) if total > 0 else 0

        return jsonify({
            "skills": skills,
            "missing_skills": missing,
            "roadmap": roadmap,
            "score": score
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# IMPORTANT FOR DEPLOYMENT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)