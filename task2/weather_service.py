import requests
from task2.utils import degree_sign
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
    elif response.status_code == 404:
        print(f"{city_name} not found. Please enter valid city name.")
    else:
        print("Ooops...an error occurred. We are sorry. Try again.")
    return None


def weather_in_cities(cities: list):
    for city in cities:
        data = call_weather_service(city)
        if data is not None:
            weather_condition = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            give_info_for_city(city, weather_condition, temperature, humidity)

    print(f"The coldest city is {get_coldest_city(cities)}")
    print(f"The average temperature for all the cities is {get_avg_temperature(cities):.2f}{degree_sign}")



