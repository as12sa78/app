import requests
from geopy.geocoders import Nominatim
from datetime import datetime
from pyowm import OWM
from pyowm.utils.config import get_default_config

def get_coordinates(address):
    geolocator = Nominatim(user_agent="myapp")
    location = geolocator.geocode(address)
    return location.point.latitude, location.point.longitude

def get_weather_forecast(lat, lon):
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = OWM('4981fb9e29d4c6bc5e01895f9d0fde65', config_dict)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_coords(lat, lon)
    weather = observation.weather
    forecast = weather.forecast_for_day(datetime.today())
    return forecast
address = "Барановичи, Беларусь"
latitude, longitude = get_coordinates(address)
get_weather_forecast = get_weather_forecast(latitude, longitude)

print(f'Прогноз погоды для {address}:')
print(f"Температура: {weather_forecast.temperature('celsius')['temp']}C")
print(f'Описание : {weather_forecast.detailed_status}')
print(f"Скорость ветра: {weather_forecast.wind()['speed']} m/c")