import requests

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_current(city: str, country: str, api_key: str) -> dict:
    r = requests.get(CURRENT_URL, params={
        "q": f"{city},{country}",
        "appid": api_key,
        "units": "metric",
        "lang": "vi"
    })
    r.raise_for_status()
    return r.json()

def get_forecast(city: str, country: str, api_key: str) -> dict:
    r = requests.get(FORECAST_URL, params={
        "q": f"{city},{country}",
        "appid": api_key,
        "units": "metric",
        "lang": "vi"
    })
    r.raise_for_status()
    return r.json()