import re
import docx2txt
import pdfplumber
import os
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load ML model & vectorizer
model = pickle.load(open(os.path.join(BASE_DIR, "career_model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))

required_skills = {
    "Data Science": ["Python", "Pandas", "Machine Learning", "SQL", "Statistics"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Django"],
    "HR": ["Recruitment", "Payroll", "Employee Relations"]
}

def extract_text(file_path):
    text = ""
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif file_path.endswith(".docx"):
        text = docx2txt.process(file_path)
    return text

def extract_info(text):
    """Extract Name, Email, DOB, GitHub, LinkedIn"""
    info = {}

    # Email
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    info['email'] = emails[0] if emails else "Not Found"

    # DOB patterns
    dob_patterns = [
        r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',                # 31/12/1995 or 31-12-1995
        r'\b\d{1,2}\.\d{1,2}\.\d{2,4}\b',                    # 31.12.1995
        r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}\b'  # December 31, 1995
    ]
    dob = None
    for pattern in dob_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            dob = match.group()
            break
    info['dob'] = dob if dob else "Not Found"

    # LinkedIn
    linkedin = re.findall(r'(https?://www\.linkedin\.com/in/[A-Za-z0-9_-]+)', text)
    info['linkedin'] = linkedin[0] if linkedin else "Not Found"

    # GitHub
    github = re.findall(r'(https?://github\.com/[A-Za-z0-9_-]+)', text)
    info['github'] = github[0] if github else "Not Found"

    # Name (first line before email/DOB heuristics)
    lines = text.strip().split("\n")
    name = lines[0] if lines else "Not Found"
    info['name'] = name

    return info

def predict_career(text):
    X_vect = vectorizer.transform([text])
    career = model.predict(X_vect)[0]
    return career

def recommend_skills(text, career_field):
    skills = required_skills[career_field]
    missing = [skill for skill in skills if skill.lower() not in text.lower()]
    return missing

def calculate_score(text, career_field):
    skills = required_skills[career_field]
    present = [skill for skill in skills if skill.lower() in text.lower()]
    return round((len(present)/len(skills))*100, 2)

def recommend_courses(skills_missing):
    # Simple Udemy + YouTube links
    courses = []
    for skill in skills_missing:
        courses.append(f"Udemy: https://www.udemy.com/topic/{skill.lower()}/")
        courses.append(f"YouTube: https://www.youtube.com/results?search_query={skill}+tutorial")
    return courses
