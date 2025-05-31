from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
<<<<<<< HEAD
from pathlib import Path
=======
>>>>>>> 3f6247b (gallery not working, implement the markdown)

from app.core.config import settings
from app.api.api_v1.api import api_router
from app.db.session import engine
from app.db.base import Base

<<<<<<< HEAD
# Create media directory if it doesn't exist
media_dir = Path("media")
media_dir.mkdir(exist_ok=True)

# Create FastAPI app
=======
# Create database tables
Base.metadata.create_all(bind=engine)

>>>>>>> 3f6247b (gallery not working, implement the markdown)
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
<<<<<<< HEAD
    allow_origins=["*"],  # In production, replace with specific origins
=======
    allow_origins=settings.BACKEND_CORS_ORIGINS,
>>>>>>> 3f6247b (gallery not working, implement the markdown)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
# Mount static files
app.mount("/media", StaticFiles(directory="media"), name="media")

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Blog API"} 
=======
# Create necessary directories if they don't exist
os.makedirs("staticfiles", exist_ok=True)
os.makedirs("media", exist_ok=True)
os.makedirs("media/albums", exist_ok=True)
os.makedirs("media/series", exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="staticfiles"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR) 
>>>>>>> 3f6247b (gallery not working, implement the markdown)
