import sys
from api.weather import get_weather


def main():
    data = get_weather(35.6823, 179.6823)
    print(data)


if __name__ == '__main__':
    main()
