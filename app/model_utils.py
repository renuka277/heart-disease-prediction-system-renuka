# ==========================================
# MODEL UTILITIES
# Heart Disease Prediction
# ==========================================

import joblib
import numpy as np
import os

# ------------------------------------------------
# Load Saved Model and Scaler
# ------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "logistic_regression_model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "scaler.pkl"
)

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

print("✅ Model Loaded Successfully")
print("✅ Scaler Loaded Successfully")
# ------------------------------------------------
# Value Mappings
# ------------------------------------------------

gender_map = {
    "Male": 1,
    "Female": 0
}

chest_pain_map = {
    "Typical Angina": 3,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 0
}

exercise_angina_map = {
    "Yes": 1,
    "No": 0
}

slope_map = {
    "Upsloping": 2,
    "Flat": 1,
    "Downsloping": 0
}

thalassemia_map = {
    "Normal": 1,
    "Fixed Defect": 0,
    "Reversible Defect": 2
}


# ------------------------------------------------
# Prediction Function
# ------------------------------------------------

def predict_heart_disease(data):

    input_data = np.array([[
        data["age"],
        gender_map[data["sex"]],
        chest_pain_map[data["chest_pain_type"]],
        data["Max_heart_rate"],
        exercise_angina_map[data["exercise_induced_angina"]],
        data["oldpeak"],
        slope_map[data["slope"]],
        int(data["vessels_colored_by_flourosopy"]),
        thalassemia_map[data["thalassemia"]]
    ]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(input_scaled)[0]

    confidence = round(max(probability) * 100, 2)

    return prediction, confidence