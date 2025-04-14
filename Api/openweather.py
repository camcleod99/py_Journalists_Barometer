import requests

from Controllers.readenv import read_env

def get_weather():
    parameters = {
        "appid": read_env("WEATHER_APPID"),
        "q": read_env("WEATHER_Q"),
        "cnt": 4,
    }
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    return response.json()