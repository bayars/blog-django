from typing import List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app.crud import gallery as crud_gallery
from app.schemas.gallery import Album, AlbumCreate, AlbumUpdate, PhotoSeries, PhotoSeriesCreate, PhotoSeriesUpdate, Photo, PhotoCreate
from app.db.session import get_db
from app.utils.file_handlers import save_upload_file, delete_file

router = APIRouter()

# Album endpoints
@router.get("/albums/", response_model=List[Album])
def read_albums(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    """
    Retrieve albums.
    """
    albums = crud_gallery.album.get_multi(db, skip=skip, limit=limit)
    return albums

@router.post("/albums/", response_model=Album)
async def create_album(
    *,
    db: Session = Depends(get_db),
    album_in: AlbumCreate,
    cover_image: UploadFile = File(None)
):
    """
    Create new album.
    """
    if cover_image:
        file_path = await save_upload_file(cover_image, "albums")
        if file_path:
            album_in.cover_image = file_path
    
    album = crud_gallery.album.create_with_slug(db=db, obj_in=album_in)
    return album

@router.get("/albums/{album_id}", response_model=Album)
def read_album(
    *,
    db: Session = Depends(get_db),
    album_id: int
):
    """
    Get album by ID.
    """
    album = crud_gallery.album.get(db=db, id=album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@router.get("/albums/slug/{slug}", response_model=Album)
def read_album_by_slug(
    *,
    db: Session = Depends(get_db),
    slug: str
):
    """
    Get album by slug.
    """
    album = crud_gallery.album.get_by_slug(db=db, slug=slug)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@router.put("/albums/{album_id}", response_model=Album)
async def update_album(
    *,
    db: Session = Depends(get_db),
    album_id: int,
    album_in: AlbumUpdate,
    cover_image: UploadFile = File(None)
):
    """
    Update an album.
    """
    album = crud_gallery.album.get(db=db, id=album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    
    if cover_image:
        if album.cover_image:
            delete_file(album.cover_image)
        file_path = await save_upload_file(cover_image, "albums")
        if file_path:
            album_in.cover_image = file_path
    
    album = crud_gallery.album.update(db=db, db_obj=album, obj_in=album_in)
    return album

@router.delete("/albums/{album_id}", response_model=Album)
def delete_album(
    *,
    db: Session = Depends(get_db),
    album_id: int
):
    """
    Delete an album.
    """
    album = crud_gallery.album.get(db=db, id=album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    if album.cover_image:
        delete_file(album.cover_image)
    album = crud_gallery.album.remove(db=db, id=album_id)
    return album

# Photo Series endpoints
@router.get("/series/", response_model=List[PhotoSeries])
def read_series(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    album_id: int = None
):
    """
    Retrieve photo series.
    """
    if album_id:
        series = crud_gallery.photo_series.get_by_album(db, album_id=album_id, skip=skip, limit=limit)
    else:
        series = crud_gallery.photo_series.get_multi(db, skip=skip, limit=limit)
    return series

@router.post("/series/", response_model=PhotoSeries)
def create_series(
    *,
    db: Session = Depends(get_db),
    series_in: PhotoSeriesCreate,
    album_id: int
):
    """
    Create new photo series.
    """
    series = crud_gallery.photo_series.create_with_slug(db=db, obj_in=series_in, album_id=album_id)
    return series

@router.get("/series/{series_id}", response_model=PhotoSeries)
def read_series_by_id(
    *,
    db: Session = Depends(get_db),
    series_id: int
):
    """
    Get photo series by ID.
    """
    series = crud_gallery.photo_series.get(db=db, id=series_id)
    if not series:
        raise HTTPException(status_code=404, detail="Photo series not found")
    return series

@router.get("/series/slug/{slug}", response_model=PhotoSeries)
def read_series_by_slug(
    *,
    db: Session = Depends(get_db),
    slug: str
):
    """
    Get photo series by slug.
    """
    series = crud_gallery.photo_series.get_by_slug(db=db, slug=slug)
    if not series:
        raise HTTPException(status_code=404, detail="Photo series not found")
    return series

@router.put("/series/{series_id}", response_model=PhotoSeries)
def update_series(
    *,
    db: Session = Depends(get_db),
    series_id: int,
    series_in: PhotoSeriesUpdate
):
    """
    Update a photo series.
    """
    series = crud_gallery.photo_series.get(db=db, id=series_id)
    if not series:
        raise HTTPException(status_code=404, detail="Photo series not found")
    series = crud_gallery.photo_series.update(db=db, db_obj=series, obj_in=series_in)
    return series

@router.delete("/series/{series_id}", response_model=PhotoSeries)
def delete_series(
    *,
    db: Session = Depends(get_db),
    series_id: int
):
    """
    Delete a photo series.
    """
    series = crud_gallery.photo_series.get(db=db, id=series_id)
    if not series:
        raise HTTPException(status_code=404, detail="Photo series not found")
    series = crud_gallery.photo_series.remove(db=db, id=series_id)
    return series

# Photo endpoints
@router.post("/series/{series_id}/photos/", response_model=List[Photo])
async def create_photos(
    *,
    db: Session = Depends(get_db),
    series_id: int,
    photos: List[UploadFile] = File(...)
):
    """
    Upload multiple photos to a series.
    """
    series = crud_gallery.photo_series.get(db=db, id=series_id)
    if not series:
        raise HTTPException(status_code=404, detail="Photo series not found")
    
    photo_creates = []
    for photo in photos:
        file_path = await save_upload_file(photo, f"series/{series_id}")
        if file_path:
            photo_creates.append(PhotoCreate(title=photo.filename, file_path=file_path))
    
    photos = crud_gallery.photo.create_multi(db=db, series_id=series_id, photos_in=photo_creates)
    return photos

@router.get("/series/{series_id}/photos/", response_model=List[Photo])
def read_photos(
    *,
    db: Session = Depends(get_db),
    series_id: int,
    skip: int = 0,
    limit: int = 100
):
    """
    Get photos from a series.
    """
    photos = crud_gallery.photo.get_by_series(db=db, series_id=series_id, skip=skip, limit=limit)
    return photos

@router.delete("/photos/{photo_id}", response_model=Photo)
def delete_photo(
    *,
    db: Session = Depends(get_db),
    photo_id: int
):
    """
    Delete a photo.
    """
    photo = crud_gallery.photo.get(db=db, id=photo_id)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    if photo.file_path:
        delete_file(photo.file_path)
    photo = crud_gallery.photo.remove(db=db, id=photo_id)
    return photo 