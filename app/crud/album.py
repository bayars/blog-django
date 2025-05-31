from typing import List, Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.album import Album
from app.schemas.album import AlbumCreate, AlbumUpdate
from slugify import slugify

class CRUDAlbum(CRUDBase[Album, AlbumCreate, AlbumUpdate]):
    def get_by_slug(self, db: Session, *, slug: str) -> Optional[Album]:
        return db.query(Album).filter(Album.slug == slug).first()

    def create(self, db: Session, *, obj_in: AlbumCreate) -> Album:
        db_obj = Album(
            title=obj_in.title,
            slug=slugify(obj_in.title),
            description=obj_in.description,
            cover_image=obj_in.cover_image
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: Album,
        obj_in: AlbumUpdate
    ) -> Album:
        update_data = obj_in.dict(exclude_unset=True)
        if "title" in update_data:
            update_data["slug"] = slugify(update_data["title"])
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_photos(self, db: Session, *, album_id: int, skip: int = 0, limit: int = 100) -> List[Album]:
        return (
            db.query(Album)
            .filter(Album.id == album_id)
            .first()
            .photos[skip : skip + limit]
        )

album = CRUDAlbum(Album) 