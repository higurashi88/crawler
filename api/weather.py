import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(lat, lon, timezone=None, hourly=False):
    params = {
        "latitude": lat,
        "longitude": lon,
    }

    if timezone:
        params["timezone"] = timezone

    if hourly:
        params["hourly"] = "temperature_2m"

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data
