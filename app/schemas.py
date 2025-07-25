from pydantic import BaseModel
from datetime import date

class AsteroidBase(BaseModel):
    name: str
    diameter: float
    discovery_date: date

class AsteroidRead(AsteroidBase):
    id: int

    class Config:
        from_attributes = True
