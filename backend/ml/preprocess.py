from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
import pandas as pd
import joblib
import os

os.makedirs("backend/models", exist_ok=True)

def preprocess_data(df, fit_encoders=True):
    if df.shape[0] == 0:
        raise ValueError("DataFrame is empty. Check CSV or filtering.")

    # Categorical columns
    cat_cols = ['Degree', 'Major', 'Industry Preference']
    
    if fit_encoders:
        enc = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        X_cat = enc.fit_transform(df[cat_cols])
        joblib.dump(enc, "backend/models/encoder.pkl")
    else:
        enc = joblib.load("backend/models/encoder.pkl")
        X_cat = enc.transform(df[cat_cols])
    
    # Numeric columns
    num_cols = ['CGPA', 'Experience']
    if fit_encoders:
        scaler = StandardScaler()
        X_num = scaler.fit_transform(df[num_cols])
        joblib.dump(scaler, "backend/models/scaler.pkl")
    else:
        scaler = joblib.load("backend/models/scaler.pkl")
        X_num = scaler.transform(df[num_cols])
    
    # Combine features
    X = pd.concat([
        pd.DataFrame(X_cat, index=df.index),
        pd.DataFrame(X_num, index=df.index)
    ], axis=1)
    
    # Encode target
    if fit_encoders:
        le = LabelEncoder()
        y = le.fit_transform(df['Job Role'])
        joblib.dump(le, "backend/models/label_encoder.pkl")
    else:
        le = joblib.load("backend/models/label_encoder.pkl")
        y = le.transform(df['Job Role'])
    
    return X, y
