# import fitz  # PyMuPDF
# from io import BytesIO
# import re


# def extract_text_from_pdf(file_bytes: bytes) -> str:
#     text = ""
#     with fitz.open(stream=BytesIO(file_bytes), filetype="pdf") as doc:
#         for page in doc:
#             text += page.get_text()
#     return text.strip()


# def extract_info_from_text(text: str) -> dict:
#     name = text.split("\n")[0] if text else ""

#     email_match = re.search(r"[\w\.-]+@[\w\.-]+", text)
#     email = email_match.group(0) if email_match else ""

#     phone_match = re.search(r"(\+\d{1,3})?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}", text)
#     phone = phone_match.group(0) if phone_match else ""

#     skills_keywords = ["python", "java", "c++", "sql", "javascript", "react", "node", "django", "fastapi"]
#     skills = [kw for kw in skills_keywords if kw.lower() in text.lower()]

#     return {
#         "name": name,
#         "email": email,
#         "phone": phone,
#         "skills": skills
#     }


import fitz  # PyMuPDF
from io import BytesIO
import re


def extract_text_from_pdf(file_bytes: bytes) -> str:
    text = ""
    with fitz.open(stream=BytesIO(file_bytes), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()


def extract_section(text: str, section_name: str) -> str:
    # Pattern to match section header (case-insensitive), with optional colon or line breaks after it
    # Then capture everything non-greedily until the next section header or end of text
    pattern = rf"{section_name}\s*[:\n\r]+([\s\S]*?)(?=\n[A-Z][^\n]*\n|$)"
    # Explanation:
    # - {section_name} followed by optional spaces and ':' or line breaks
    # - Capture any characters including newlines ([\s\S]*?), non-greedy
    # - Stop when you see a new line that starts with capital letter (likely next section header) or end of string

    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ""

def parse_bullets(section_text: str) -> list[str]:
    lines = section_text.split('\n')
    bullets = [line.strip("-*0123456789. \t") for line in lines if line.strip()]
    return [b for b in bullets if b]  # filter out empty lines


def extract_info_from_text(text: str) -> dict:
    name = text.split("\n")[0] if text else ""

    email_match = re.search(r"[\w\.-]+@[\w\.-]+", text)
    email = email_match.group(0) if email_match else ""

    phone_match = re.search(r"(\+\d{1,3})?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}", text)
    phone = phone_match.group(0) if phone_match else ""

    skills_keywords = ["python", "java", "c++", "sql", "javascript", "react", "node", "django", "fastapi"]
    skills = [kw for kw in skills_keywords if kw.lower() in text.lower()]

    education = extract_section(text, "Education")
    experience = extract_section(text, "Work experience")
    projects = extract_section(text, "Projects")
    certifications = extract_section(text, "Certifications")

    linkedin_match = re.search(r"https?://(www\.)?linkedin\.com/in/[\w-]+", text)
    github_match = re.search(r"https?://(www\.)?github\.com/[\w-]+", text)

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "education": education,
        "experience": experience,
        "projects": projects,
        "certifications": certifications,
        "linkedin": linkedin_match.group(0) if linkedin_match else "",
        "github": github_match.group(0) if github_match else ""
    }
