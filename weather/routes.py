from config import BaseConfig
from flask import Blueprint
from services import OpenWeatherMap
from middleware import cache_api_response

open_weather_map = OpenWeatherMap(BaseConfig.OPEN_WEATHER_MAP_API_KEY, BaseConfig.LATITUDE, BaseConfig.LONGITUDE)

weather = Blueprint("weather", __name__)


@weather.route("/now")
def now():
    return open_weather_map.now()


@weather.route("/hourly")
@cache_api_response(60, open_weather_map.hourly)
def hourly(response):
    return response


@weather.route("/daily")
@cache_api_response(60 * 60 * 24, open_weather_map.daily)
def daily(response):
    return response
