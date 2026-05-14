import logging
import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)

from keras.callbacks import EarlyStopping

from src.data_processing.preprocessing import WeatherPreprocessor
from src.models.lstm_model import build_lstm_model


# ==========================================
# LOGGING CONFIGURATION
# ==========================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DATA_PATH = "data/weather_dataset.csv"


def train_pipeline():

    logging.info("===================================")
    logging.info("WEATHER FORECAST TRAINING STARTED")
    logging.info("===================================")

    # ==========================================
    # STEP 1 - INITIALIZE PREPROCESSOR
    # ==========================================

    logging.info("[STEP 1] Initializing preprocessor...")

    preprocessor = WeatherPreprocessor(
        sequence_length=30
    )

    logging.info(
        "[SUCCESS] Preprocessor initialized."
    )

    # ==========================================
    # STEP 2 - LOAD DATASET
    # ==========================================

    logging.info("[STEP 2] Loading dataset...")

    df = preprocessor.load_data(
        DATA_PATH
    )

    logging.info(
        f"[SUCCESS] Dataset loaded successfully. Shape: {df.shape}"
    )

    # ==========================================
    # STEP 3 - CLEAN DATA
    # ==========================================

    logging.info("[STEP 3] Cleaning dataset...")

    df = preprocessor.clean_data(df)

    logging.info(
        "[SUCCESS] Data cleaning completed."
    )

    # ==========================================
    # STEP 4 - FEATURE ENGINEERING
    # ==========================================

    logging.info(
        "[STEP 4] Performing feature engineering..."
    )

    df = preprocessor.feature_engineering(df)

    logging.info(
        "[SUCCESS] Feature engineering completed."
    )

    # ==========================================
    # STEP 5 - NORMALIZE FEATURES
    # ==========================================

    logging.info(
        "[STEP 5] Normalizing features..."
    )

    features = preprocessor.normalize_features(df)

    logging.info(
        f"[SUCCESS] Feature normalization completed. Shape: {features.shape}"
    )

    # ==========================================
    # STEP 6 - TARGET EXTRACTION
    # ==========================================

    logging.info(
        "[STEP 6] Extracting target columns..."
    )

    targets = {

        "min_temp": df["min_temp"].values,

        "max_temp": df["max_temp"].values,

        "mean_temp": df["mean_temp"].values,

        "rainfall": df["rainfall_mm"].values
    }

    logging.info(
        "[SUCCESS] Target extraction completed."
    )

    # ==========================================
    # STEP 7 - TRAIN FORECASTING MODELS
    # ==========================================

    logging.info(
        "[STEP 7] Training forecasting models..."
    )

    for model_name, target in targets.items():

        logging.info(
            f"[INFO] Training model for: {model_name}"
        )

        # ==========================================
        # CREATE SEQUENCES
        # ==========================================

        X, y = preprocessor.create_sequences(
            features,
            target
        )

        logging.info(
            f"[SUCCESS] Sequences created for {model_name}"
        )

        logging.info(
            f"[INFO] X Shape: {X.shape}"
        )

        logging.info(
            f"[INFO] y Shape: {y.shape}"
        )

        # ==========================================
        # TRAIN TEST SPLIT
        # ==========================================

        split_index = int(len(X) * 0.8)

        X_train, X_test = (
            X[:split_index],
            X[split_index:]
        )

        y_train, y_test = (
            y[:split_index],
            y[split_index:]
        )

        logging.info(
            "[SUCCESS] Train-test split completed."
        )

        # ==========================================
        # BUILD MODEL
        # ==========================================

        model = build_lstm_model(
            input_shape=(
                X_train.shape[1],
                X_train.shape[2]
            )
        )

        logging.info(
            f"[SUCCESS] {model_name} model built."
        )

        # ==========================================
        # CALLBACKS
        # ==========================================

        early_stopping = EarlyStopping(
            monitor="val_loss",
            patience=5,
            restore_best_weights=True
        )

        # ==========================================
        # TRAIN MODEL
        # ==========================================

        logging.info(
            f"[INFO] Training started for {model_name}"
        )

        model.fit(
            X_train,
            y_train,
            validation_split=0.2,
            epochs=10,
            batch_size=32,
            callbacks=[early_stopping]
        )

        logging.info(
            f"[SUCCESS] Training completed for {model_name}"
        )

        # ==========================================
        # EVALUATE MODEL
        # ==========================================

        predictions = model.predict(X_test)

        mae = mean_absolute_error(
            y_test,
            predictions
        )

        rmse = np.sqrt(
            mean_squared_error(
                y_test,
                predictions
            )
        )

        logging.info(
            f"[RESULT] {model_name} MAE: {mae}"
        )

        logging.info(
            f"[RESULT] {model_name} RMSE: {rmse}"
        )

        # ==========================================
        # SAVE MODEL
        # ==========================================

        model.save(
            f"{model_name}_model.h5"
        )

        logging.info(
            f"[SUCCESS] {model_name} model saved!"
        )

    # ==========================================
    # FINAL LOG
    # ==========================================

    logging.info("===================================")
    logging.info("ALL MODELS TRAINED SUCCESSFULLY")
    logging.info("===================================")


if __name__ == "__main__":

    try:

        train_pipeline()

    except Exception as e:

        logging.error(
            f"[FATAL ERROR] {str(e)}"
        )