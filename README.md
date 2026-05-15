# 🌦️ AI Weather Forecasting System Documentation

---

# 📘 Project Overview

## Overview

This project is a deep learning-based weather forecasting system using Time Series Forecasting techniques.

The application predicts:

* 🌡️ Minimum Temperature
* ☀️ Maximum Temperature
* 🌤️ Average Temperature
* 🌧️ Projected Rainfall

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
* Indian city dropdown selection
* Rainfall forecasting
* Sequential data processing
* Automated startup script

---

# 🏗️ System Architecture

## Workflow

User Browser
↓
Streamlit Frontend
↓
FastAPI Backend
↓
LSTM Deep Learning Models
↓
Weather Forecast Predictions

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

### GET /health

Health check endpoint.

### POST /predict

Predict future weather.

Request Example:

{
"city": "Mumbai",
"date": "2026-05-20"
}

Response Example:

{
"city": "Mumbai",
"date": "2026-05-20",
"min_temperature": 24.1,
"max_temperature": 33.5,
"mean_temperature": 28.3,
"rainfall": 12.4
}

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

python -m src.training.train

---

## Evaluation Metrics

### MAE

Mean Absolute Error

### RMSE

Root Mean Squared Error

---

# 🚀 Deployment Guide

## Prerequisites

Install the following before running the project:

* Python 3.11
* Git
* VS Code (Recommended)

Python 3.14 is NOT supported by TensorFlow.

---

## Step 1 — Open Project Folder

Open PowerShell inside the project directory:

cd D:\Month5Projects-TheDevelopersArena-Internship

---

## Step 2 — Create Virtual Environment

python -m venv venv

---

## Step 3 — Activate Virtual Environment

.\venv\Scripts\Activate.ps1

---

## Step 4 — Enable PowerShell Script Execution (First Time Only)

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

---

## Step 5 — Install Required Packages

pip install -r requirements.txt

---

## Step 6 — Train AI Models

python -m src.training.train

This creates:

* min_temp_model.h5
* max_temp_model.h5
* mean_temp_model.h5
* rainfall_model.h5

---

## Step 7 — Start FastAPI Backend

uvicorn src.api.main:app --reload

Backend URL:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Step 8 — Start Streamlit Frontend

streamlit run ui/simple_app.py

Frontend URL:

[http://localhost:8501](http://localhost:8501)

---

## Step 9 — Open Application

Open browser and visit:

[http://localhost:8501](http://localhost:8501)

---

## Using the Application

1. Select an Indian city from dropdown
2. Select a future date
3. Click Predict Weather

The system predicts:

* 🌡️ Minimum Temperature
* ☀️ Maximum Temperature
* 🌤️ Average Temperature
* 🌧️ Projected Rainfall

---

## Quick Start (Recommended)

Instead of running all commands manually, users can run:

.\run_project.ps1

This automatically:

* Creates virtual environment
* Activates environment
* Installs requirements
* Trains models (if missing)
* Starts backend
* Starts frontend

---

# 🌐 Application URLs

Backend API:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

Swagger API Documentation:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Frontend UI:
[http://localhost:8501](http://localhost:8501)

---

# 🛠️ Troubleshooting

## TensorFlow Installation Error

Cause:
Unsupported Python version.

Fix:
Use Python 3.10 or 3.11 only.

---

## Streamlit Not Opening

Run manually:

streamlit run ui/simple_app.py

---

## Backend Not Starting

Run manually:

uvicorn src.api.main:app --reload

---

## Script Execution Blocked

Run:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

---

# ✅ Successful Startup

When everything works correctly:

* FastAPI terminal shows:

  * Application startup complete

* Streamlit terminal shows:

  * Local URL: [http://localhost:8501](http://localhost:8501)

* Browser opens weather prediction UI.

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

---

# 📁 Recommended Project Structure

Month5Projects-TheDevelopersArena-Internship/
│
├── .gitignore
├── README.md
├── requirements.txt
├── documentation.txt
├── run_project.ps1
│
├── data/
├── docs/
├── src/
├── ui/
└── venv/

---

# 👨‍💻 Author

Kaushik NS

AI Weather Forecasting System
