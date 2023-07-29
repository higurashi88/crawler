import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "timezone": "Asia/Tokyo",
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data
