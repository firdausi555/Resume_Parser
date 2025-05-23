import fitz  # PyMuPDF
from io import BytesIO
import re


def extract_text_from_pdf(file_bytes: bytes) -> str:
    text = ""
    with fitz.open(stream=BytesIO(file_bytes), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()


def extract_info_from_text(text: str) -> dict:
    name = text.split("\n")[0] if text else ""

    email_match = re.search(r"[\w\.-]+@[\w\.-]+", text)
    email = email_match.group(0) if email_match else ""

    phone_match = re.search(r"(\+\d{1,3})?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}", text)
    phone = phone_match.group(0) if phone_match else ""

    skills_keywords = ["python", "java", "c++", "sql", "javascript", "react", "node", "django", "fastapi"]
    skills = [kw for kw in skills_keywords if kw.lower() in text.lower()]

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills
    }
