"""Shared configuration for migration scripts."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BACKUP_ROOT = Path(r"D:\PARA\Resource\memoryhub-1-1-article1-1067\memoryhub-1-1")

DATA_DIR = PROJECT_ROOT / "data"
CONTENT_KO = PROJECT_ROOT / "content" / "ko" / "posts"
CONTENT_EN = PROJECT_ROOT / "content" / "en" / "posts"
STATIC_IMAGES = PROJECT_ROOT / "static" / "images"

POSTS_INDEX = DATA_DIR / "posts.json"
ORIGINAL_BASE_URL = "https://memoryhub.tistory.com"
