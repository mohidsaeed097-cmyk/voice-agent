"""
Tools the voice agent can call.

The LLM does not know today's weather or time by itself, so we give it
functions. When the user asks "weather in Lahore?", the LLM decides to call
get_weather("Lahore"), we fetch live data, and the LLM speaks the result.
"""

from datetime import datetime
from zoneinfo import ZoneInfo

import aiohttp
from livekit.agents import function_tool

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

# Open-Meteo weather codes -> plain words the agent can say out loud
WEATHER_CODES = {
    0: "clear sky",
    1: "mainly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "foggy",
    48: "foggy",
    51: "light drizzle",
    53: "drizzle",
    55: "heavy drizzle",
    61: "light rain",
    63: "rain",
    65: "heavy rain",
    71: "light snow",
    73: "snow",
    75: "heavy snow",
    80: "rain showers",
    81: "rain showers",
    82: "heavy rain showers",
    95: "a thunderstorm",
    96: "a thunderstorm with hail",
    99: "a thunderstorm with hail",
}


@function_tool
async def get_weather(city: str) -> str:
    """Get the current live weather for a city.

    Args:
        city: Name of the city, for example "Lahore" or "London".
    """
    timeout = aiohttp.ClientTimeout(total=10)
    try:
        async with aiohttp.ClientSession(timeout=timeout) as http:
            # 1) City name -> latitude/longitude
            async with http.get(GEOCODE_URL, params={"name": city, "count": 1}) as r:
                geo = await r.json()
            results = geo.get("results") or []
            if not results:
                return f"I could not find a city called {city}."
            place = results[0]

            # 2) Latitude/longitude -> current weather
            params = {
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "current": "temperature_2m,apparent_temperature,relative_humidity_2m,weather_code,wind_speed_10m",
            }
            async with http.get(WEATHER_URL, params=params) as r:
                data = await r.json()
    except Exception:
        return "The weather service is not reachable right now."

    now = data["current"]
    condition = WEATHER_CODES.get(now["weather_code"], "unknown conditions")
    return (
        f"In {place['name']}, {place.get('country', '')}: {condition}, "
        f"{round(now['temperature_2m'])} degrees Celsius, feels like "
        f"{round(now['apparent_temperature'])}, humidity {now['relative_humidity_2m']} percent, "
        f"wind {round(now['wind_speed_10m'])} km per hour."
    )


@function_tool
async def get_time(timezone: str = "Asia/Karachi") -> str:
    """Get the current date and time.

    Args:
        timezone: IANA timezone name. Use "Asia/Karachi" for Pakistan unless the user names another place.
    """
    try:
        now = datetime.now(ZoneInfo(timezone))
    except Exception:
        now = datetime.now(ZoneInfo("Asia/Karachi"))
        timezone = "Asia/Karachi"
    return now.strftime(f"It is %I:%M %p on %A, %d %B %Y ({timezone}).")
