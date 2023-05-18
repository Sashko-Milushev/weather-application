from django.db import models


class WeatherForCity(models.Model):
    name = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=200)
    background_image = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    IMAGE_MAPPING = {
        'clear sky': 'images/sun.jpg',
        'few clouds': 'images/clouds.jpg',
        'scattered clouds': 'images/clouds.jpg',
        'overcast clouds': 'images/clouds.jpg',
        'broken clouds': 'images/clouds.jpg',
        'shower rain': 'images/rain.jpg',
        'rain': 'images/rain.jpg',
        'light intensity drizzle': 'images/rain.jpg',
        'thunderstorm': 'images/thunderstorm.jpg',
        'snow': 'images/snow.jpg',
        'mist': 'images/mist.jpg',
        'fog': 'images/mist.jpg'
    }

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.background_image = self.IMAGE_MAPPING.get(self.description, '')
        super().save(*args, **kwargs)
