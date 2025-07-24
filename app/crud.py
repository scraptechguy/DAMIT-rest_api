from sqlalchemy.orm import Session
from app import models, schemas

def get_asteroids(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Asteroid).offset(skip).limit(limit).all()
