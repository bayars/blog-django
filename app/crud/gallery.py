from typing import List, Optional
from sqlalchemy.orm import Session
from slugify import slugify

from app.crud.base import CRUDBase
from app.models.gallery import Album, PhotoSeries, Photo
from app.schemas.gallery import AlbumCreate, AlbumUpdate, PhotoSeriesCreate, PhotoSeriesUpdate, PhotoCreate

class CRUDAlbum(CRUDBase[Album, AlbumCreate, AlbumUpdate]):
    def create_with_slug(self, db: Session, *, obj_in: AlbumCreate) -> Album:
        obj_in_data = obj_in.dict()
        obj_in_data["slug"] = slugify(obj_in_data["title"])
        db_obj = Album(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_slug(self, db: Session, *, slug: str) -> Optional[Album]:
        return db.query(Album).filter(Album.slug == slug).first()

album = CRUDAlbum(Album)

class CRUDPhotoSeries(CRUDBase[PhotoSeries, PhotoSeriesCreate, PhotoSeriesUpdate]):
    def create_with_slug(self, db: Session, *, obj_in: PhotoSeriesCreate, album_id: int) -> PhotoSeries:
        obj_in_data = obj_in.dict()
        obj_in_data["slug"] = slugify(obj_in_data["title"])
        obj_in_data["album_id"] = album_id
        db_obj = PhotoSeries(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_slug(self, db: Session, *, slug: str) -> Optional[PhotoSeries]:
        return db.query(PhotoSeries).filter(PhotoSeries.slug == slug).first()

    def get_by_album(
        self, db: Session, *, album_id: int, skip: int = 0, limit: int = 100
    ) -> List[PhotoSeries]:
        return (
            db.query(PhotoSeries)
            .filter(PhotoSeries.album_id == album_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

photo_series = CRUDPhotoSeries(PhotoSeries)

class CRUDPhoto(CRUDBase[Photo, PhotoCreate, PhotoCreate]):
    def create_multi(
        self, db: Session, *, series_id: int, photos_in: List[PhotoCreate]
    ) -> List[Photo]:
        db_photos = []
        for i, photo_in in enumerate(photos_in):
            photo_data = photo_in.dict()
            photo_data["series_id"] = series_id
            photo_data["order"] = i
            db_photo = Photo(**photo_data)
            db.add(db_photo)
            db_photos.append(db_photo)
        db.commit()
        for db_photo in db_photos:
            db.refresh(db_photo)
        return db_photos

    def get_by_series(
        self, db: Session, *, series_id: int, skip: int = 0, limit: int = 100
    ) -> List[Photo]:
        return (
            db.query(Photo)
            .filter(Photo.series_id == series_id)
            .order_by(Photo.order)
            .offset(skip)
            .limit(limit)
            .all()
        )

photo = CRUDPhoto(Photo) 