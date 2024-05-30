from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str


class Job(BaseModel):
    job_name: str
    company_name: str
