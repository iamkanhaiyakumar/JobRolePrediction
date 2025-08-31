# backend/app.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.database import engine, Base
from backend.routes import auth_routes, user_routes, prediction_routes, admin_routes, visualization_routes

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Role Prediction API")

# Mount frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# Include API routes
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(user_routes.router, prefix="/user", tags=["User"])
app.include_router(prediction_routes.router, prefix="/predict", tags=["Prediction"])
app.include_router(admin_routes.router, prefix="/admin", tags=["Admin"])
app.include_router(visualization_routes.router, prefix="/visual", tags=["Visualization"])
