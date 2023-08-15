from django.shortcuts import render

from .utils import get_5_random_cities, get_coldest_city, get_avg_temperature, background_images
from .weather_service import get_weather_for_5_random_cities, call_weather_service


def home(request):
    current_cities = get_5_random_cities()
    weather_data = get_weather_for_5_random_cities(current_cities)
    coldest_city = get_coldest_city(current_cities)
    avg_temperature = get_avg_temperature(current_cities)

    for data in weather_data:
        description = data['description'].lower()
        data['background_image'] = background_images.get(description, '/static/images/default.jpg')

    context = {
        'weather_data': weather_data,
        'coldest_city': coldest_city,
        'avg_temperature': avg_temperature

    }
    return render(request, 'weather/weather.html', context)


from django.http import JsonResponse


def search(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        data, status_code = call_weather_service(city)

        description = data['description'].lower()
        data['background_image'] = background_images.get(description, '/static/images/default.jpg')

        if status_code == 200:
            return JsonResponse(data)
        else:
            return JsonResponse({'error': data['error']}, status=status_code)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
