from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout


def build_lstm_model(input_shape):

    model = Sequential()

    model.add(
        LSTM(
            units=64,
            return_sequences=True,
            input_shape=input_shape
        )
    )

    model.add(Dropout(0.2))

    model.add(LSTM(units=32))

    model.add(Dropout(0.2))

    model.add(Dense(1))

    model.compile(
        optimizer="adam",
        loss="mse",
        metrics=["mae"]
    )

    return model