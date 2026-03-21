from flask import Flask, render_template, request, jsonify
import os
import re
from PyPDF2 import PdfReader

app = Flask(__name__)

# 🔥 Extract text from PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# 🔥 NLP Skill Extraction
def extract_skills(text):
    text = text.lower()

    skill_keywords = [
        "python", "java", "c", "c++", "html", "css",
        "javascript", "react", "node", "sql",
        "excel", "power bi", "machine learning"
    ]

    found = []

    for skill in skill_keywords:
        if skill in text:
            found.append(skill)

    return list(set(found))


# 🏠 Home
@app.route("/")
def home():
    return render_template("index.html")


# 🔍 Analyze
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        job_role = ""

        # 📄 If PDF uploaded
        if 'file' in request.files and request.files['file'].filename != "":
            file = request.files['file']
            resume = extract_text_from_pdf(file)
            job_role = request.form.get("jobRole", "").lower()
        else:
            data = request.get_json()
            resume = data.get("resume", "")
            job_role = data.get("jobRole", "").lower()

        # 🔥 Extract skills
        skills = extract_skills(resume)

        # 🎯 Job roles
        job_roles = {
            "full stack developer": ["html", "css", "javascript", "react", "node"],
            "data analyst": ["python", "sql", "excel", "power bi"],
            "ml engineer": ["python", "machine learning", "sql"]
        }

        required = job_roles.get(job_role, [])

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


# 🚀 Run
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)