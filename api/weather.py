import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(lat, lon):
    url = f"{BASE_URL}?latitude={lat}&longitude={lon}&hourly=temperature_2m&timezone=Asia%2FTokyo"
    response = requests.get(url)
    data = response.json()
    return data
