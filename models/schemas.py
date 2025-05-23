from pydantic import BaseModel
from typing import List

class ResumeParsedData(BaseModel):
    name: str
    email: str
    phone: str
    skills: List[str]