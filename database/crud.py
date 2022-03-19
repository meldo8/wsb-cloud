from typing import Optional

from sqlalchemy.orm import Session

from . import models, schemas


def get_destination(db: Session, destination_id: int) -> Optional[models.Destination]:
    return db.query(models.Destination).filter(models.Destination.id == destination_id).first()


def get_user_by_city(db: Session, location: str) -> Optional[models.Destination]:
    return db.query(models.Destination).filter(models.Destination.city == location).first()


def get_destinations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Destination).offset(skip).limit(limit).all()


def create_destination(db: Session, destination: schemas.BaseDestination):
    db_destination = models.Destination(
        trip_start=destination.trip_start, trip_end=destination.trip_end, city=destination.city
    )
    db.add(db_destination)
    db.commit()
    db.refresh(db_destination)
    return db_destination
