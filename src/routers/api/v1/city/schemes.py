from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CityResponseScheme(BaseModel):
    id: int
    name: str
    weather: float

    
    class Config:
        orm_mode = True


class CreateCityScheme(BaseModel):
    name: str


class GetCityScheme(BaseModel):
    name: str