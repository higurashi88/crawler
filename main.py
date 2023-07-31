import sys
from api.weather import get_weather
from api.export_json import export_json
import time
import schedule


def main():
    # 緯度,経度,タイムゾーン,時間ごとの気温を取得
    data = get_weather(35.6823, 179.6823, timezone="Asia/Tokyo", hourly=True)

    filepath = time.strftime("%Y%m%d%H%M%S") + ".json"
    export_json(data, filepath)


if __name__ == '__main__':
    # 毎時55分に実行
    while True:
        schedule.run_pending()
        time.sleep(1)
        schedule.every().hour.at(":55").do(main)
