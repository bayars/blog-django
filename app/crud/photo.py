from typing import List, Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.photo import Photo
from app.schemas.album import PhotoCreate, PhotoUpdate

class CRUDPhoto(CRUDBase[Photo, PhotoCreate, PhotoUpdate]):
    def get_by_album(
        self, db: Session, *, album_id: int, skip: int = 0, limit: int = 100
    ) -> List[Photo]:
        return (
            db.query(Photo)
            .filter(Photo.album_id == album_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create(self, db: Session, *, obj_in: PhotoCreate, album_id: int) -> Photo:
        db_obj = Photo(
            title=obj_in.title,
            description=obj_in.description,
            album_id=album_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

photo = CRUDPhoto(Photo) 