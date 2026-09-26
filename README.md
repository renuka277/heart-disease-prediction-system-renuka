# ❤️ Heart Disease Prediction System

A Machine Learning based web application that predicts the likelihood of heart disease using patient clinical data.

---

## 📌 Project Overview

Heart Disease Prediction System is an AI-powered web application developed using **Python**, **Flask**, and **Machine Learning**.

The application predicts whether a patient is at **High Risk** or **Low Risk** of heart disease based on clinical parameters.

The prediction model is built using **Logistic Regression**, which achieved an accuracy of **80.33%** on the test dataset.

---

## 🚀 Features

- ❤️ Heart Disease Risk Prediction
- 🤖 Machine Learning Powered
- 📊 Logistic Regression Model
- 📈 Prediction Confidence Score
- 💡 Medical Recommendation
- 🌐 Flask Web Application
- 📱 Responsive User Interface

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- HTML5
- CSS3
- Bootstrap 5

---

## 📂 Project Structure

```text
Heart Disease Prediction/
│
├── app/
│   ├── app.py
│   ├── model_utils.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── predict.html
│   │   └── result.html
│   ├── static/
│   │   ├── style.css
│   │   ├── script.js
│   │   └── assets/
│
├── dataset/
│
├── models/
│   ├── logistic_regression_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Feature Scaling
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Saving
10. Flask Deployment

---

## 📈 Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | **80.33%** |
| Decision Tree | 73.77% |
| Random Forest | 78.69% |
| K-Nearest Neighbors | 85.25% |

> **Selected Model:** Logistic Regression

Although KNN achieved higher accuracy, Logistic Regression was selected because it provides a simpler, more interpretable model suitable for healthcare prediction and deployment.

---


## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/heart-disease-prediction.git
```

Move into the project folder

```bash
cd "Heart Disease Prediction"
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
cd app
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📌 Dataset

UCI Heart Disease Dataset

---

## 👩‍💻 Developer

**Renuka T**

B.Tech - Artificial Intelligence & Machine Learning

Pragati Engineering College

---

## ⭐ Future Enhancements

- Support additional Machine Learning models
- Patient history management
- Doctor dashboard
- Cloud deployment
- Improved prediction visualization

---

## 📄 License

This project is developed for educational purposes.