import streamlit as st
import requests
import pandas as pd


API_URL = "http://127.0.0.1:8000/predict"


st.set_page_config(
    page_title="AI Weather Forecast",
    page_icon="🌦️"
)

st.title("🌦️ AI Weather Forecasting")

st.write(
    "Enter a city and future date "
    "to predict weather."
)

# City input
cities = [

    "Mumbai",
    "Delhi",
    "Bengaluru",
    "Chennai",
    "Hyderabad",
    "Kolkata",
    "Pune",
    "Ahmedabad",
    "Jaipur",
    "Lucknow",
    "Surat",
    "Kanpur",
    "Nagpur",
    "Indore",
    "Bhopal",
    "Patna",
    "Visakhapatnam",
    "Coimbatore",
    "Kochi",
    "Thiruvananthapuram",
    "Madurai",
    "Mysuru",
    "Vijayawada",
    "Chandigarh",
    "Goa",
    "Shimla",
    "Dehradun",
    "Ranchi",
    "Raipur",
    "Guwahati"
]

city = st.selectbox(
    "Select City",
    cities
)

# Date input
future_date = st.date_input(
    "Future Date"
)

if st.button("Predict Weather"):

    try:

        # Load historical dataset
        df = pd.read_csv(
            "data/weather_dataset.csv"
        )

        # Use latest 30 days
        latest_data = df.tail(30)

        sequence = []

        for _, row in latest_data.iterrows():

            temp_range = (
                row["max_temp"] -
                row["min_temp"]
            )

            sequence.append([
                row["max_temp"],
                row["min_temp"],
                row["rainfall_mm"],
                temp_range,
                pd.to_datetime(row["date"]).month,
                pd.to_datetime(row["date"]).day
            ])

        payload = {
            "sequence": sequence
        }

        response = requests.post(
            API_URL,
            json=payload
        )

        if response.status_code == 200:

            prediction = response.json()

            st.success(
                f'''
🌍 Weather Forecast for {city}

📅 Date: {future_date}

🌡️ Minimum Temperature:
{prediction["min_temp"]:.2f} °C

☀️ Maximum Temperature:
{prediction["max_temp"]:.2f} °C

🌤️ Average Temperature:
{prediction["mean_temp"]:.2f} °C

🌧️ Projected Rainfall:
{prediction["projected_rainfall"]:.2f} mm
'''
            )

        else:

            st.error(
                "Prediction failed."
            )

    except Exception as e:

        st.error(str(e))