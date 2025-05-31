from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, File
from sqlalchemy.orm import Session

from app.crud import project as crud_project
from app.schemas.project import Project, ProjectCreate, ProjectUpdate
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=List[Project])
def read_projects(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    tag_id: Optional[int] = None
):
    """
    Retrieve projects.
    """
    if tag_id:
        projects = crud_project.get_multi_by_tag(db, tag_id=tag_id, skip=skip, limit=limit)
    else:
        projects = crud_project.get_multi(db, skip=skip, limit=limit)
    return projects

@router.post("/", response_model=Project)
def create_project(
    *,
    db: Session = Depends(get_db),
    project_in: ProjectCreate
):
    """
    Create new project.
    """
    project = crud_project.create_with_slug(db=db, obj_in=project_in)
    return project

@router.put("/{project_id}", response_model=Project)
def update_project(
    *,
    db: Session = Depends(get_db),
    project_id: int,
    project_in: ProjectUpdate
):
    """
    Update a project.
    """
    project = crud_project.get(db=db, id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project = crud_project.update(db=db, db_obj=project, obj_in=project_in)
    return project

@router.get("/{project_id}", response_model=Project)
def read_project(
    *,
    db: Session = Depends(get_db),
    project_id: int
):
    """
    Get project by ID.
    """
    project = crud_project.get(db=db, id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.get("/slug/{slug}", response_model=Project)
def read_project_by_slug(
    *,
    db: Session = Depends(get_db),
    slug: str
):
    """
    Get project by slug.
    """
    project = crud_project.get_by_slug(db=db, slug=slug)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.delete("/{project_id}", response_model=Project)
def delete_project(
    *,
    db: Session = Depends(get_db),
    project_id: int
):
    """
    Delete a project.
    """
    project = crud_project.get(db=db, id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project = crud_project.remove(db=db, id=project_id)
    return project 