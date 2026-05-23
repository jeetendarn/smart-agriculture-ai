import streamlit as st
import requests

st.set_page_config(page_title="Crop Yield AI", layout="centered")

st.title("🌾 Smart Agriculture AI System")
st.write("Predict crop yield using Machine Learning")

# =========================
# INPUT FORM
# =========================

year = st.number_input("Year", 1990, 2030, 2020)

area = st.selectbox(
    "Country",
    ["India", "USA", "Brazil", "China", "Australia", "Nigeria", "Argentina"]
)

item = st.selectbox(
    "Crop Type",
    ["Wheat", "Rice", "Maize", "Barley", "Soybean"]
)

rainfall = st.number_input("Rainfall (mm/year)", 0, 5000, 1200)

pesticides = st.number_input("Pesticides (tonnes)", 0, 1000, 200)

temp = st.number_input("Average Temperature (°C)", 0.0, 50.0, 25.0)

# =========================
# PREDICT BUTTON
# =========================

if st.button("Predict Yield"):

    payload = {
        "Year": year,
        "Area": area,
        "Item": item,
        "average_rain_fall_mm_per_year": rainfall,
        "pesticides_tonnes": pesticides,
        "avg_temp": temp
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"🌾 Predicted Yield: {result['predicted_yield']}")
    else:
        st.error("Prediction failed")