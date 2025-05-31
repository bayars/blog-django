from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.crud import post as crud_post
from app.schemas.post import Post, PostCreate, PostUpdate
from app.db.session import get_db
from app.core.utils import save_upload_file

router = APIRouter()

@router.get("/", response_model=List[Post])
def read_posts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
):
    posts = crud_post.get_multi(db, skip=skip, limit=limit)
    return posts

@router.post("/", response_model=Post)
def create_post(
    *,
    db: Session = Depends(get_db),
    post_in: PostCreate,
):
    post = crud_post.create(db=db, obj_in=post_in)
    return post

@router.get("/{post_id}", response_model=Post)
def read_post(
    *,
    db: Session = Depends(get_db),
    post_id: int,
):
    post = crud_post.get(db=db, id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.get("/slug/{slug}", response_model=Post)
def read_post_by_slug(
    *,
    db: Session = Depends(get_db),
    slug: str,
):
    post = crud_post.get_by_slug(db=db, slug=slug)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=Post)
def update_post(
    *,
    db: Session = Depends(get_db),
    post_id: int,
    post_in: PostUpdate,
):
    post = crud_post.get(db=db, id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post = crud_post.update(db=db, db_obj=post, obj_in=post_in)
    return post

@router.delete("/{post_id}", response_model=Post)
def delete_post(
    *,
    db: Session = Depends(get_db),
    post_id: int,
):
    post = crud_post.get(db=db, id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post = crud_post.remove(db=db, id=post_id)
    return post

@router.post("/{post_id}/upload-image")
async def upload_post_image(
    *,
    db: Session = Depends(get_db),
    post_id: int,
    file: UploadFile = File(...),
):
    post = crud_post.get(db=db, id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    file_path = await save_upload_file(file, "posts")
    post = crud_post.update(
        db=db,
        db_obj=post,
        obj_in={"featured_image": file_path}
    )
    return {"file_path": file_path} 