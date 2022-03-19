class WeatherOracle:
    def forecast(self, weather: dict, number_of_days_to_forecast: int) -> str:
        weather_condition_points = 0
        for forecast in weather["forecast"]["forecastday"]:
            if forecast["day"]["mintemp_c"] < 0 or forecast["day"]["mintemp_c"] > 25:
                weather_condition_points += 1

            if forecast["day"]["maxtemp_c"] > 40:
                weather_condition_points += 1

            if forecast.get("daily_chance_of_rain", 0) >= 60 or forecast.get("daily_chance_of_rain", 0) >= 60:
                weather_condition_points += 3

        weather_condition_points = weather_condition_points // number_of_days_to_forecast
        if weather_condition_points == 0:
            return "good"
        elif weather_condition_points in [1, 2]:
            return "moderate"

        return "bad"
