import requests
from dotenv import dotenv_values

env_vars = dotenv_values("../.env")


def get_coldest_city(cities: list):
    return min(cities, key=lambda city: call_weather_service(city)["main"]["temp"])


def get_avg_temperature(cities: list):
    temperatures = [call_weather_service(city)["main"]["temp"] for city in cities]
    return sum(temperatures) / len(temperatures)


def call_weather_service(city_name: str):
    api_key = env_vars["API_KEY"]
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data

    return None
