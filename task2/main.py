# !!!!! Press the green button in the gutter to run the script
import tkinter as tk

from task2.utils import get_5_random_cities
from task2.weather_service import call_weather_service, get_coldest_city, get_avg_temperature

city_labels = []
cities = ["Sofia", "Varna", "Rome", "Naples", "Paris", "Nantes", "Madrid", "Barcelona", "New York", "Louisiana"]


def update_weather_info(city_label, city_name):
    weather_data = call_weather_service(city_name)

    if weather_data is not None:
        weather_condition = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        info_text = f"City: {city_name}\nWeather: {weather_condition}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
    else:
        info_text = f"City: {city_name}\nError retrieving weather information."

    city_label.config(text=info_text)


def get_weather_for_city_from_input(city_name: str):
    city_to_check = city_entry.get()
    data = call_weather_service(city_to_check)
    if data is not None:
        weather_condition = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        result_text.set(f"Weather: {weather_condition}\nTemperature: {temperature}°C\nHumidity: {humidity}%")
    else:
        result_text.set("Error retrieving weather information.")


window = tk.Tk()
window.title("Weather App")

current_cities = get_5_random_cities(cities)

for city_name in current_cities:
    city_label = tk.Label(window, text="Loading...")
    city_label.pack()
    city_labels.append(city_label)

for i, city_name in enumerate(current_cities):
    update_weather_info(city_labels[i], city_name)

coldest_city_label = tk.Label(window, text="Coldest City: ")
coldest_city_label.pack()

avg_temp_label = tk.Label(window, text="Average Temperature: ")
avg_temp_label.pack()

coldest_city = get_coldest_city(current_cities)
avg_temperature = get_avg_temperature(current_cities)

coldest_city_label.config(text=f"Coldest City: {coldest_city}")
avg_temp_label.config(text=f"Average Temperature: {avg_temperature:.2f}°C")

city_label = tk.Label(window, text="Enter a specific city to check weather:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

get_weather_button = tk.Button(window, text="Get Weather",
                               command=lambda: get_weather_for_city_from_input(city_entry.get()))
get_weather_button.pack()

result_text = tk.StringVar()

result_label = tk.Label(window, textvariable=result_text)
result_label.pack()
# !!!!! Press the green button in the gutter to run the script

if __name__ == '__main__':
    window.mainloop()
