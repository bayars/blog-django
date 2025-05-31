import os
from fastapi import UploadFile
from pathlib import Path
from typing import Optional

from app.core.config import settings

async def save_upload_file(upload_file: UploadFile, directory: str) -> Optional[str]:
    """
    Save an uploaded file to the specified directory.
    Returns the relative path to the saved file.
    """
    try:
        # Create directory if it doesn't exist
        upload_dir = Path(settings.MEDIA_ROOT) / directory
        upload_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate file path
        file_path = upload_dir / upload_file.filename
        
        # Save the file
        with open(file_path, "wb") as buffer:
            content = await upload_file.read()
            buffer.write(content)
        
        # Return relative path
        return f"{directory}/{upload_file.filename}"
    except Exception as e:
        print(f"Error saving file: {str(e)}")
        return None

def delete_file(file_path: str) -> bool:
    """
    Delete a file from the media directory.
    Returns True if successful, False otherwise.
    """
    try:
        full_path = Path(settings.MEDIA_ROOT) / file_path
        if full_path.exists():
            os.remove(full_path)
            return True
        return False
    except Exception as e:
        print(f"Error deleting file: {str(e)}")
        return False 