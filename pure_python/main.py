# !!!!! Press the green button in the gutter to run the script
from task1.utils import get_5_random_cities
from task1.weather_service import weather_in_cities, get_weather_for_city_from_input

cities = ["Sofia", "Varna", "Rome", "Naples", "Paris", "Nantes", "Madrid", "Barcelona", "New York", "Louisiana"]

if __name__ == '__main__':
    cities_to_fetch = get_5_random_cities(cities)
    weather_in_cities(cities_to_fetch)
    get_weather_for_city_from_input()


# !!!!! Press the green button in the gutter to run the script
