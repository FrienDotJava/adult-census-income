import streamlit as st
import pandas as pd
import joblib

@st.cache_resource
def load_model():
    return joblib.load("income_gbc.pkl")

model = load_model()

st.title('Income Prediction')

age = st.number_input('Age')

education_to_num = {
"Preschool": 1, "1st-4th": 2, "5th-6th": 3, "7th-8th": 4,
"9th": 5, "10th": 6, "11th": 7, "12th": 8,
"HS-grad": 9, "Some-college": 10, "Assoc-voc": 11, "Assoc-acdm": 12,
"Bachelors": 13, "Masters": 14, "Prof-school": 15, "Doctorate": 16
}

education = st.selectbox("Education", list(education_to_num.keys()))
education_num = education_to_num[education]

occupation = st.selectbox("Occupation", [
"Tech-support","Craft-repair","Other-service","Sales","Exec-managerial", "Prof-specialty","Handlers-cleaners","Machine-op-inspct","Adm-clerical", "Farming-fishing","Transport-moving","Priv-house-serv", "Protective-serv","Armed-Forces"])

hours_per_week = st.number_input('Working hours per week')
marital_status = st.selectbox('Marital Status', ['Widowed', 'Divorced', 'Separated', 'Never-married', 'Married-civ-spouse', 'Married-spouse-absent', 'Married-AF-spouse'])


row = {
    "age": age,
    "education.num": education_num,
    "marital.status": marital_status,
    "occupation": occupation,
    "capital.gain": 0,
    "capital.loss": 0,
    "hours.per.week": hours_per_week
}
X_new = pd.DataFrame([row])
st.write(X_new)
if st.button("Predict"):
    pred = model.predict(X_new)[0]
    proba = model.predict_proba(X_new)[0, 1]
    label = ">50K" if pred == 1 else "<=50K"
    st.success(f"Prediction: {label} — Probability: {proba:.3f}")