from typing import List, Optional
from sqlalchemy.orm import Session
from slugify import slugify

from app.crud.base import CRUDBase
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate

class CRUDProject(CRUDBase[Project, ProjectCreate, ProjectUpdate]):
    def create_with_slug(self, db: Session, *, obj_in: ProjectCreate) -> Project:
        obj_in_data = obj_in.dict()
        obj_in_data["slug"] = slugify(obj_in_data["title"])
        db_obj = Project(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_slug(self, db: Session, *, slug: str) -> Optional[Project]:
        return db.query(Project).filter(Project.slug == slug).first()

    def get_multi_by_tag(
        self, db: Session, *, tag_id: int, skip: int = 0, limit: int = 100
    ) -> List[Project]:
        return (
            db.query(Project)
            .join(Project.tags)
            .filter(Project.tags.any(id=tag_id))
            .offset(skip)
            .limit(limit)
            .all()
        )

project = CRUDProject(Project) 