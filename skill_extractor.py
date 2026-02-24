import re

SKILLS_DB = [
    "python", "java", "c", "c++", "sql", "html", "css", "javascript",
    "machine learning", "deep learning", "data science",
    "django", "flask", "streamlit",
    "git", "github",
    "linux", "windows",
    "cloud", "aws", "azure", "gcp",
    "networking", "cybersecurity",
    "react", "node", "mysql"
]

def extract_skills(text):
    text = text.lower()
    skills_found = []

    for skill in SKILLS_DB:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            skills_found.append(skill)

    return list(set(skills_found))
