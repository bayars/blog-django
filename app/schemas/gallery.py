from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class PhotoBase(BaseModel):
    title: str
    file_path: str
    order: Optional[int] = 0

class PhotoCreate(PhotoBase):
    pass

class Photo(PhotoBase):
    id: int
    series_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class PhotoSeriesBase(BaseModel):
    title: str
    description: Optional[str] = None

class PhotoSeriesCreate(PhotoSeriesBase):
    pass

class PhotoSeriesUpdate(PhotoSeriesBase):
    title: Optional[str] = None

class PhotoSeries(PhotoSeriesBase):
    id: int
    slug: str
    album_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    photos: List[Photo] = []

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

class Album(AlbumBase):
    id: int
    slug: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    series: List[PhotoSeries] = []

    class Config:
        from_attributes = True 