import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from backend.ml.preprocess import preprocess_data
import joblib
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ensure models folder exists
os.makedirs("backend/models", exist_ok=True)

# Load CSV
df = pd.read_csv("backend/data/training_data.csv")

# Only include employed candidates for training
# df = df[df['Employed'] == 1]

# Preprocess
X, y = preprocess_data(df, fit_encoders=True)

# Train Random Forest
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)

# Save trained model
joblib.dump(model, "backend/models/job_model.pkl")
print("Model trained and saved successfully!")
