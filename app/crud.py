from sqlalchemy.orm import Session
from app import models, schemas

def get_asteroids(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Asteroid).offset(skip).limit(limit).all()

def create_asteroid(db: Session, asteroid: schemas.AsteroidCreate):
    db_asteroid = models.Asteroid(**asteroid.dict())
    db.add(db_asteroid)
    db.commit()
    db.refresh(db_asteroid)
    return db_asteroid
