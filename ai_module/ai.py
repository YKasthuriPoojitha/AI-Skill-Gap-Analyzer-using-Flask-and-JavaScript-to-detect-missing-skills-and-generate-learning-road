# 📊 Dataset (skills database)
SKILLS_DB = [
    "python", "java", "c", "c++", "sql", "excel", "power bi",
    "html", "css", "javascript", "react", "node", "mongodb",
    "machine learning", "data analysis"
]

# 📊 Job role dataset
JOB_SKILLS = {
    "data analyst": ["python", "sql", "excel", "power bi"],
    "web developer": ["html", "css", "javascript"],
    "full stack developer": ["html", "css", "javascript", "react", "node", "mongodb"],
    "ai engineer": ["python", "machine learning", "data analysis"]
}


# 🧠 Algorithm: Skill Extraction
def extract_skills(resume):
    resume = resume.lower()
    found = []

    for skill in SKILLS_DB:
        if skill in resume:
            found.append(skill)

    return list(set(found))  # remove duplicates


# 🧠 Algorithm: Gap Detection
def get_missing_skills(skills, job_role):
    job_role = job_role.lower()

    if job_role in JOB_SKILLS:
        required = JOB_SKILLS[job_role]
    else:
        # fallback (unknown role)
        required = SKILLS_DB[:5]

    missing = [s for s in required if s not in skills]
    return missing


# 🧠 Algorithm: Metrics Calculation
def calculate_match_score(found, missing):
    total = len(found) + len(missing)

    if total == 0:
        return 0

    return round((len(found) / total) * 100)


# 🧠 Algorithm: Roadmap
def generate_roadmap(missing):
    roadmap = []

    for skill in missing:
        roadmap.append(f"Learn basics of {skill}")
        roadmap.append(f"Practice {skill} projects")
        roadmap.append(f"Build mini project using {skill}")

    return roadmap
def simulate_training():
    print("Training model using predefined dataset...")