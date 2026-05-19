import requests, os

BASE = "https://api.openweathermap.org/geo/1.0/reverse"

def coords_to_city(lat: float, lon: float, api_key: str) -> dict:
    """Trả về {'name': 'Ho Chi Minh City', 'country': 'VN', ...}"""
    r = requests.get(BASE, params={
        "lat": lat, "lon": lon,
        "limit": 1, "appid": api_key
    })
    r.raise_for_status()
    data = r.json()
    if not data:
        return {}
    return data[0]  # name, country (ISO 3166-1 alpha-2), state, ...