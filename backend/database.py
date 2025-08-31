from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
import sys

# Load environment variables
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
print("Connecting to:", DATABASE_URL)

try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    Base = declarative_base()
    print("✅ MySQL connection successful!")
except Exception as e:
    print(f"❌ Could not connect to MySQL: {e}")
    sys.exit(1)

# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(200))
    role = Column(String(20), default="user")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    educations = relationship("Education", back_populates="user")
    predictions = relationship("JobPrediction", back_populates="user")

class Education(Base):
    __tablename__ = "education_details"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    degree = Column(String(50))
    specialization = Column(String(50))
    cgpa = Column(Float)
    certifications = Column(String(200))
    user = relationship("User", back_populates="educations")

class JobPrediction(Base):
    __tablename__ = "job_predictions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    job = Column(String(100))
    confidence = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship("User", back_populates="predictions")

class AdminLog(Base):
    __tablename__ = "admin_logs"
    id = Column(Integer, primary_key=True, index=True)
    action = Column(String(200))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# Create tables
try:
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully!")
except Exception as e:
    print(f"❌ Error creating tables: {e}")
    sys.exit(1)
