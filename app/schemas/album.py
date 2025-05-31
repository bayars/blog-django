from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PhotoBase(BaseModel):
    title: str
    description: Optional[str] = None

class PhotoCreate(PhotoBase):
    pass

class PhotoUpdate(PhotoBase):
    title: Optional[str] = None

class Photo(PhotoBase):
    id: int
    image: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    album_id: int

    class Config:
        from_attributes = True

class AlbumBase(BaseModel):
    title: str
    description: Optional[str] = None
    cover_image: Optional[str] = None

class AlbumCreate(AlbumBase):
    pass

class AlbumUpdate(AlbumBase):
    title: Optional[str] = None
    description: Optional[str] = None
    cover_image: Optional[str] = None

class Album(AlbumBase):
    id: int
    slug: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    photos: List[Photo] = []

    class Config:
        from_attributes = True 