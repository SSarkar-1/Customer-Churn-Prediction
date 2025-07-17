import streamlit as st
import numpy as np
import pickle 
import pandas as pd

with open('C:/Users/SHUBHAM SARKAR/Desktop/ML Algorithms/Customer Churn Prediction/Customer-Churn-Prediction/Model_pipeline','rb') as f:
    loaded_pipeline=pickle.load(f)

def churn_prediction(input_data):
    feature_names=['age', 'gender',
       'region_category', 'membership_category','joined_through_referral', 'preferred_offer_types',
       'medium_of_operation',
       'days_since_last_login', 'avg_time_spent', 'avg_transaction_value',
       'avg_frequency_login_days', 'points_in_wallet', 'used_special_discount',
       'offer_application_preference','past_complaint', 'complaint_status',
       'feedback']
    df = pd.DataFrame([input_data], columns=feature_names)
    
    prediction=loaded_pipeline.predict(df)
    print(prediction)
    
    return prediction.item()

def main():
    st.title(":orange[Customer Churn Prediction]")
    st.header(":violet[Find about to churn customers and retain them]")

    age=st.number_input("Age of Person",min_value=1.0,max_value=100.0,format="%.2f")
    if age > 100:
        st.warning("Age cannot be more than 100!")
    if age < 1:
        st.warning("Age cannot be less than 1!")

    gender=st.radio("Select Gender :",('M','F'))

    region_category=st.selectbox("Region Type",['City','Town','Village'])

    membership_category=st.selectbox("Membership Category",['No Membership','Basic Membership','Premium Membership','Silver Membership','Gold Membership','Platinum Membership'])

    joined_through_referral=st.selectbox("Joined Through Referral?",['Yes','No'])

    preferred_offer_types=st.selectbox("Preferred offer Types",['Without Offers','Gift Vouchers/Coupons','Credit/Debit Card Offers'])

    medium_of_operation=st.selectbox("Medium of Operation",['Desktop','Smartphone','Both'])

    days_since_last_login=st.number_input("Days Since Last Login",min_value=0.0,format="%.2f")
    if days_since_last_login < 0:
        st.warning("Days Since Last Login cannot be less than 0!")

    avg_time_spent=st.number_input("Average Time Spent",min_value=0.0,format="%.2f")
    if avg_time_spent < 0:
        st.warning("Average Time Spent cannot be less than 0!")
    
    avg_transaction_value=st.number_input("Average Transaction Value",min_value=0.0,format="%.2f")
    if avg_transaction_value < 0:
        st.warning("Average Transaction Value cannot be less than 0!")

    avg_frequency_login_days=st.number_input("Average Frequency Login Days",min_value=0.0,format="%.2f")
    if avg_frequency_login_days < 0:
        st.warning("Average Frequency Login Days cannot be less than 0!")
    
    points_in_wallet=st.number_input("Points in Wallet",format="%.2f")

    used_special_discount=st.selectbox("Used Special Discount?",['Yes','No'])

    offer_application_preference=st.selectbox("Offer Application Preference",['Yes','No'])

    past_complaint=st.selectbox("Past Complaint",['Yes','No'])

    complaint_status=st.selectbox("Complaint Status Currently",['Not Applicable','No Information Available','Unsolved','Solved in Follow-up','Solved'])

    feedback=st.selectbox("Customer Feedback",['Poor Product Quality','Poor Website','No reason specified','Poor Customer Service','Too many ads','Reasonable Price','User Friendly Website','Products always in Stock','Quality Customer Care'])

    prediction=0

    if st.button('Customer Churn Risk'):
        prediction=churn_prediction([age, gender,
       region_category, membership_category,joined_through_referral, preferred_offer_types,
       medium_of_operation,
       days_since_last_login, avg_time_spent, avg_transaction_value,
       avg_frequency_login_days, points_in_wallet, used_special_discount,
       offer_application_preference, past_complaint, complaint_status,
       feedback])
        
    color_map = {
    1: "🟩",
    2: "🟨",
    3: "🟧",
    4: "🟥",
    5: "🟥"}

   
    labels = {
        1: "Very Low Risk",
        2: "Low Risk",
        3: "Moderate Risk",
        4: "High Risk",
        5: "Very High Risk"
    }
    st.metric(label=f"Score {prediction}", value=color_map[prediction])
    st.success(f"Predicted Risk Score: {prediction} → {labels[prediction]}")
    #st.success(prediction)

if __name__=='__main__':
    main()