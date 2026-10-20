import streamlit as st
import pandas as pd
import joblib
st.title('Diabetes Risk Predictor')
@st.cache_resource
def load_model():
    return joblib.load('diabetes_model_pipeline.pkl')

pipeline=load_model()
st.success('model loaded succesfullly')
st.subheader('Patient Clinical Markers')
gender=st.selectbox('Gender',['Female','Male','Other'])
age=st.slider('Age',min_value=1,max_value=100,value=45)
hypertension=st.selectbox('Hypertension History(0=No,1=Yes)',[0,1])
heart_disease=st.selectbox('Heart Disease History(0=No,1=Yes)',[0,1])
smoking_history= st.selectbox('Smoking History',['never','current','former','not current','no info'])
bmi=st.number_input('BMI',min_value=10,max_value=100,value=25)
Hba1c_level=st.number_input('HBA1C Level',min_value=6.5,max_value=10.0,value=8.0)
blood_glucose_level=st.slider('Bloog Glucose Level (mg/dl)',min_value=50,max_value=100,value=70)


if st.button('Predict Diabetes Risk',type='primary'):
    input_data=pd.DataFrame([{
        'gender':gender,
        'hypertension':hypertension,
        'heart_disease':heart_disease,
        'smoking_history':smoking_history,
        'bmi':bmi,
        'HbA1c_level':Hba1c_level,
        'blood_glucose_level':blood_glucose_level,
        'age':age
        }])

####generate prediction using loaded data
    prediction=pipeline.predict(input_data)[0]

    st.divider()
    if prediction==1:
        st.error('High Risk of diabetes predicted')
    else :
        st.success('low risk of diabetes detected')