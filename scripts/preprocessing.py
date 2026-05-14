import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


class WeatherPreprocessor:

    def __init__(self, sequence_length=30):
        print("Loading preprocessing module...")
        print("Loading dataset...")
        self.sequence_length = sequence_length
        self.scaler = MinMaxScaler()

    def load_data(self, file_path):

        df = pd.read_csv(file_path)

        df["date"] = pd.to_datetime(df["date"])

        df = df.sort_values("date")

        return df

    def clean_data(self, df):
        print("Cleaning data...")
        numerical_columns = df.select_dtypes(include=np.number).columns

        for col in numerical_columns:
            df[col] = df[col].fillna(df[col].mean())

        return df

    def feature_engineering(self, df):
        print("Performing feature engineering...")
        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month
        df["day"] = df["date"].dt.day

        df["temp_range"] = df["max_temp"] - df["min_temp"]

        return df

    def normalize_features(self, df):
        print("Normalizing features...")
        features = [
            "max_temp",
            "min_temp",
            "rainfall_mm",
            "temp_range",
            "month",
            "day"
        ]

        scaled_features = self.scaler.fit_transform(df[features])

        return scaled_features

    def create_sequences(self, features, target):
        print("Creating sequences...")
        X = []
        y = []

        for i in range(self.sequence_length, len(features)):

            X.append(features[i-self.sequence_length:i])

            y.append(target[i])

        return np.array(X), np.array(y)