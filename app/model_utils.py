import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "logistic_regression_onehot.pkl"
)

model = joblib.load(MODEL_PATH)

print("✅ One-Hot Encoding model loaded successfully")


def predict_heart_disease(data):

    input_data = pd.DataFrame([{
        "age": data["age"],
        "sex": data["sex"],
        "chest_pain_type": data["chest_pain_type"],
        "Max_heart_rate": data["Max_heart_rate"],
        "exercise_induced_angina": data["exercise_induced_angina"],
        "oldpeak": data["oldpeak"],
        "slope": data["slope"],
        "vessels_colored_by_flourosopy": data["vessels_colored_by_flourosopy"],
        "thalassemia": data["thalassemia"]
    }])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    confidence = round(max(probability) * 100, 2)

    return prediction, confidence
