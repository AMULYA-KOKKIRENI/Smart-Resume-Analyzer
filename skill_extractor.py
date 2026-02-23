import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills(text, skills_list):
    doc = nlp(text)
    extracted_skills = set()

    for token in doc:
        if token.text in skills_list:
            extracted_skills.add(token.text)

    return extracted_skills
