import folium
from streamlit_folium import st_folium

LAYER_OPTIONS = {
    "🌡️ Nhiệt độ": "temp_new",
    "💨 Gió": "wind_new",
    "☁️ Mây": "clouds_new",
    "🌧️ Mưa": "precipitation_new",
}

def render_weather_map(lat: float, lon: float, city: str, api_key: str, layer: str = "temp_new"):
    m = folium.Map(location=[lat, lon], zoom_start=8)
    for label, code in LAYER_OPTIONS.items():
        folium.TileLayer(
            tiles=f"https://tile.openweathermap.org/map/{code}/{{z}}/{{x}}/{{y}}.png?appid={api_key}",
            attr="OpenWeatherMap",
            name=label,
            overlay=True,
            show=(code == layer),
        ).add_to(m)
    folium.LayerControl().add_to(m)
    folium.Marker([lat, lon], popup=city).add_to(m)
    st_folium(m, height=420, use_container_width=True)