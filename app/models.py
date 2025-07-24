from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Asteroid(Base):
    __tablename__ = "asteroids"

    id = Column(Integer, primary_key=True, index=True)  # THIS LINE IS REQUIRED
    name = Column(String(255), nullable=False)
    diameter = Column(Float)
    discovery_date = Column(Date)