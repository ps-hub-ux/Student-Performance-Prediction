from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("student_model.pkl")

@app.get("/")
def home():
    return {"message": "Student Performance API Working"}

@app.get("/predict")
def predict(hours: int, attendance: int, previous: int, sleep: int):

    features = np.array([
        [hours, attendance, previous, sleep]
    ])

    prediction = model.predict(features)

    return {
        "Predicted Performance": round(prediction[0], 2)
    }