# -*- coding: utf-8 -*-
"""
Updated on Fri Jan 4 2025

@modified_by: Assistant
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
try:
    diabetes_model = pickle.load(open('C:/Users/Admin/OneDrive/Desktop/Multiple Disease Prediction System/saved models/diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('C:/Users/Admin/OneDrive/Desktop/Multiple Disease Prediction System/saved models/heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open('C:/Users/Admin/OneDrive/Desktop/Multiple Disease Prediction System/saved models/parkinsons_model.sav', 'rb'))
except FileNotFoundError as e:
    st.error(f"Error loading models: {e}")

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        'Disease Prediction System',
        ['Overview', 'Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"],
        icons=['info-circle', 'activity', 'heart-pulse', 'brain'], 
        default_index=0,
        styles={
            "nav-link-selected": {"background-color": "#FF6347"},  
            "icon": {"color": "white", "font-size": "18px"},
        }
    )

# Overview Page
if selected == 'Overview':
    st.title('Disease Prediction System')
    st.write("""
    This system provides predictions for three major diseases:
    - **Diabetes**: A chronic condition that affects how your body processes blood sugar (glucose).
    - **Heart Disease**: A range of conditions affecting the heart, including coronary artery disease and more.
    - **Parkinson’s Disease**: A progressive nervous system disorder that affects movement.
    
    Use the sidebar to select a disease prediction module, input the required parameters, and get an instant prediction.
    """)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        pregnancies = st.number_input('Number of Pregnancies', min_value=0, format="%d")
    with col2:
        glucose = st.number_input('Glucose Level', min_value=0.0)
    with col3:
        blood_pressure = st.number_input('Blood Pressure', min_value=0.0)
    with col1:
        skin_thickness = st.number_input('Skin Thickness', min_value=0.0)
    with col2:
        insulin = st.number_input('Insulin Level', min_value=0.0)
    with col3:
        bmi = st.number_input('BMI', min_value=0.0)
    with col1:
        diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0)
    with col2:
        age = st.number_input('Age', min_value=0, format="%d")

    # Prediction
    if st.button('Predict Diabetes', help="Click to predict"):
        try:
            features = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]]
            prediction = diabetes_model.predict(features)
            result = "The person is diabetic" if prediction[0] == 1 else "The person is not diabetic"
            st.success(result)
        except Exception as e:
            st.error(f"Error in prediction: {e}")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction')

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=0, format="%d")
    with col2:
        sex = st.selectbox('Sex (0: Female, 1: Male)', [0, 1])
    with col3:
        cp = st.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3, format="%d")
    with col1:
        trestbps = st.number_input('Resting Blood Pressure', min_value=0.0)
    with col2:
        chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=0.0)
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (0: No, 1: Yes)', [0, 1])
    with col1:
        restecg = st.number_input('Resting ECG (0-2)', min_value=0, max_value=2, format="%d")
    with col2:
        thalach = st.number_input('Max Heart Rate Achieved', min_value=0.0)
    with col3:
        exang = st.selectbox('Exercise-Induced Angina (0: No, 1: Yes)', [0, 1])
    with col1:
        oldpeak = st.number_input('ST Depression', min_value=0.0)
    with col2:
        slope = st.number_input('Slope of ST Segment (0-2)', min_value=0, max_value=2, format="%d")
    with col3:
        ca = st.number_input('Major Vessels (0-3)', min_value=0, max_value=3, format="%d")
    with col1:
        thal = st.number_input('Thalassemia (0-3)', min_value=0, max_value=3, format="%d")

    # Prediction
    if st.button('Predict Heart Disease', help="Click to predict"):
        try:
            features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            prediction = heart_disease_model.predict(features)
            result = "The person has heart disease" if prediction[0] == 1 else "The person does not have heart disease"
            st.success(result)
        except Exception as e:
            st.error(f"Error in prediction: {e}")

# Parkinson's Prediction Page
if selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction")

    # Input fields
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0)
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0)
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0)
    with col4:
        jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0)
    with col1:
        jitter_abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0)
    with col2:
        rap = st.number_input('MDVP:RAP', min_value=0.0)
    with col3:
        ppq = st.number_input('MDVP:PPQ', min_value=0.0)
    with col4:
        ddp = st.number_input('Jitter:DDP', min_value=0.0)
    with col1:
        shimmer = st.number_input('MDVP:Shimmer', min_value=0.0)
    with col2:
        shimmer_db = st.number_input('MDVP:Shimmer(dB)', min_value=0.0)
    with col3:
        apq3 = st.number_input('Shimmer:APQ3', min_value=0.0)
    with col4:
        apq5 = st.number_input('Shimmer:APQ5', min_value=0.0)
    with col1:
        apq = st.number_input('MDVP:APQ', min_value=0.0)
    with col2:
        dda = st.number_input('Shimmer:DDA', min_value=0.0)
    with col3:
        nhr = st.number_input('NHR', min_value=0.0)
    with col4:
        hnr = st.number_input('HNR', min_value=0.0)
    with col1:
        rpde = st.number_input('RPDE', min_value=0.0)
    with col2:
        dfa = st.number_input('DFA', min_value=0.0)
    with col3:
        spread1 = st.number_input('Spread1', min_value=-10.0)  # Allows negative values
    with col4:
        spread2 = st.number_input('Spread2', min_value=0.0)
    with col1:
        d2 = st.number_input('D2', min_value=0.0)
    with col2:
        ppe = st.number_input('PPE', min_value=0.0)

    # Prediction
    if st.button("Predict Parkinson's Disease", help="Click to predict"):
        try:
            features = [[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]]
            prediction = parkinsons_model.predict(features)
            result = "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
            st.success(result)
        except Exception as e:
            st.error(f"Error in prediction: {e}")
