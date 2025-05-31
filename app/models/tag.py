from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

# Association tables
post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("post.id", ondelete="CASCADE")),
    Column("tag_id", Integer, ForeignKey("tag.id", ondelete="CASCADE")),
)

project_tags = Table(
    "project_tags",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("project.id", ondelete="CASCADE")),
    Column("tag_id", Integer, ForeignKey("tag.id", ondelete="CASCADE")),
)

class Tag(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    
    # Relationships
    posts = relationship("Post", secondary=post_tags, back_populates="tags")
    projects = relationship("Project", secondary=project_tags, back_populates="tags") 