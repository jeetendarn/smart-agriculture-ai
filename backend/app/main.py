from fastapi import FastAPI
from app.utils.weather import get_weather
from app.utils.recommendation import recommend_crop
from app.utils.fertilizer import recommend_fertilizer
import joblib
import numpy as np
import pandas as pd

app = FastAPI(title="Crop Yield Prediction API")

# =========================
# LOAD MODEL
# =========================
# model = joblib.load("e:/smart-agriculture-ai/backend/app/model/crop_yield_model.pkl")
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(
    BASE_DIR,
    "model",
    "crop_yield_model.pkl"
)

model = joblib.load(model_path)
# =========================
# ROOT ENDPOINT
# =========================
@app.get("/")
def home():
    return {"message": "Crop Yield Prediction API is running"}

# =========================
# PREDICTION ENDPOINT
# =========================
@app.post("/predict")
def predict(data: dict):

    try:
        input_data = pd.DataFrame([data])

        prediction = model.predict(input_data)

        return {
            "predicted_yield": float(prediction[0])
        }

    except Exception as e:
        return {
            "error": str(e)
        }
    
@app.post("/smart-predict")
def smart_predict(data: dict):

    city = data.get("Area")

    weather = get_weather(city)

    temp = weather["temperature"]
    rainfall = weather["rainfall"]

    crop = recommend_crop(temp, rainfall)

    fertilizer = recommend_fertilizer(crop)

    input_data = pd.DataFrame([{
        "Year": data["Year"],
        "Area": data["Area"],
        "Item": crop,
        "average_rain_fall_mm_per_year": rainfall,
        "pesticides_tonnes": data["pesticides_tonnes"],
        "avg_temp": temp
    }])

    prediction = model.predict(input_data)

    return {
        "weather": weather,
        "recommended_crop": crop,
        "fertilizer": fertilizer,
        "predicted_yield": float(prediction[0])
    }    