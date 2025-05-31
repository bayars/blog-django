<<<<<<< HEAD
from app.db.base_class import Base
from app.models.post import Post
from app.models.album import Album
from app.models.photo import Photo 
=======
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import all models here that are needed by SQLAlchemy
from app.models.tag import Tag, post_tags, project_tags  # noqa
from app.models.post import Post  # noqa
from app.models.project import Project  # noqa
from app.models.gallery import Album, PhotoSeries, Photo  # noqa 
>>>>>>> 3f6247b (gallery not working, implement the markdown)
