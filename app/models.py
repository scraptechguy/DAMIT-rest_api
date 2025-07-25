from sqlalchemy import Column, Integer, String, Float, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Asteroid(Base):
    __tablename__ = "stored_files"

    id = Column(Integer, primary_key=True, index=True)  # THIS LINE IS REQUIRED
    filename = Column(String(255), nullable=False)
    comment = Column(String(255), nullable=True)
    hidden = Column(Boolean)
    hash = Column(String(255), nullable=False)
    created = Column(String(255), nullable=True)
    modified = Column(String(255), nullable=False)
