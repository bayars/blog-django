from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, HttpUrl

class TagBase(BaseModel):
    name: str
    slug: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    title: str
    description: str
    content: str
    featured_image: Optional[str] = None
    github_url: Optional[str] = None
    live_url: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None

class Project(ProjectBase):
    id: int
    slug: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    tags: List[Tag] = []

    class Config:
        from_attributes = True 