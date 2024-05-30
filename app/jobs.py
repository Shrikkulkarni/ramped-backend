from typing import List

from fastapi import APIRouter, Depends, Request

from .auth import verify_token
from .database import db
from .schemas import JobResponse


router = APIRouter()

jobs_collection = db.jobs


@router.get("/jobs", response_model=List[JobResponse])
async def get_jobs(
    title: str, request: Request, token: dict = Depends(verify_token)
):
    jobs = jobs_collection.find(
        {"job_name": {"$regex": title, "$options": "i"}}
    )
    return [
        {"job_name": job["job_name"], "company_name": job["company_name"]}
        for job in jobs
    ]
