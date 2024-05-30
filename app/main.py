from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


load_dotenv()

from .auth import router as auth_router
from .jobs import router as jobs_router


app = FastAPI()

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(jobs_router, prefix="/api", tags=["jobs"])


@app.get("/")
async def root():
    return {"message": "Welcome to the Job Search API"}


@app.options("/{path:path}")
async def options_handler(path: str):
    response = JSONResponse(content=None)
    response.headers[
        "Access-Control-Allow-Methods"
    ] = "POST, GET, OPTIONS, PUT, PATCH, DELETE"
    response.headers[
        "Access-Control-Allow-Headers"
    ] = "Authorization, Content-Type"
    return response
