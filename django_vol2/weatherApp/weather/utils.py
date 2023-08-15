import random

import requests
from dotenv import dotenv_values

from .models import WeatherForCity
from .weather_service import call_weather_service

env_vars = dotenv_values("../../.env")

background_images = {
    'clear sky': '/static/images/sun.jpg',
    'few clouds': '/static/images/clouds.jpg',
    'scattered clouds': '/static/images/clouds.jpg',
    'overcast clouds': '/static/images/clouds.jpg',
    'broken clouds': '/static/images/clouds.jpg',
    'shower rain': '/static/images/rain.jpg',
    'rain': '/static/images/rain.jpg',
    'light rain': '/static/images/rain.jpg',
    'light intensity drizzle': '/static/images/rain.jpg',
    'thunderstorm': '/static/images/thunderstorm.jpg',
    'snow': '/static/images/snow.jpg',
    'mist': '/static/images/mist.jpg',
    'fog': '/static/images/mist.jpg',
    'haze': '/static/images/mist.jpg',

}


def get_5_random_cities():
    username = 'corewin'
    url = f"http://api.geonames.org/citiesJSON?north=90&south=-90&east=180&west=-180&lang=en&username={username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        cities = [result['name'] for result in data['geonames']]
        random_cities = random.sample(cities, 5)
        return random_cities
    else:
        print('Error occurred!')
        return []


def get_coldest_city(cities: list):
    return min(cities, key=lambda city: call_weather_service(city)[0]["temperature"])


def get_avg_temperature(cities: list):
    temperatures = [call_weather_service(city)[0]["temperature"] for city in cities]
    avg_temp = sum(temperatures) / len(temperatures)
    return f'{avg_temp:.2f}'


def get_last_10_weather_records(city_name):
    weather_records = WeatherForCity.objects.filter(name=city_name).order_by('-timestamp')[:10]
    return weather_records
