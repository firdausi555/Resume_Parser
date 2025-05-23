# from pydantic import BaseModel
# from typing import List

# class ResumeParsedData(BaseModel):
#     name: str
#     email: str
#     phone: str
#     skills: List[str]

class ResumeParsedData(BaseModel):
    name: str
    email: str
    phone: str
    skills: List[str]
    education: Optional[str]
    experience: Optional[str]
    projects: Optional[str]
    certifications: Optional[str]
    linkedin: Optional[str]
    github: Optional[str]
