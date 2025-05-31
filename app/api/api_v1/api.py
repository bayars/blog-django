from fastapi import APIRouter
<<<<<<< HEAD
from app.api.api_v1.endpoints import posts, albums, photos

api_router = APIRouter()
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(albums.router, prefix="/albums", tags=["albums"])
api_router.include_router(photos.router, prefix="/photos", tags=["photos"]) 
=======

from app.api.api_v1.endpoints import posts, projects, gallery

api_router = APIRouter()
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(gallery.router, prefix="/gallery", tags=["gallery"]) 
>>>>>>> 3f6247b (gallery not working, implement the markdown)
