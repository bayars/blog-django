from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
<<<<<<< HEAD
=======

>>>>>>> 3f6247b (gallery not working, implement the markdown)
from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

<<<<<<< HEAD
=======
# Dependency
>>>>>>> 3f6247b (gallery not working, implement the markdown)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 