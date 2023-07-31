import sys
from api.weather import get_weather
from api.export_json import export_json
import time


def main():
    data = get_weather(35.6823, 179.6823, timezone="Asia/Tokyo", hourly=True)
    filepath = time.strftime("%Y%m%d%H%M%S") + ".json"
    export_json(data, filepath)


if __name__ == '__main__':
    main()
