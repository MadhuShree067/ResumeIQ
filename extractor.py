skills_list = [
    "python",
    "sql",
    "html",
    "css",
    "javascript",
    "git",
    "github",
    "flask",
    "machine learning"
]

def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills