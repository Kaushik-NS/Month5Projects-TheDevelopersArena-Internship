import numpy as np

from keras.models import load_model


class WeatherPredictor:

    def __init__(self):

        self.min_model = load_model(
            "min_temp_model.h5",
            compile=False
        )

        self.max_model = load_model(
            "max_temp_model.h5",
            compile=False
        )

        self.mean_model = load_model(
            "mean_temp_model.h5",
            compile=False
        )

        self.rainfall_model = load_model(
            "rainfall_model.h5",
            compile=False
        )

    def predict_weather(self, sequence):

        sequence_array = np.array(sequence)

        sequence_array = np.expand_dims(
            sequence_array,
            axis=0
        )

        min_temp = self.min_model.predict(
            sequence_array
        )[0][0]

        max_temp = self.max_model.predict(
            sequence_array
        )[0][0]

        mean_temp = self.mean_model.predict(
            sequence_array
        )[0][0]

        rainfall = self.rainfall_model.predict(
            sequence_array
        )[0][0]

        return {

            "min_temp": float(min_temp),

            "max_temp": float(max_temp),

            "mean_temp": float(mean_temp),

            "projected_rainfall": float(rainfall)
        }