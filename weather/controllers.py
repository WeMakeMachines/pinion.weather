from config import BaseConfig
from flask import request
from services import OpenWeatherMap
from helpers import Units

open_weather_map = OpenWeatherMap(
    BaseConfig.OPEN_WEATHER_MAP_API_KEY,
    BaseConfig.LATITUDE,
    BaseConfig.LONGITUDE,
    BaseConfig.BASE_UNITS
)


class WeatherArgs:
    def __init__(self):
        self.speed_units = WeatherArgs.__get_units(request.args.get('speed'))
        self.temperature_units = WeatherArgs.__get_units(request.args.get('temperature'))

    @staticmethod
    def __get_units(arg):
        if arg == Units.IMPERIAL.value:
            return Units.IMPERIAL
        else:
            return Units.METRIC


def get_units_from_args(api_call):
    weather_args = WeatherArgs()
    return api_call(speed_units=weather_args.speed_units, temperature_units=weather_args.temperature_units)


def open_weather_map_now():
    return get_units_from_args(open_weather_map.now)


def open_weather_map_hourly():
    return get_units_from_args(open_weather_map.hourly)


def open_weather_map_daily():
    return get_units_from_args(open_weather_map.daily)