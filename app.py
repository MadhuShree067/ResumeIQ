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

    if file:

        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)

        # Extract text from PDF
        resume_text = extract_text(filepath)

        # Extract skills
        skills = extract_skills(resume_text)

        # Calculate score
        score = len(skills) * 10

        if score > 100:
            score = 100

        return f"""
        <html>
        <body style="font-family: Arial; padding: 20px;">

        <h1>Resume Analysis</h1>

        <h2>Resume Score: {score}/100</h2>

        <h2>Skills Found:</h2>

        <ul>
        {''.join([f'<li>{skill}</li>' for skill in skills])}
        </ul>

        <hr>

        <h2>Resume Text:</h2>

        <pre>{resume_text}</pre>

        </body>
        </html>
        """

    return "No file selected"


if __name__ == "__main__":
    app.run(debug=True)