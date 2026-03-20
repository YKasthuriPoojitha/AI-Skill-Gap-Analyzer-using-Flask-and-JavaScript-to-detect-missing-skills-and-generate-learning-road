def extract_skills(resume):
    SKILLS_DB = [
        "python", "java", "c", "c++", "sql", "excel", "power bi",
        "html", "css", "javascript", "react", "node", "mongodb",
        "machine learning", "data analysis"
    ]

    resume = resume.lower()
    found = []

    for skill in SKILLS_DB:
        if skill in resume:
            found.append(skill)

    return found


def get_missing_skills(skills, job_role):
    JOB_SKILLS = {
        "data analyst": ["python", "sql", "excel", "power bi"],
        "web developer": ["html", "css", "javascript"],
        "full stack developer": ["html", "css", "javascript", "react", "node", "mongodb"],
        "software engineer": ["java", "python", "c++", "data structures"],
        "ai engineer": ["python", "machine learning", "data analysis"]
    }

    job_role = job_role.lower()

    # 👉 If role exists
    if job_role in JOB_SKILLS:
        required = JOB_SKILLS[job_role]
    else:
        # 👉 If role unknown → suggest common tech skills
        required = ["python", "sql", "html", "css", "javascript"]

    missing = [s for s in required if s not in skills]

    return missing


def generate_roadmap(missing):
    roadmap = []

    for skill in missing:
        roadmap.append(f"Learn basics of {skill}")
        roadmap.append(f"Practice {skill} projects")
        roadmap.append(f"Build mini project using {skill}")

    return roadmap