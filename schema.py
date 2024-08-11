# schema.py
from pydantic import BaseModel, HttpUrl, EmailStr
from typing import List, Optional

class Location(BaseModel):
    address: Optional[str]
    postalCode: Optional[str]
    city: Optional[str]
    countryCode: Optional[str]
    region: Optional[str]

class Profile(BaseModel):
    network: str
    username: str
    url: Optional[HttpUrl]

class Basics(BaseModel):
    name: str
    label: Optional[str]
    picture: Optional[HttpUrl]
    email: EmailStr
    phone: Optional[str]
    website: Optional[HttpUrl]
    summary: Optional[str]
    location: Optional[Location]
    profiles: Optional[List[Profile]]

class Work(BaseModel):
    company: str
    position: str
    website: Optional[HttpUrl]
    startDate: str
    endDate: Optional[str]
    summary: Optional[str]
    highlights: Optional[List[str]]

class Volunteer(BaseModel):
    organization: str
    position: str
    website: Optional[HttpUrl]
    startDate: str
    endDate: Optional[str]
    summary: Optional[str]
    highlights: Optional[List[str]]

class Education(BaseModel):
    institution: str
    area: str
    studyType: str
    startDate: str
    endDate: Optional[str]
    gpa: Optional[str]
    courses: Optional[List[str]]

class Award(BaseModel):
    title: str
    date: str
    awarder: str
    summary: Optional[str]

class Publication(BaseModel):
    name: str
    publisher: str
    releaseDate: str
    website: Optional[HttpUrl]
    summary: Optional[str]

class Skill(BaseModel):
    name: str
    level: Optional[str]
    keywords: Optional[List[str]]

class Language(BaseModel):
    language: str
    fluency: Optional[str]

class Interest(BaseModel):
    name: str
    keywords: Optional[List[str]]

class Reference(BaseModel):
    name: str
    reference: str

class ResumeSchema(BaseModel):
    basics: Optional[Basics]
    work: Optional[List[Work]]
    volunteer: Optional[List[Volunteer]]
    education: Optional[List[Education]]
    awards: Optional[List[Award]]
    publications: Optional[List[Publication]]
    skills: Optional[List[Skill]]
    languages: Optional[List[Language]]
    interests: Optional[List[Interest]]
    references: Optional[List[Reference]]