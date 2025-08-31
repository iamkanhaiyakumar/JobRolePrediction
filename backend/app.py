from fastapi import FastAPI
from backend.database import engine, Base
from backend.routes import auth_routes, prediction_routes, admin_routes  # removed user_routes
import uvicorn
import os
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Job Role Prediction API")

# Mount frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# Create DB tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(prediction_routes.router, prefix="/predict", tags=["Prediction"])
app.include_router(admin_routes.router, prefix="/admin", tags=["Admin"])
