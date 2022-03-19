from sqlalchemy import Column, DateTime, Integer, String

from .db import Base


class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, unique=False, nullable=False)
    trip_start = Column(DateTime, nullable=False)
    trip_end = Column(DateTime, nullable=False)
