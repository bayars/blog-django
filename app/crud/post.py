from typing import List, Optional
from sqlalchemy.orm import Session
<<<<<<< HEAD
from app.crud.base import CRUDBase
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate
from app.models.tag import Tag
from slugify import slugify

class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):
    def get_by_slug(self, db: Session, *, slug: str) -> Optional[Post]:
        return db.query(Post).filter(Post.slug == slug).first()

    def create(self, db: Session, *, obj_in: PostCreate) -> Post:
        db_obj = Post(
            title=obj_in.title,
            slug=slugify(obj_in.title),
            content=obj_in.content,
            featured_image=obj_in.featured_image
        )
=======
from slugify import slugify

from app.crud.base import CRUDBase
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate

class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):
    def create_with_slug(self, db: Session, *, obj_in: PostCreate) -> Post:
        obj_in_data = obj_in.dict()
        obj_in_data["slug"] = slugify(obj_in_data["title"])
        db_obj = Post(**obj_in_data)
>>>>>>> 3f6247b (gallery not working, implement the markdown)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

<<<<<<< HEAD
    def update(
        self,
        db: Session,
        *,
        db_obj: Post,
        obj_in: PostUpdate
    ) -> Post:
        update_data = obj_in.dict(exclude_unset=True)
        if "title" in update_data:
            update_data["slug"] = slugify(update_data["title"])
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def add_tags(self, db: Session, *, post_id: int, tag_names: List[str]) -> Post:
        post = self.get(db, id=post_id)
        if not post:
            return None
        
        for tag_name in tag_names:
            tag = db.query(Tag).filter(Tag.name == tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.add(tag)
            post.tags.append(tag)
        
        db.commit()
        db.refresh(post)
        return post
=======
    def get_by_slug(self, db: Session, *, slug: str) -> Optional[Post]:
        return db.query(Post).filter(Post.slug == slug).first()

    def get_multi_by_tag(
        self, db: Session, *, tag_id: int, skip: int = 0, limit: int = 100
    ) -> List[Post]:
        return (
            db.query(Post)
            .join(Post.tags)
            .filter(Post.tags.any(id=tag_id))
            .offset(skip)
            .limit(limit)
            .all()
        )
>>>>>>> 3f6247b (gallery not working, implement the markdown)

post = CRUDPost(Post) 