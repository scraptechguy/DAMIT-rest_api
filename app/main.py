from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.db import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/asteroids/", response_model=list[schemas.AsteroidRead])
def read_asteroids(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_asteroids(db, skip=skip, limit=limit)

@app.get("/")
def read_root():
    return {"message": "FastAPI DAMIT API is running!"}
