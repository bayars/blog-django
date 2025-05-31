from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path

from app.core.config import settings
from app.api.api_v1.api import api_router
from app.db.session import engine
from app.db.base import Base

# Create media directory if it doesn't exist
media_dir = Path("media")
media_dir.mkdir(exist_ok=True)

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/media", StaticFiles(directory="media"), name="media")

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Blog API"} 