from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from PyPDF2 import PdfReader
import os

app = Flask(__name__)
CORS(app)

# 🔥 Extract text from PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


# 🔥 NLP skill extraction
def extract_skills(text):
    text = text.lower()

    skills_list = [
        "python", "java", "c", "c++", "html", "css",
        "javascript", "react", "node", "sql",
        "excel", "power bi", "machine learning"
    ]

    found = [skill for skill in skills_list if skill in text]
    return list(set(found))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        # ✅ HANDLE PDF OR TEXT INPUT
        if request.content_type and "multipart/form-data" in request.content_type:
            file = request.files.get("file")
            job_role = request.form.get("jobRole", "").lower()

            if file:
                resume = extract_text_from_pdf(file)
            else:
                resume = ""

        else:
            data = request.get_json(silent=True) or {}
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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)