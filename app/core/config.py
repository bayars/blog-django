<<<<<<< HEAD
from pydantic_settings import BaseSettings
from typing import Optional, List
=======
from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
>>>>>>> 3f6247b (gallery not working, implement the markdown)

class Settings(BaseSettings):
    PROJECT_NAME: str = "Blog API"
    API_V1_STR: str = "/api/v1"
    
<<<<<<< HEAD
    # Database settings
=======
    # CORS Configuration
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]
    
    # Database Configuration
>>>>>>> 3f6247b (gallery not working, implement the markdown)
    POSTGRES_SERVER: str = "db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "blog"
<<<<<<< HEAD
    POSTGRES_PORT: str = "5432"
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    # Media settings
    MEDIA_ROOT: str = "media"
    
    # Security settings
    SECRET_KEY: str = "your-secret-key-here"  # Change in production
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days

    # CORS settings
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

=======
    SQLALCHEMY_DATABASE_URI: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
    
    # Media files
    MEDIA_ROOT: str = "media"
    
>>>>>>> 3f6247b (gallery not working, implement the markdown)
    class Config:
        case_sensitive = True
        env_file = ".env"

<<<<<<< HEAD
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.SQLALCHEMY_DATABASE_URI = (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

=======
>>>>>>> 3f6247b (gallery not working, implement the markdown)
settings = Settings() 