from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd

app = FastAPI(title="Crop Yield Prediction API")

# =========================
# LOAD MODEL
# =========================
model = joblib.load("e:/smart-agriculture-ai/backend/app/model/crop_yield_model.pkl")

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