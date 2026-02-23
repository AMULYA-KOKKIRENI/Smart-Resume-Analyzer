def match_skills(resume_skills, job_skills):
    matched = resume_skills.intersection(job_skills)
    missing = job_skills - resume_skills
    score = (len(matched) / len(job_skills)) * 100 if job_skills else 0
    return matched, missing, round(score, 2)
