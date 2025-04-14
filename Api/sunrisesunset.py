import requests
from datetime import datetime
from Controllers.readenv import read_env

def get_sun_times() -> []:

    params = {
        "lat": read_env("SUN_LAT"),
        "lng": read_env("SUN_LNG")
    }

    try:
        res = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
        res.raise_for_status()
        response = res.json()
        time_sunrise = datetime.strptime(response['results']['sunrise'], "%I:%M:%S %p").strftime("%H:%M")
        time_sunset = datetime.strptime(response['results']['sunset'], "%I:%M:%S %p").strftime("%H:%M")
        return time_sunrise, time_sunset
    except requests.exceptions.HTTPError as e:
        print(f"GET Error: {e}")
        print(f"Response Text: {res.text}")
        print(f"URL: {res.url}")
        raise
