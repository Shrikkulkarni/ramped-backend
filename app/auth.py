import datetime
import os

import jwt
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, Request
from passlib.context import CryptContext

from .database import db
from .schemas import UserCreate, UserLogin


load_dotenv()

router = APIRouter()

users_collection = db.users
blacklisted_tokens = set()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(email: str):
    expire = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    encoded_jwt = jwt.encode(
        {"sub": email, "exp": expire}, SECRET_KEY, algorithm="HS256"
    )
    return encoded_jwt


def verify_token(request: Request):
    token = request.headers.get("Authorization")
    if token is None or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid or missing token")

    token = token[len("Bearer ") :]  # Remove 'Bearer ' prefix
    if token in blacklisted_tokens:
        raise HTTPException(
            status_code=401, detail="Token has been invalidated"
        )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.post("/signup")
async def sign_up(user: UserCreate):
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    users_collection.insert_one(
        {"email": user.email, "password": hashed_password}
    )
    return {"message": "User created successfully"}


@router.post("/login")
async def log_in(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    token = create_access_token(user.email)
    return {"access_token": token}


@router.post("/logout")
async def log_out(request: Request):
    token = request.headers.get("Authorization")
    if token is None or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid or missing token")

    token = token[len("Bearer ") :]  # Remove 'Bearer ' prefix
    blacklisted_tokens.add(token)
    return {"message": "Logged out successfully"}
