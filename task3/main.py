from flask import Flask, render_template

from utils import get_5_random_cities
from weather_service import get_weather_for_5_random_cities

app = Flask(__name__)

cities = ["Sofia", "Varna", "Rome", "Naples", "Paris", "Nantes", "Madrid", "Barcelona", "New York", "Louisiana"]


@app.route('/home')
def load_home():
    current_5_cities = get_5_random_cities(cities)
    weather_data = get_weather_for_5_random_cities(current_5_cities)
    return render_template('base.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
