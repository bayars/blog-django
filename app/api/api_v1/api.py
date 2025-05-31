from fastapi import APIRouter
from app.api.api_v1.endpoints import posts, albums, photos

api_router = APIRouter()
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(albums.router, prefix="/albums", tags=["albums"])
api_router.include_router(photos.router, prefix="/photos", tags=["photos"]) 