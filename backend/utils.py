import re
from PyPDF2 import PdfReader
import docx2txt

def extract_text_from_resume(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return docx2txt.process(file_path)
    return ""

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def match_resume_with_jd(resume_text, jd_text):
    resume_words = set(re.findall(r'\b\w+\b', resume_text.lower()))
    jd_words = set(re.findall(r'\b\w+\b', jd_text.lower()))
    matched_words = resume_words & jd_words
    missing_words = jd_words - resume_words
    match_score = round((len(matched_words) / len(jd_words)) * 100, 2) if jd_words else 0
    return match_score, list(matched_words), list(missing_words)
