# 🌦️ AI Weather Forecasting System

## 📌 Project Overview

This project is a Time Series Forecasting application built using Deep Learning (LSTM) to predict future weather conditions for major Indian cities.

The system predicts:

- 🌡️ Minimum Temperature
- ☀️ Maximum Temperature
- 🌤️ Average Temperature
- 🌧️ Projected Rainfall

using historical weather data and sequential forecasting techniques.

The project includes:

- Deep Learning forecasting models
- Data preprocessing pipeline
- FastAPI backend API
- Streamlit frontend interface
- Multi-model prediction system
- Production-style project structure

---

# 🧠 Specialization

## Time Series Forecasting

This project focuses on Time Series Analysis using Long Short-Term Memory (LSTM) neural networks.

Time series forecasting uses historical sequential data to predict future values.

Example:

Past weather → Predict future weather

---

# 🏗️ Technologies Used

## Machine Learning / Deep Learning
- TensorFlow
- Keras
- LSTM Neural Networks
- Scikit-learn

## Backend
- FastAPI
- Uvicorn

## Frontend
- Streamlit

## Data Processing
- Pandas
- NumPy

## Visualization
- Matplotlib

---

# 📁 Project Structure

```text
data/
│
├── weather_dataset.csv

src/
│
├── api/
│   └── main.py
│
├── data_processing/
│   └── preprocessing.py
│
├── inference/
│   └── predict.py
│
├── models/
│   └── lstm_model.py
│
├── training/
│   └── train.py

ui/
│
└── simple_app.py
