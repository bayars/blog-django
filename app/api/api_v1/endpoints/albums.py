from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.crud import album as crud_album
from app.schemas.album import Album, AlbumCreate, AlbumUpdate
from app.db.session import get_db
from app.core.utils import save_upload_file

router = APIRouter()

@router.get("/", response_model=List[Album])
def read_albums(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
):
    albums = crud_album.get_multi(db, skip=skip, limit=limit)
    return albums

@router.post("/", response_model=Album)
def create_album(
    *,
    db: Session = Depends(get_db),
    album_in: AlbumCreate,
):
    album = crud_album.create(db=db, obj_in=album_in)
    return album

@router.get("/{album_id}", response_model=Album)
def read_album(
    *,
    db: Session = Depends(get_db),
    album_id: int,
):
    album = crud_album.get(db=db, id=album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@router.get("/slug/{slug}", response_model=Album)
def read_album_by_slug(
    *,
    db: Session = Depends(get_db),
    slug: str,
):
    album = crud_album.get_by_slug(db=db, slug=slug)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@router.put("/{album_id}", response_model=Album)
def update_album(
    *,
    db: Session = Depends(get_db),
    album_id: int,
    album_in: AlbumUpdate,
):
    album = crud_album.get(db=db, id=album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    album = crud_album.update(db=db, db_obj=album, obj_in=album_in)
    return album

@router.delete("/{album_id}", response_model=Album)
def delete_album(
    *,
    db: Session = Depends(get_db),
    album_id: int,
):
    album = crud_album.get(db=db, id=album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    album = crud_album.remove(db=db, id=album_id)
    return album

@router.post("/{album_id}/upload-cover")
async def upload_album_cover(
    *,
    db: Session = Depends(get_db),
    album_id: int,
    file: UploadFile = File(...),
):
    album = crud_album.get(db=db, id=album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    
    file_path = await save_upload_file(file, "albums")
    album = crud_album.update(
        db=db,
        db_obj=album,
        obj_in={"cover_image": file_path}
    )
    return {"file_path": file_path} 