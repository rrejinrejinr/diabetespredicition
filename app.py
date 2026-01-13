import streamlit as st
import joblib
import numpy as np

model=joblib.load("diabetesprediction")
st.title("Diabetes Prediction System")
=st.number_input("Enter the work Experience",min_value=0,max_value=50,step=1,format="%d")
jobrate=st.number_input("Enter the job Rate")

if st.button("Predict"):
  result=model.predict([[years,jobrate]])
  st.write("Predict the Annual Salary",result)




import streamlit as st
import numpy as np


model=joblib.load("diabetesprediction")


st.title("Diabetes Prediction App")
st.write("Enter the patient details below to predict diabetes.")


pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
glucose = st.number_input("Glucose Level", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin Level", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0, step=1)


if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure,
                             skin_thickness, insulin, bmi, dpf, age]])

    

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ The person is **Diabetic**")
    else:
        st.success("✅ The person is **Not Diabetic**")
