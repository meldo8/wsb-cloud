import datetime
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import crud, models, schemas
from database.db import engine, get_db
from database.weather_api import WeatherApi
from database.weather_oracle import WeatherOracle

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def health():
    return "It works!"


@app.post("/destinations/", response_model=schemas.Destination)
def create_destination(destination: schemas.BaseDestination, db: Session = Depends(get_db)):
    return crud.create_destination(db=db, destination=destination)


@app.get("/destinations/", response_model=List[schemas.Destination])
def read_destinations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    destinations = crud.get_destinations(db, skip=skip, limit=limit)
    return destinations


@app.get("/destinations/{destination_id}", response_model=schemas.Destination)
def read_destination(destination_id: int, db: Session = Depends(get_db)):
    db_destination = crud.get_destination(db, destination_id=destination_id)
    if db_destination is None:
        raise HTTPException(status_code=404, detail="destination not found")
    return db_destination


@app.get("/destinations/{destination_id}/forecast", response_model=schemas.ForecastDestination)
def read_destination_forecast(
    destination_id: int,
    db: Session = Depends(get_db),
    api: WeatherApi = Depends(WeatherApi),
    oracle: WeatherOracle = Depends(WeatherOracle),
):
    db_destination = crud.get_destination(db, destination_id=destination_id)
    if db_destination is None:
        raise HTTPException(status_code=404, detail="destination not found")

    number_of_days_to_forecast = (db_destination.trip_end - datetime.datetime.today()).days
    if number_of_days_to_forecast > 10:
        raise HTTPException(status_code=403, detail="It is too early for this forecast")

    if number_of_days_to_forecast <= 0:
        raise HTTPException(status_code=403, detail="It is too late for the forecast")

    weather = api.retrieve_forecast(str(db_destination.city), str(number_of_days_to_forecast))

    return schemas.ForecastDestination(forecast=oracle.forecast(weather, number_of_days_to_forecast))
