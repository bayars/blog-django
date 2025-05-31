from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Album(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    slug = Column(String(200), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    cover_image = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    photos = relationship("Photo", back_populates="album", cascade="all, delete-orphan") 