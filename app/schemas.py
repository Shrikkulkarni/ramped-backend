from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class JobResponse(BaseModel):
    job_name: str
    company_name: str
