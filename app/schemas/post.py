<<<<<<< HEAD
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TagBase(BaseModel):
    name: str
=======
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, HttpUrl

class TagBase(BaseModel):
    name: str
    slug: str
>>>>>>> 3f6247b (gallery not working, implement the markdown)

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        from_attributes = True

class PostBase(BaseModel):
    title: str
    content: str
    featured_image: Optional[str] = None

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    title: Optional[str] = None
    content: Optional[str] = None

class Post(PostBase):
    id: int
    slug: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    tags: List[Tag] = []

    class Config:
        from_attributes = True 