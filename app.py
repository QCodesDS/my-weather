import streamlit as st
from dotenv import load_dotenv
import os

from api.geocoding import coords_to_city
from api.weather import get_current, get_forecast
from api.air_pollution import get_aqi
from components.map_view import render_weather_map
from components.charts import render_forecast_charts

load_dotenv()
API_KEY = os.getenv("OWM_API_KEY")

st.set_page_config(page_title="MyWeather", page_icon="🌤️", layout="wide")
st.title("🌤️ MyWeather")

st.sidebar.header("Nhập tọa độ (từ Google Maps)")
lat = st.sidebar.number_input("Latitude", value=10.7769, format="%.6f")
lon = st.sidebar.number_input("Longitude", value=106.7009, format="%.6f")

if st.sidebar.button("🔍 Tìm thông tin thời tiết"):
    st.session_state["lat"] = lat
    st.session_state["lon"] = lon
    st.session_state["searched"] = True

if st.session_state.get("searched"):
    lat = st.session_state["lat"]
    lon = st.session_state["lon"]

    try:
        with st.spinner("Đang lấy dữ liệu..."):
            geo = coords_to_city(lat, lon, API_KEY)

        if not geo:
            st.error("⚠️ Không tìm thấy địa điểm tại tọa độ này.")
        else:
            city = geo.get("name", "Unknown")
            country = geo.get("country", "")
            st.subheader(f"📍 {city}, {country}")

            weather = get_current(city, country, API_KEY)
            main = weather["main"]
            wind = weather["wind"]
            w = weather["weather"][0]

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("🌡️ Nhiệt độ", f"{main['temp']}°C", f"Cảm giác: {main['feels_like']}°C")
            col2.metric("💧 Độ ẩm", f"{main['humidity']}%")
            col3.metric("💨 Gió", f"{wind['speed']} m/s")
            col4.metric("☁️ Tình trạng", w["description"].capitalize())

            aqi_data = get_aqi(lat, lon, API_KEY)
            st.info(f"🌿 Chất lượng không khí: **{aqi_data['label']}** (AQI = {aqi_data['aqi']}) | "
                    f"PM2.5: {aqi_data['components']['pm2_5']} μg/m³")

            st.subheader("🗺️ Bản đồ thời tiết")
            selected_layer = st.selectbox(
                "Chọn lớp bản đồ",
                ["temp_new", "wind_new", "clouds_new", "precipitation_new"]
            )
            render_weather_map(lat, lon, city, API_KEY, layer=selected_layer)

            st.subheader("📈 Dự báo 5 ngày / 3 giờ")
            forecast = get_forecast(city, country, API_KEY)
            render_forecast_charts(forecast)

    except Exception as e:
        st.error(f"⚠️ Không thể lấy dữ liệu thời tiết cho tọa độ này. ({e})")