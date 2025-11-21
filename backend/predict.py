# backend/predict.py
import joblib
import numpy as np
import os

# Same smart path as train.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_soil_model.pkl")

# Load model
model = joblib.load(MODEL_PATH)

def predict_fertility(input_data):
    """
    input_data: list of 14 values in order:
    [NO3, NH4, P, K, SO4, B, OM, pH, Zn, Cu, Fe, Ca, Mg, Na]
    """
    pred = model.predict(np.array(input_data).reshape(1, -1))[0]
    return round(float(pred), 2)