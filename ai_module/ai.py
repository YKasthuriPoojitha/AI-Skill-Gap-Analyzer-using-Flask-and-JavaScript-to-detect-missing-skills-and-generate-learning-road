def extract_skills(resume):
    # Simple skill extraction (based on keywords)
    resume = resume.lower()

    known_skills = [
        "python", "java", "c", "c++", "javascript", "html", "css",
        "react", "node", "flask", "django", "sql", "mongodb"
    ]

    skills = []

    for skill in known_skills:
        if skill in resume:
            skills.append(skill)

    return skills


def get_missing_skills(skills, job_role):
    job_role = job_role.lower()

    role_requirements = {
        "full stack developer": ["html", "css", "javascript", "react", "node", "mongodb"],
        "backend developer": ["python", "flask", "django", "sql"],
        "frontend developer": ["html", "css", "javascript", "react"],
        "data scientist": ["python", "sql", "machine learning"],
        "ai engineer": ["python", "machine learning", "deep learning"]
    }

    required = role_requirements.get(job_role, [])

    missing = []
    for skill in required:
        if skill not in skills:
            missing.append(skill)

    return missing


def generate_roadmap(missing_skills):
    roadmap = []

    for skill in missing_skills:
        roadmap.append(f"Learn {skill}")

    if not roadmap:
        return ["You are well prepared! 🎉"]

    return roadmap


def calculate_match_score(skills, missing_skills):
    total = len(skills) + len(missing_skills)

    if total == 0:
        return 0

    score = (len(skills) / total) * 100
    return round(score, 2)