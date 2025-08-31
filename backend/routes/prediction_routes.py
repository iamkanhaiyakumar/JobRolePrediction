from fastapi import APIRouter, Depends, Header
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.database import SessionLocal, JobPrediction
from backend.utils.jwt_handler import decode_access_token
import joblib
import pandas as pd
import numpy as np

router = APIRouter()

model = joblib.load("backend/models/job_model.pkl")
scaler = joblib.load("backend/models/scaler.pkl")
encoder = joblib.load("backend/models/encoder.pkl")
label_encoder = joblib.load("backend/models/label_encoder.pkl")

class EducationInput(BaseModel):
    Degree: str
    Major: str
    CGPA: float
    Experience: float
    Skills: str = ""
    Certifications: str = ""
    Industry_Preference: str = ""

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Header(...)):
    payload = decode_access_token(token.split(" ")[1])
    if payload:
        return payload
    return None

@router.post("/predict")
def predict(input: EducationInput, db: Session = Depends(get_db), token: str = Header(...)):
    user = get_current_user(token)
    if not user:
        return {"message": "Invalid token"}

    df = pd.DataFrame([{
        'Degree': input.Degree,
        'Major': input.Major,
        'CGPA': input.CGPA,
        'Experience': input.Experience,
        'Industry Preference': input.Industry_Preference
    }])

    cat_cols = ['Degree', 'Major', 'Industry Preference']
    X_cat = encoder.transform(df[cat_cols])
    num_cols = ['CGPA', 'Experience']
    X_num = scaler.transform(df[num_cols])
    X = np.hstack([X_cat, X_num])

    probs = model.predict_proba(X)[0]
    classes = model.classes_

    top_idx = np.argsort(probs)[::-1][:3]
    predictions = []
    for i in top_idx:
        predictions.append({
            "job": label_encoder.inverse_transform([classes[i]])[0],
            "confidence": round(probs[i]*100, 2)
        })

    for pred in predictions:
        new_pred = JobPrediction(user_id=user["user_id"], job=pred["job"], confidence=pred["confidence"])
        db.add(new_pred)
    db.commit()

    return {"predictions": predictions}
