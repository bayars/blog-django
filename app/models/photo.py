from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Photo(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    image = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Foreign keys
    album_id = Column(Integer, ForeignKey("album.id", ondelete="CASCADE"), nullable=False)
    
    # Relationships
    album = relationship("Album", back_populates="photos") 