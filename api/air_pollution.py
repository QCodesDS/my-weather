import requests

URL = "https://api.openweathermap.org/data/2.5/air_pollution"

AQI_LABEL = {1: "Tốt", 2: "Khá", 3: "Trung bình", 4: "Xấu", 5: "Rất xấu"}

def get_aqi(lat: float, lon: float, api_key: str) -> dict:
    r = requests.get(URL, params={"lat": lat, "lon": lon, "appid": api_key})
    r.raise_for_status()
    data = r.json()
    aqi = data["list"][0]["main"]["aqi"]
    components = data["list"][0]["components"]
    return {"aqi": aqi, "label": AQI_LABEL[aqi], "components": components}