# Student Performance Prediction

## Overview

This project predicts student performance based on study habits and academic factors using Machine Learning. The application takes inputs such as study hours, attendance, previous scores, and sleep hours to estimate a student's performance.

## Features

* Student performance prediction using Machine Learning
* Data preprocessing and model training
* Interactive Streamlit web application
* FastAPI backend API
* Real-time prediction system

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* FastAPI
* Joblib

## Project Structure

Student_Performance_Prediction/

├── app.py

├── model.py

├── dataset.csv

├── student_model.pkl

├── main.py

├── requirements.txt

└── README.md

## How to Run

Install dependencies:

pip install -r requirements.txt

Train the model:

python model.py

Run the Streamlit application:

streamlit run app.py

Run the FastAPI backend:

uvicorn main:app --reload

## Future Improvements

* Advanced feature engineering
* Multiple ML model comparison
* Cloud deployment
* Interactive analytics dashboard

## Author

Parvathy S
