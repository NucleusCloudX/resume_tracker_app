from flask import Flask, request, jsonify
import os
from utils import extract_text_from_resume, match_resume_with_jd
from email_service import send_email
from models import db, User, Resume, JobDescription

app = Flask(__name__)
app.config.from_object("config.Config")
db.init_app(app)

@app.route("/upload-resume", methods=["POST"])
def upload_resume():
    try:
        # Check for email
        email = request.form.get("email")
        if not email:
            return jsonify({"error": "Email is required"}), 400

        # Check for file
        if "resume" not in request.files:
            return jsonify({"error": "No resume file part in the request"}), 400

        file = request.files["resume"]
        if file.filename == "":
            return jsonify({"error": "No file selected for uploading"}), 400

        # Save the file
        uploads_dir = os.path.join(os.getcwd(), "uploads")
        os.makedirs(uploads_dir, exist_ok=True)
        file_path = os.path.join(uploads_dir, file.filename)
        file.save(file_path)

        # Process the resume
        resume_text = extract_text_from_resume(file_path)
        
        # Store resume (for example)
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(email=email)
            db.session.add(user)
            db.session.commit()

        resume = Resume(user_id=user.id, resume_text=resume_text)
        db.session.add(resume)
        db.session.commit()

        return jsonify({"message": "Resume uploaded successfully"}), 200

    except Exception as e:
        app.logger.error(f"Error uploading resume: {str(e)}")
        return jsonify({"error": "Failed to upload resume", "details": str(e)}), 500

@app.route("/upload-jd", methods=["POST"])
def upload_jd():
    try:
        email = request.form.get("email")
        jd_text = request.form.get("job_description")
        if not email or not jd_text:
            return jsonify({"error": "Email and Job Description are required"}), 400

        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        job_desc = JobDescription(user_id=user.id, jd_text=jd_text)
        db.session.add(job_desc)
        db.session.commit()

        # Optionally perform matching and send email here.
        match_score, matched, missing = match_resume_with_jd(resume_text=resume_text, jd_text=jd_text)
        send_email(email, match_score)

        return jsonify({"message": "Job description uploaded and processed", "match_score": match_score}), 200

    except Exception as e:
        app.logger.error(f"Error uploading job description: {str(e)}")
        return jsonify({"error": "Failed to upload job description", "details": str(e)}), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
