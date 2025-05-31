from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
<<<<<<< HEAD
from app.db.base_class import Base
=======

from app.db.base import Base
>>>>>>> 3f6247b (gallery not working, implement the markdown)

# Association tables
post_tags = Table(
    "post_tags",
    Base.metadata,
<<<<<<< HEAD
    Column("post_id", Integer, ForeignKey("post.id", ondelete="CASCADE")),
    Column("tag_id", Integer, ForeignKey("tag.id", ondelete="CASCADE")),
=======
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
>>>>>>> 3f6247b (gallery not working, implement the markdown)
)

project_tags = Table(
    "project_tags",
    Base.metadata,
<<<<<<< HEAD
    Column("project_id", Integer, ForeignKey("project.id", ondelete="CASCADE")),
    Column("tag_id", Integer, ForeignKey("tag.id", ondelete="CASCADE")),
)

class Tag(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
=======
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
)

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    slug = Column(String(50), unique=True, nullable=False)
>>>>>>> 3f6247b (gallery not working, implement the markdown)
    
    # Relationships
    posts = relationship("Post", secondary=post_tags, back_populates="tags")
    projects = relationship("Project", secondary=project_tags, back_populates="tags") 