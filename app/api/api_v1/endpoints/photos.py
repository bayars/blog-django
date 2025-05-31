from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.crud import photo as crud_photo
from app.schemas.album import Photo, PhotoCreate, PhotoUpdate
from app.db.session import get_db
from app.core.utils import save_upload_file

router = APIRouter()

@router.get("/", response_model=List[Photo])
def read_photos(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
):
    photos = crud_photo.get_multi(db, skip=skip, limit=limit)
    return photos

@router.get("/album/{album_id}", response_model=List[Photo])
def read_album_photos(
    *,
    db: Session = Depends(get_db),
    album_id: int,
    skip: int = 0,
    limit: int = 100,
):
    photos = crud_photo.get_by_album(db=db, album_id=album_id, skip=skip, limit=limit)
    return photos

@router.post("/album/{album_id}", response_model=Photo)
async def create_photo(
    *,
    db: Session = Depends(get_db),
    album_id: int,
    photo_in: PhotoCreate,
    file: UploadFile = File(...),
):
    file_path = await save_upload_file(file, "photos")
    photo = crud_photo.create(
        db=db,
        obj_in=photo_in,
        album_id=album_id
    )
    photo = crud_photo.update(
        db=db,
        db_obj=photo,
        obj_in={"image": file_path}
    )
    return photo

@router.get("/{photo_id}", response_model=Photo)
def read_photo(
    *,
    db: Session = Depends(get_db),
    photo_id: int,
):
    photo = crud_photo.get(db=db, id=photo_id)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    return photo

@router.put("/{photo_id}", response_model=Photo)
def update_photo(
    *,
    db: Session = Depends(get_db),
    photo_id: int,
    photo_in: PhotoUpdate,
):
    photo = crud_photo.get(db=db, id=photo_id)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    photo = crud_photo.update(db=db, db_obj=photo, obj_in=photo_in)
    return photo

@router.delete("/{photo_id}", response_model=Photo)
def delete_photo(
    *,
    db: Session = Depends(get_db),
    photo_id: int,
):
    photo = crud_photo.get(db=db, id=photo_id)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    photo = crud_photo.remove(db=db, id=photo_id)
    return photo 