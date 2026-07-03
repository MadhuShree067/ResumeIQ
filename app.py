from flask import Flask, render_template, request
from parser import extract_text
from extractor import extract_skills
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]
    job_description = request.form["job_description"]

    if not file:
        return "No file selected"

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    # Extract resume text
    resume_text = extract_text(filepath)

    # Extract skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    # Resume Score
    score = min(len(resume_skills) * 10, 100)

    # Matching Skills
    matched_skills = [
        skill for skill in resume_skills
        if skill in job_skills
    ]

    # Missing Skills
    missing_skills = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    # Match Score
    if len(job_skills) > 0:
        match_score = int(
            (len(matched_skills) / len(job_skills)) * 100
        )
    else:
        match_score = 0

    # Recommendations
    recommendations = []

    for skill in missing_skills:
        recommendations.append(
            f"Learn {skill.title()} to improve your profile."
        )

    return render_template(
        "result.html",
        score=score,
        match_score=match_score,
        resume_skills=resume_skills,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)