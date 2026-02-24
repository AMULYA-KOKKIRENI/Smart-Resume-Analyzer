import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from matcher import match_skills

# Load skills list
with open("data/skills_list.txt", "r") as f:
    skills_list = [skill.strip().lower() for skill in f.read().split(",")]

st.set_page_config(page_title="Smart Resume Analyzer")

st.title("🧠 Smart Resume Analyzer")
st.write("Upload your resume and compare it with a job description")

# Upload resume
resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

# Job description input
job_description = st.text_area("📝 Paste Job Description")

if resume_file and job_description:
    # Extract text
    resume_text = extract_text_from_pdf(resume_file)
    job_text = job_description.lower()

    # Extract skills
     resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    # Match skills
    matched, missing, score = match_skills(resume_skills, job_skills)

    st.subheader("📊 Results")
    st.success(f"Match Score: {score}%")

    col1, col2 = st.columns(2)

    with col1:
        st.write("✅ Matched Skills")
        st.write(list(matched) if matched else "None")

    with col2:
        st.write("❌ Missing Skills")
        st.write(list(missing) if missing else "None")
else:
    st.info("Please upload a resume and paste a job description.")
