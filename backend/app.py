from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, User, Resume, JobDescription
from utils import extract_text_from_resume, match_resume_with_jd
from email_service import send_email
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/upload-resume", methods=["POST"])
def upload_resume():
    email = request.form.get("email")
    file = request.files["resume"]
    
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email)
        db.session.add(user)
        db.session.commit()
    
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    resume_text = extract_text_from_resume(file_path)
    
    resume = Resume(user_id=user.id, resume_text=resume_text)
    db.session.add(resume)
    db.session.commit()
    
    return jsonify({"message": "Resume uploaded successfully"})

@app.route("/upload-jd", methods=["POST"])
def upload_jd():
    email = request.form.get("email")
    jd_text = request.form.get("job_description")
    
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    job_desc = JobDescription(user_id=user.id, jd_text=jd_text)
    db.session.add(job_desc)
    db.session.commit()
    
    return jsonify({"message": "Job description uploaded successfully"})

@app.route("/match", methods=["POST"])
def match_resume_jd():
    email = request.form.get("email")
    
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    resume = Resume.query.filter_by(user_id=user.id).first()
    job_desc = JobDescription.query.filter_by(user_id=user.id).first()
    
    if not resume or not job_desc:
        return jsonify({"error": "Resume or job description missing"}), 400
    
    match_score, matched_words, missing_words = match_resume_with_jd(resume.resume_text, job_desc.jd_text)
    send_email(email, match_score)
    
    return jsonify({
        "match_score": match_score,
        "matched_words": matched_words,
        "missing_words": missing_words
    })

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
