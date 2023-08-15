import random

from .weather_service import call_weather_service

cities = ["Sofia", "Varna", "Rome", "Naples",
          "Paris", "Metz", "Madrid", "Barcelona",
          "New York", "Louisiana"]

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
    'fog': '/static/images/mist.jpg'
}

def get_5_random_cities():
    return random.sample(cities, 5)


def get_coldest_city(cities: list):
    return min(cities, key=lambda city: call_weather_service(city)[0]["temperature"])


def get_avg_temperature(cities: list):
    temperatures = [call_weather_service(city)[0]["temperature"] for city in cities]
    avg_temp = sum(temperatures) / len(temperatures)
    return f'{avg_temp:.2f}'
