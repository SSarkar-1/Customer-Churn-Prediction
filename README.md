# Customer Churn Prediction



## Overview

This project aims to predict customer churn using a machine learning model deployed on a web application. The project leverages a dataset of customer information and behavior to train a model that can accurately predict the likelihood of a customer churning.

## Technical Details

Dataset: The dataset used for this project is not publicly available, but it contains information on customer demographics, behavior, and transaction history.

Model: The model used is a Random Forest Classifier, trained on a pipeline of feature engineering and preprocessing steps. The model is saved as a joblib file (Model_pipeline) and loaded into the web application.

Web Application: The web application is built using Streamlit, a Python framework for building web applications. The application allows users to input customer information and receive a predicted churn risk score.

Deployment: The web application is deployed on Streamlit's cloud platform, allowing for easy sharing and collaboration.

## Files

Churn_Predictor.ipynb: Jupyter Notebook containing the data preprocessing, feature engineering, and model training code.

app.py: Streamlit web application code, including the user interface and model deployment.

Test.ipynb: Jupyter Notebook containing test code for the model and web application.

requirements.txt: List of dependencies required to run the project.

Model_pipeline: Joblib file containing the trained model.

model_jbl: Backup of the trained model.
