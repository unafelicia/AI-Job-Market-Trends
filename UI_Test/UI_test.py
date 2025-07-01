import streamlit as st
import joblib
import numpy as np

model = joblib.load("salary_prediction_model.pkl")

st.title("AI Job Salary Estimator")
st.markdown("Estimate your AI job salary based on your profile.")

experience = st.selectbox("Experience Level", ["EN", "MI", "SE", "EX"])
employment = st.selectbox("Employment Type", ["FT", "PT", "CT", "FL"])
company_location = st.selectbox("Company Location", ["United States", "Germany", "India", "France", "Other"])
company_size = st.selectbox("Company Size", ["S", "M", "L"])
employee_location = st.selectbox("Employee Residence", ["United States", "Germany", "India", "France", "Other"])
remote_ratio = st.slider("Remote Work Ratio", 0, 100, 50)
education = st.selectbox("Education Level", ["Bachelor", "Master", "PhD", "Associate", "Other"])
years_experience = st.slider("Years of Experience", 0, 25, 3)
industry = st.selectbox("Industry", ["Technology", "Healthcare", "Finance", "Retail", "Other"])

map_dict = {
    "experience": {"EN": 0, "MI": 1, "SE": 2, "EX": 3},
    "employment": {"FT": 0, "PT": 1, "CT": 2, "FL": 3},
    "company_location": {"United States": 0, "Germany": 1, "India": 2, "France": 3, "Other": 4},
    "company_size": {"S": 0, "M": 1, "L": 2},
    "employee_location": {"United States": 0, "Germany": 1, "India": 2, "France": 3, "Other": 4},
    "education": {"Bachelor": 0, "Master": 1, "PhD": 2, "Associate": 3, "Other": 4},
    "industry": {"Technology": 0, "Healthcare": 1, "Finance": 2, "Retail": 3, "Other": 4}
}


input_features = [
    map_dict["experience"][experience],
    map_dict["employment"][employment],
    map_dict["company_location"][company_location],
    map_dict["company_size"][company_size],
    map_dict["employee_location"][employee_location],
    remote_ratio,
    map_dict["education"][education],
    years_experience,
    map_dict["industry"][industry]
]


if st.button("Predict Salary"):
    prediction = model.predict([input_features])[0]
    st.success(f"💰 Estimated Salary: ${prediction:,.2f}")