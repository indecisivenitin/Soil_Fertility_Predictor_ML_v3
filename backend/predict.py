# backend/predict.py
import joblib
import numpy as np
import os
import subprocess

# Smart path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_soil_model.pkl")

# ——— CRITICAL: Train model if it doesn't exist ———
if not os.path.exists(MODEL_PATH):
    print("MODEL NOT FOUND → AUTO TRAINING NOW...")
    # Create models folder
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    # Run training script
    result = subprocess.call(["python", os.path.join(BASE_DIR, "backend", "train.py")])
    if result != 0:
        raise Exception("Training failed!")
    print("MODEL TRAINED & SAVED SUCCESSFULLY")

# Now safely load the model
model = joblib.load(MODEL_PATH)
print("Model loaded → Ready for predictions!")

def predict_fertility(input_data):
    pred = model.predict(np.array(input_data).reshape(1, -1))[0]
    return round(float(pred), 2)