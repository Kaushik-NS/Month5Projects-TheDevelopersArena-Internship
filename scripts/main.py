from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from src.inference.predict import WeatherPredictor


# ==========================================
# FASTAPI INITIALIZATION
# ==========================================

app = FastAPI(
    title="Weather Forecasting API",
    version="1.0"
)

# ==========================================
# LOAD PREDICTOR
# ==========================================

print("[INFO] Loading weather prediction models...")

predictor = WeatherPredictor()

print("[SUCCESS] Models loaded successfully!")

# ==========================================
# REQUEST MODEL
# ==========================================


class PredictionRequest(BaseModel):

    sequence: List[List[float]]


# ==========================================
# ROOT ENDPOINT
# ==========================================


@app.get("/")
def root():

    return {
        "message": "Weather Forecasting API Running"
    }


# ==========================================
# HEALTH CHECK
# ==========================================


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


# ==========================================
# PREDICTION ENDPOINT
# ==========================================


@app.post("/predict")
def predict(request: PredictionRequest):

    try:

        print("[INFO] Prediction request received.")

        prediction = predictor.predict_weather(
            request.sequence
        )

        print(
            "[SUCCESS] Prediction completed."
        )

        return {

            "min_temp": prediction["min_temp"],

            "max_temp": prediction["max_temp"],

            "mean_temp": prediction["mean_temp"],

            "projected_rainfall":
            prediction["projected_rainfall"]
        }

    except Exception as e:

        print(
            f"[ERROR] Prediction failed: {str(e)}"
        )

        return {
            "error": str(e)
        }