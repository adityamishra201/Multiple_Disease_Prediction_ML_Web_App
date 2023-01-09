# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 14:00:49 2023

@author: Admin
"""


import streamlit as st
import pickle
from streamlit_option_menu import option_menu

heart_model=pickle.load(open('heart_disease_model.sav','rb'))

diabetes_model=pickle.load(open('Predtrained_model.sav','rb'))


#sidebar or navigate

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction'],
                         icons=['activity','heart'],
                         default_index=0)
    
# Diabetes Prediction Page
if(selected=='Diabetes Prediction'):
    # Page title
    st.title('Diabetes Prediction using ML')
    
    
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies')
    with col2:
        Glucose = st.number_input('Glucose Level')
    with col3:
        BloodPressure = st.number_input('Blood Pressure value')
    with col1:
        SkinThickness = st.number_input('Skin Thickness value')
    with col2:
        Insulin = st.number_input('Insulin Level')
    with col3:
        BMI = st.number_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.number_input('Age of the Person')
    
    diab_diagnosis=''
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis='The person is diabetic'
        else:
            diab_diagnosis='The person is Not diabetic'
    st.success(diab_diagnosis)
    
    
    
    

# Heart Disease Prediction Page
if(selected=='Heart Disease Prediction'):
    # Page title
    st.title('Heart Disease Prediction using ML')
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        Age= st.number_input('Age of the Person')
    with col2:
        sex = st.number_input('Sex of the person')
    with col3:
        cp = st.number_input('Cp value')
    with col1:
        trestbps = st.number_input('Trestbps value')
    with col2:
        chol = st.number_input('Chol Level')
    with col3:
        fbs = st.number_input('FBS value')
    with col1:
        restecg = st.number_input('restecg value')
    with col2:
        thalach = st.number_input('Thalach value')
    with col3:
        exang = st.number_input('Exang value')
    with col1:
        oldpeak = st.number_input('Oldpeak value')
    with col2:
        slope = st.number_input('Slope value')
    with col3:
        ca = st.number_input('CA value')
    with col1:
        thal = st.number_input('Thal value')
        
        
        
    heart_diagnosis=''
    
    if st.button('Heart Test Result'):
        heart_prediction=heart_model.predict([[Age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if(heart_prediction[0]==1):
            heart_diagnosis='The person is sufering from Heart Disease'
        else:
            heart_diagnosis='The person is Healthy'
    st.success(heart_diagnosis)