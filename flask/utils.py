import random

from task3.weather_service import call_weather_service


def get_5_random_cities(cities: list):
    return random.sample(cities, 5)


def get_coldest_city(cities: list):
    return min(cities, key=lambda city: call_weather_service(city)[0]["temperature"])


def get_avg_temperature(cities: list):
    temperatures = [call_weather_service(city)[0]["temperature"] for city in cities]
    avg_temp = sum(temperatures) / len(temperatures)
    return f'{avg_temp:.2f}'
