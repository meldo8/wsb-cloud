import requests
from fastapi import HTTPException

from database.config import API_KEY


class WeatherApi:
    BASE_URL = "http://api.weatherapi.com/v1/"

    def retrieve_forecast(self, city: str, days: str) -> dict:
        response = requests.get(f"{self.BASE_URL}forecast.json?key={API_KEY}&q={city}&days={days}&aqi=no&alerts=no")
        if response.status_code >= 400:
            raise HTTPException(status_code=404, detail="destination has no forecast")

        return response.json()
