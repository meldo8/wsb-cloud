from datetime import date

from pydantic import BaseModel


class BaseDestination(BaseModel):
    city: str
    trip_start: date
    trip_end: date


class ForecastDestination(BaseModel):
    forecast: str


class Destination(BaseDestination):
    id: int

    class Config:
        orm_mode = True
