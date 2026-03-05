import os
from dotenv import load_dotenv

load_dotenv(override=True)


class Config:
    """Application configuration loaded from environment variables."""
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    GROQ_MODEL = "llama-3.3-70b-versatile"
    DEBUG = os.getenv("FLASK_DEBUG", "True").lower() in ("true", "1", "yes")
