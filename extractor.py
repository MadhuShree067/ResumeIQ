skills_list = [
    "python",
    "sql",
    "html",
    "css",
    "javascript",
    "git",
    "github",
    "flask",
    "django",
    "mysql",
    "machine learning",
    "data analysis",
    "aws",
    "docker",
    "kubernetes",
    "numpy",
    "pandas",
    "excel"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill in text:
            found_skills.append(skill)

    return found_skills