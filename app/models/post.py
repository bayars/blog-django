from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship
<<<<<<< HEAD
from app.db.base_class import Base

class Post(Base):
=======

from app.db.base import Base

class Post(Base):
    __tablename__ = "posts"

>>>>>>> 3f6247b (gallery not working, implement the markdown)
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    slug = Column(String(200), unique=True, nullable=False)
    content = Column(Text, nullable=False)
<<<<<<< HEAD
    featured_image = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
=======
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    featured_image = Column(String(255), nullable=True)
>>>>>>> 3f6247b (gallery not working, implement the markdown)
    
    # Relationships
    tags = relationship("Tag", secondary="post_tags", back_populates="posts") 