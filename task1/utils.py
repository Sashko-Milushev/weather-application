import random


def get_5_random_cities(cities: list):
    return random.sample(cities, 5)


degree_sign = u'\N{DEGREE SIGN}'


def give_info_for_city(name: str, condition: str, temperature: float, humidity: int):
    print(
        f"Weather condition in {name} is {condition}. The temperature is around {temperature}{degree_sign} and "
        f"{humidity}% humidity.")
    print("...")
