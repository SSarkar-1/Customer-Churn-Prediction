# Customer Churn Prediction

## Project Overview
This project focuses on predicting customer churn risk using machine learning techniques. By analyzing customer behavior and transactional data, the model classifies customers into different churn risk categories (1 to 5), enabling businesses to proactively identify and retain at-risk customers. The project is deployed as an interactive Streamlit web application for real-time churn risk assessment.

## Problem Statement
Customer churn is a critical challenge for businesses, impacting revenue and growth. Early identification of customers likely to churn allows targeted retention strategies, improving customer lifetime value and reducing acquisition costs. This project leverages classification algorithms to predict churn risk scores based on customer demographics, engagement, and feedback data.

## Dataset
The dataset includes customer demographics, transaction history, engagement metrics, and feedback. Key features include:
- Age, Gender, Region Category
- Membership Category, Referral Status
- Preferred Offer Types, Medium of Operation
- Login frequency, Average time spent, Transaction value
- Points in wallet, Discount usage, Complaint history
- Customer feedback and complaint status

The dataset was preprocessed by removing irrelevant columns, handling missing values, encoding categorical variables, and scaling numerical features.

## Exploratory Data Analysis (EDA)
- Visualized distributions of churn risk scores across membership categories and feedback types.
- Analyzed relationships between churn risk and transaction value, points in wallet, and time spent.
- Identified and treated outliers using interquartile range (IQR) filtering.
- Explored feature correlations to inform model selection.

## Model Development
- Multiple classification models were evaluated: Random Forest, Support Vector Machine, Logistic Regression, Decision Tree, and Gaussian Naive Bayes.
- Hyperparameter tuning was performed using GridSearchCV with 5-fold cross-validation.
- Random Forest Classifier with 20 estimators was selected based on best performance.
- A robust pipeline was created combining preprocessing (encoding, scaling) and the trained model.

## Deployment
- The trained pipeline was saved using joblib.
- A Streamlit app was developed to provide an intuitive UI for inputting customer data and displaying churn risk predictions.
- The app categorizes churn risk into five levels with color-coded risk scores and descriptive labels.
- Deployment link: [Customer Churn Prediction App](https://customer-churn-prediction-ss.streamlit.app/)

## Technologies and Libraries
- Python 3.x
- pandas, numpy for data manipulation
- scikit-learn for machine learning and model tuning
- matplotlib, seaborn for data visualization
- joblib for model serialization
- Streamlit for interactive web app deployment

## How to Run Locally
1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
4. Access the app in your browser at
🔍 Key Highlights:
- Comprehensive data preprocessing and feature engineering
- Evaluation of multiple ML models with hyperparameter tuning
- Deployment of an interactive Streamlit app for real-time predictions
- Scalable pipeline combining preprocessing and model inference

🔧 Tech Stack: Python, scikit-learn, Streamlit, pandas, numpy, joblib

🌐 Check out the live app here: [https://customer-churn-prediction-ss.streamlit.app/](https://customer-churn-prediction-ss.streamlit.app/)

Looking ahead, I’m excited about integrating AI-driven customer insights with CRM platforms and exploring deep learning for even more accurate predictions. The future of customer retention is intelligent, proactive, and data-driven!

Feel free to try the app and share your feedback or collaboration ideas. Let’s innovate together! 💡

#MachineLearning #CustomerChurn #DataScience #AI #Streamlit #Python #CustomerRetention #PredictiveAnalytics
