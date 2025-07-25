from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from app import models, config
from app.db import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "FastAPI DAMIT API is running!"}

@app.get("/shape/{file_id}", response_class=PlainTextResponse)
def get_shape_file(file_id: int, db: Session = Depends(get_db)):
    file_record = db.query(models.Asteroid).filter(models.Asteroid.id == file_id).first()

    if not file_record:
        raise HTTPException(status_code=404, detail="File ID not found in database")

    shape_hash = file_record.hash
    file_path = config.SHAPE_PATH / shape_hash  # e.g., data/shapes/<hash>

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found on disk")

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")

    return content
