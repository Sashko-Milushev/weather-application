import requests
from dotenv import dotenv_values

from .models import WeatherForCity

env_vars = dotenv_values("../../.env")


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
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }

        # Create a new WeatherForCity instance and save it
        weather_instance = WeatherForCity(
            name=weather_info["city"],
            temperature=weather_info["temperature"],
            humidity=weather_info["humidity"],
            description=weather_info["description"]
        )
        weather_instance.save()

        return weather_info, 200

    elif response.status_code == 404:
        return {'error': f'{city_name} not found. Try with another name'}, 404
    else:
        return {'error': 'Ooops...an error occurred. We are sorry. Try again.'}, 500


def get_weather_for_5_random_cities(cities: list):
    weather_info_for_cities = []
    for city in cities:
        data, status_code = call_weather_service(city)
        if status_code == 200:
            weather_info_for_cities.append(data)
        elif status_code == 404:
            weather_info_for_cities.append({'error': f'{city} not found. Try with another name'})
        else:
            weather_info_for_cities.append({'error': 'Ooops...an error occurred. We are sorry. Try again.'})

    return weather_info_for_cities
