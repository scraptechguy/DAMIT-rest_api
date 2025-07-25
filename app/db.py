from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import config

DATABASE_URL = (
    f"mysql+pymysql://{config.DB_USER}:{config.DB_PASSWORD}@"
    f"{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
