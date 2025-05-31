from typing import List, Optional
<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.crud import post as crud_post
from app.schemas.post import Post, PostCreate, PostUpdate
from app.db.session import get_db
from app.core.utils import save_upload_file
=======
from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, File
from sqlalchemy.orm import Session

from app.crud import post as crud_post
from app.schemas.post import Post, PostCreate, PostUpdate
from app.db.session import get_db
>>>>>>> 3f6247b (gallery not working, implement the markdown)

router = APIRouter()

@router.get("/", response_model=List[Post])
def read_posts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
<<<<<<< HEAD
):
    posts = crud_post.get_multi(db, skip=skip, limit=limit)
=======
    tag_id: Optional[int] = None
):
    """
    Retrieve posts.
    """
    if tag_id:
        posts = crud_post.get_multi_by_tag(db, tag_id=tag_id, skip=skip, limit=limit)
    else:
        posts = crud_post.get_multi(db, skip=skip, limit=limit)
>>>>>>> 3f6247b (gallery not working, implement the markdown)
    return posts

@router.post("/", response_model=Post)
def create_post(
    *,
    db: Session = Depends(get_db),
<<<<<<< HEAD
    post_in: PostCreate,
):
    post = crud_post.create(db=db, obj_in=post_in)
=======
    post_in: PostCreate
):
    """
    Create new post.
    """
    post = crud_post.create_with_slug(db=db, obj_in=post_in)
    return post

@router.put("/{post_id}", response_model=Post)
def update_post(
    *,
    db: Session = Depends(get_db),
    post_id: int,
    post_in: PostUpdate
):
    """
    Update a post.
    """
    post = crud_post.get(db=db, id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post = crud_post.update(db=db, db_obj=post, obj_in=post_in)
>>>>>>> 3f6247b (gallery not working, implement the markdown)
    return post

@router.get("/{post_id}", response_model=Post)
def read_post(
    *,
    db: Session = Depends(get_db),
<<<<<<< HEAD
    post_id: int,
):
=======
    post_id: int
):
    """
    Get post by ID.
    """
>>>>>>> 3f6247b (gallery not working, implement the markdown)
    post = crud_post.get(db=db, id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.get("/slug/{slug}", response_model=Post)
def read_post_by_slug(
    *,
    db: Session = Depends(get_db),
<<<<<<< HEAD
    slug: str,
):
=======
    slug: str
):
    """
    Get post by slug.
    """
>>>>>>> 3f6247b (gallery not working, implement the markdown)
    post = crud_post.get_by_slug(db=db, slug=slug)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

<<<<<<< HEAD
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

=======
>>>>>>> 3f6247b (gallery not working, implement the markdown)
@router.delete("/{post_id}", response_model=Post)
def delete_post(
    *,
    db: Session = Depends(get_db),
<<<<<<< HEAD
    post_id: int,
):
=======
    post_id: int
):
    """
    Delete a post.
    """
>>>>>>> 3f6247b (gallery not working, implement the markdown)
    post = crud_post.get(db=db, id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post = crud_post.remove(db=db, id=post_id)
<<<<<<< HEAD
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
=======
    return post 
>>>>>>> 3f6247b (gallery not working, implement the markdown)
