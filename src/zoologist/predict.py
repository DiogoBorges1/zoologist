"""
This module loads a trained machine learning model
and makes predictions on new data.
"""

import joblib
import pandas as pd
from sklearn import set_config

set_config(transform_output="pandas")

MODEL_PATH = "models/pipeline_logreg.joblib"


def load_model(model_path: str):
    """Load a trained model from the specified file path."""
    return joblib.load(model_path)


def predict(model, data):
    """Make predictions using the loaded model and input data."""
    return model.predict(data)


if __name__ == "__main__":
    model = load_model(MODEL_PATH)

    sample_data = pd.read_csv("data/sample_input.csv")

    predictions = predict(model, sample_data)
    print("Predictions:", predictions)
