from dotenv import load_dotenv
from pathlib import Path
import os

# Load environment variables from .env file
load_dotenv()

DB_USER = os.getenv("DB_USER", "fastapi")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password123")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "example_db")
SHAPE_PATH = Path(os.getenv("SHAPE_PATH", "./data/shapes")).resolve()
# Default fallbacks are set to match the example_db config