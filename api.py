import requests
import datetime as dt

def get_iss() -> []:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    return data["iss_position"]['latitude'], data["iss_position"]["longitude"]

def get_sun_times(lat, long) -> []:
    params = {
        "lat": lat,
        "lng": long
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    print (f'{response.json()['results']['sunrise']}, {response.json()['results']['sunset']}')
    time_sunrise = dt.datetime.strptime(response.json()['results']['sunrise'], "%I:%M:%S %p").strftime("%H:%M")
    time_sunset = dt.datetime.strptime(response.json()['results']['sunset'], "%I:%M:%S %p").strftime("%H:%M")

    return time_sunrise, time_sunset