# backend/train.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.metrics import r2_score
import joblib
import os

# ——— SMART PATH: works locally AND on Render ———
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "processed_data_set.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "best_soil_model.pkl")

# Create models folder if not exists
os.makedirs(MODEL_DIR, exist_ok=True)

print("Loading dataset...")
df = pd.read_csv(DATA_PATH)

# Features & target
X = df.drop("Vegetation Cover", axis=1)
y = df["Vegetation Cover"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Models
models = {
    "RandomForest": RandomForestRegressor(n_estimators=300, random_state=42),
    "XGBoost": XGBRegressor(n_estimators=300, learning_rate=0.1, random_state=42),
    "GradientBoosting": GradientBoostingRegressor(n_estimators=300, random_state=42),
    "LinearRegression": LinearRegression(),
    "SVR": SVR(kernel='rbf')
}

best_model = None
best_score = 0
best_name = ""

print("Training models...")
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    score = r2_score(y_test, pred)
    print(f"{name}: R² = {score:.4f}")
    
    if score > best_score:
        best_score = score
        best_model = model
        best_name = name

# Save the best model
# Save the best model
joblib.dump(best_model, MODEL_PATH)

print(f"\nBEST MODEL: {best_name} → R² = {best_score:.4f}")
print(f"Model saved successfully at: {MODEL_PATH}")
print("Training completed! App ready to predict.")
