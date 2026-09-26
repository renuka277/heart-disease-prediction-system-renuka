# ==========================================
# HEART DISEASE PREDICTION SYSTEM
# Flask Backend
# ==========================================

from flask import Flask, render_template, request
from model_utils import predict_heart_disease

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        user_data = {
            "age": int(request.form["age"]),
            "sex": request.form["sex"],
            "chest_pain_type": request.form["chest_pain_type"],
            "Max_heart_rate": int(request.form["Max_heart_rate"]),
            "exercise_induced_angina": request.form["exercise_induced_angina"],
            "oldpeak": float(request.form["oldpeak"]),
            "slope": request.form["slope"],
            "vessels_colored_by_flourosopy": request.form["vessels_colored_by_flourosopy"],
            "thalassemia": request.form["thalassemia"]
        }

        prediction, confidence = predict_heart_disease(user_data)

        if prediction == 1:
            result = "High Risk"
            color = "danger"
            recommendation = (
                "Please consult a cardiologist. "
                "Maintain a healthy diet, exercise regularly, "
                "and monitor your heart health."
            )
        else:
            result = "Low Risk"
            color = "success"
            recommendation = (
                "Maintain your healthy lifestyle and "
                "schedule regular health check-ups."
            )

        return render_template(
            "result.html",
            prediction=result,
            confidence=confidence,
            color=color,
            recommendation=recommendation
        )

    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)