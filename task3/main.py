from flask import Flask, render_template

from utils import get_5_random_cities
from weather_service import get_weather_for_5_random_cities

app = Flask(__name__)

cities = ["Sofia", "Varna", "Rome", "Naples", "Paris", "Metz", "Madrid", "Barcelona", "New York", "Louisiana"]


@app.route('/home')
def load_home():
    current_5_cities = get_5_random_cities(cities)
    weather_data = get_weather_for_5_random_cities(current_5_cities)

    background_images = {
        'clear sky': '/static/images/sun.jpg',
        'few clouds': '/static/images/clouds.jpg',
        'scattered clouds': '/static/images/clouds.jpg',
        'overcast clouds': '/static/images/clouds.jpg',
        'broken clouds': '/static/images/clouds.jpg',
        'shower rain': '/static/images/rain.jpg',
        'rain': '/static/images/rain.jpg',
        'light intensity drizzle': '/static/images/rain.jpg',
        'thunderstorm': '/static/images/thunderstorm.jpg',
        'snow': '/static/images/snow.jpg',
        'mist': '/static/images/mist.jpg',
        'fog': '/static/images/mist.jpg'
    }
    for data in weather_data:
        description = data['description'].lower()
        data['background_image'] = background_images.get(description, '/static/images/default.jpg')

    return render_template('base.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
