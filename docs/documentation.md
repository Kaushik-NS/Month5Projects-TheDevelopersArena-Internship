# 🌦️ AI Weather Forecasting System Documentation

---

# 📘 Project Overview

## Overview

This project is a deep learning-based weather forecasting system using Time Series Forecasting techniques.

The application predicts:

* Minimum Temperature
* Maximum Temperature
* Average Temperature
* Rainfall

for future dates and major Indian cities.

---

## Objective

To build a production-style AI forecasting pipeline using:

* Deep Learning
* LSTM Neural Networks
* FastAPI
* Streamlit
* Time Series Analysis

---

## Specialization

Time Series Forecasting

---

## Key Features

* Multi-output weather prediction
* LSTM-based forecasting
* FastAPI backend
* Streamlit UI
* Indian city support
* Rainfall forecasting
* Sequential data processing

---

# 🏗️ System Architecture

## Workflow

User Input
↓
Streamlit Frontend
↓
FastAPI Backend
↓
LSTM Deep Learning Models
↓
Weather Forecast Output

---

## Components

### Frontend

Streamlit web application for user interaction.

### Backend

FastAPI REST API for prediction handling.

### Data Processing

Preprocessing pipeline for feature engineering and normalization.

### Deep Learning Models

LSTM neural networks trained for:

* Minimum temperature
* Maximum temperature
* Average temperature
* Rainfall

### Dataset

Historical weather dataset containing:

* Date
* City
* Temperature
* Rainfall
* Seasonal information

---

# 🌐 API Documentation

## Base URL

[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Endpoints

### GET /

Returns API status.

#### Response

```json
{
    "message": "Weather Forecast API Running"
}
```

---

### GET /health

Health check endpoint.

#### Response

```json
{
    "status": "healthy"
}
```

---

### POST /predict

Predict future weather.

#### Request Body

```json
{
    "city": "Mumbai",
    "date": "2026-05-20"
}
```

#### Response

```json
{
    "city": "Mumbai",
    "date": "2026-05-20",
    "min_temperature": 24.1,
    "max_temperature": 33.5,
    "mean_temperature": 28.3,
    "rainfall": 12.4
}
```

---

# 🧠 Model Training Guide

## Deep Learning Model

The project uses LSTM (Long Short-Term Memory) neural networks for time-series forecasting.

---

## Training Workflow

1. Load dataset
2. Clean data
3. Feature engineering
4. Normalize features
5. Create sequences
6. Train LSTM models
7. Save trained models

---

## Features Used

* Month
* Day
* Temperature history
* Rainfall history
* Seasonal data

---

## Model Outputs

* Min Temperature
* Max Temperature
* Mean Temperature
* Rainfall

---

## Training Command

```powershell
python -m src.training.train
```

---

## Evaluation Metrics

### MAE

Mean Absolute Error

### RMSE

Root Mean Squared Error

---

# 🚀 Deployment Guide

## Step 1 — Create Virtual Environment

```powershell
python -m venv venv
```

Activate:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Step 2 — Install Requirements

```powershell
pip install -r requirements.txt
```

---

## Step 3 — Train Models

```powershell
python -m src.training.train
```

---

## Step 4 — Start Backend

```powershell
uvicorn src.api.main:app --reload
```

---

## Step 5 — Start Frontend

```powershell
streamlit run ui/simple_app.py
```

---

## Application URLs

Backend:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

Frontend:
[http://localhost:8501](http://localhost:8501)

---

# 🛠️ Troubleshooting

## TensorFlow Installation Error

### Cause

Unsupported Python version.

### Fix

Use Python 3.10 or 3.11.

---

## Streamlit Not Found

### Fix

```powershell
pip install streamlit
```

---

## Uvicorn Not Found

### Fix

```powershell
pip install uvicorn
```

---

## Model Not Found Error

### Cause

Training not completed.

### Fix

```powershell
python -m src.training.train
```

---

## Port Already In Use

### Fix

Close previous terminal sessions.

Or use different port:

```powershell
uvicorn src.api.main:app --reload --port 8001
```

---

# 🔮 Future Improvements

## Planned Enhancements

* Real-time weather API integration
* Cloud deployment
* Docker containerization
* Kubernetes scaling
* CI/CD pipelines
* Monitoring dashboards
* Multi-country weather support
* Weather map visualization
* GPU acceleration
* Attention-based forecasting models

---

## Advanced AI Improvements

* Transformer-based forecasting
* Hybrid forecasting models
* AutoML optimization
* Hyperparameter tuning
* Ensemble prediction systems
