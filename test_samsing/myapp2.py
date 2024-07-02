from pyowm import OWM
owm = OWM('4981fb9e29d4c6bc5e01895f9d0fde65')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Baranovichi, Belarus')
weather = observation.weather

forecast = mgr.forecast_at_place('New York, US', '3h')
for weather_forecast in forecast.forecast:
    date = weather_forecast.reference_time('iso')
    temerature = weather_forecast.temperature('celsius')
    print(f"Прогноз на {date}: {temerature['temp']}C")