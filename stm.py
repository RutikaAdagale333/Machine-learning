import streamlit as st
import pickle
import numpy as np

# Load the trained ML model
model = pickle.load(open('c:\\Users\\Rutesh\\OneDrive\\Desktop\\ML_pro\\Model\\ML_Model1.pkl', 'rb'))

# Function to predict loan eligibility
def predict_eligibility(gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_term, credit_history, property_area):
    input_data = np.array([[gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_term, credit_history, property_area]])
    prediction = model.predict(input_data)
    return prediction

# Streamlit UI for user input
st.title("Loan Eligibility Prediction")

st.sidebar.header("User Input")

# Input fields for the loan eligibility criteria
gender= st.sidebar.selectbox("Gender", ['Male', 'Female'])
married = st.sidebar.selectbox("Marital Status", ['Married', 'Single'])
dependents = st.sidebar.selectbox("Dependents", [0, 1, 2, 3])
education = st.sidebar.selectbox("Education", ['Graduate', 'Not Graduate'])
self_employed = st.sidebar.selectbox("Self-Employed", ['Yes', 'No'])
applicant_income = st.sidebar.number_input("Applicant Income ", min_value=0)
coapplicant_income = st.sidebar.number_input("Coapplicant Income", min_value=0)
loan_amount = st.sidebar.number_input("Loan Amount", min_value=0)
loan_term = st.sidebar.number_input("Loan Term (in years)", min_value=1, max_value=30)
credit_history = st.sidebar.selectbox("Credit History(Yes=1 No=0)", [0, 1])  # 0 = No, 1 = Yes
property_area = st.sidebar.selectbox("Property Area", ['Urban', 'Semiurban', 'Rural'])

# Preprocessing user input
gender = 1 if gender == 'Male' else 0
married = 1 if married == 'Married' else 0
education = 1 if education == 'Graduate' else 0
self_employed = 1 if self_employed == 'Yes' else 0
property_area = ['Urban', 'Semiurban', 'Rural'].index(property_area)

# Prediction button
if st.sidebar.button("Check Loan Eligibility"):
    eligibility = predict_eligibility(gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_term, credit_history, property_area)
    
    if eligibility == 1:
        st.success("Congratulations! You are eligible for the loan.")
        st.image('loan.jpg', caption="You are eligible for the loan!", use_container_width=True)
    else:
        st.error("Sorry, you are not eligible for the loan.")
        st.image('no.jpg', caption="You are not eligible for the loan!", use_container_width=True)