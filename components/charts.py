import plotly.express as px
import pandas as pd
import streamlit as st

def render_forecast_charts(forecast_json: dict):
    records = [
        {
            "Thời gian": item["dt_txt"],
            "Nhiệt độ (°C)": item["main"]["temp"],
            "Độ ẩm (%)": item["main"]["humidity"],
            "Gió (m/s)": item["wind"]["speed"],
        }
        for item in forecast_json["list"]
    ]
    df = pd.DataFrame(records)

    fig_temp = px.line(df, x="Thời gian", y="Nhiệt độ (°C)", title="🌡️ Nhiệt độ 5 ngày")
    st.plotly_chart(fig_temp, use_container_width=True)

    fig_wind = px.line(df, x="Thời gian", y="Gió (m/s)", title="💨 Tốc độ gió 5 ngày")
    st.plotly_chart(fig_wind, use_container_width=True)

    fig_hum = px.bar(df, x="Thời gian", y="Độ ẩm (%)", title="💧 Độ ẩm 5 ngày")
    st.plotly_chart(fig_hum, use_container_width=True)