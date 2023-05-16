from flask import Flask, render_template, request, jsonify

from utils import get_5_random_cities
from weather_service import get_weather_for_5_random_cities, call_weather_service

app = Flask(__name__)

cities = ["Sofia", "Varna", "Rome", "Naples", "Paris", "Metz", "Madrid", "Barcelona", "New York", "Louisiana"]
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


@app.route('/home', methods=['GET'])
def load_home():
    current_5_cities = get_5_random_cities(cities)
    weather_data = get_weather_for_5_random_cities(current_5_cities)

    for data in weather_data:
        description = data['description'].lower()
        data['background_image'] = background_images.get(description, '/static/images/default.jpg')

    return render_template('base.html', weather_data=weather_data)


@app.route('/search', methods=['GET'])
def search():
    city_name = request.args.get('city')
    data, status_code = call_weather_service(city_name)
    if status_code == 200:
        description = data['description'].lower()
        data['background_image'] = background_images.get(description, '/static/images/default.jpg')
        return jsonify(data)
    else:
        return jsonify({'error': 'Weather data not found'}), status_code


if __name__ == '__main__':
    app.run(debug=True)
