from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.database import SessionLocal, User
from backend.utils.jwt_handler import create_access_token
import bcrypt
import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

router = APIRouter()

class SignupModel(BaseModel):
    name: str
    email: str
    password: str

class LoginModel(BaseModel):
    email: str
    password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(user: SignupModel, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        return {"message": "User already exists"}
    hashed_pw = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(name=user.name, email=user.email, password=hashed_pw.decode('utf-8'))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: LoginModel, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        return {"message": "User not found"}
    if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.password.encode('utf-8')):
        return {"message": "Incorrect password"}
    token_data = {"user_id": db_user.id, "role": db_user.role}
    token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(data=token_data, secret_key=SECRET_KEY, algorithm=ALGORITHM, expires_delta=token_expires)
    return {"message": "Login successful", "token": token}
