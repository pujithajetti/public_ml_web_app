# -*- coding: utf-8 -*-
"""
Updated on Fri Jan 4 2025

@modified_by: Assistant - Professional UI Design
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Custom CSS for professional AI-themed design
st.markdown("""
<style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main app styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Custom background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Main content area */
    .main > div {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    
    /* Title styling */
    .main-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Section headers */
    .section-header {
        color: #2c3e50;
        font-size: 2.2rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
        position: relative;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -3px;
        left: 0;
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 2px;
    }
    
    /* Input field styling */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        background: rgba(255, 255, 255, 0.9);
        border: 2px solid #e1e8ed;
        border-radius: 12px;
        padding: 0.75rem 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        outline: none;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        width: 100%;
        margin-top: 1rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(0px);
    }
    
    /* Success/Error messages */
    .stAlert {
        border-radius: 12px;
        border: none;
        padding: 1rem 1.5rem;
        margin: 1rem 0;
        font-weight: 500;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
        color: white;
    }
    
    .stError {
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
        color: white;
    }
    
    /* Card-like containers */
    .prediction-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
    }
    
    /* Info cards for overview */
    .info-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.7) 100%);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        transition: transform 0.3s ease;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
    }
    
    .info-card h3 {
        color: #2c3e50;
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .info-card p {
        color: #5a6c7d;
        line-height: 1.6;
        margin: 0;
    }
    
    /* Input labels */
    .stNumberInput label, .stSelectbox label {
        color: #2c3e50 !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Sidebar customization */
    .css-1d391kg {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
    }
    
    /* Hide Streamlit menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* AI-themed decorative elements */
    .ai-decoration {
        position: relative;
        overflow: hidden;
    }
    
    .ai-decoration::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(102, 126, 234, 0.05), transparent);
        animation: shimmer 3s infinite;
        pointer-events: none;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
</style>
""", unsafe_allow_html=True)

# Load the saved models
try:
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
except FileNotFoundError as e:
    st.error(f"⚠️ Error loading models: {e}")

# Sidebar navigation with enhanced styling
with st.sidebar:
    selected = option_menu(
        '🤖 AI Health Predictor',
        ['🏠 Overview', '🩺 Diabetes Prediction', '❤️ Heart Disease Prediction', "🧠 Parkinson's Prediction"],
        icons=['house-fill', 'activity', 'heart-pulse-fill', 'brain'], 
        default_index=0,
        styles={
            "container": {
                "padding": "1rem",
                "background-color": "transparent",
            },
            "nav-link": {
                "font-size": "1rem",
                "text-align": "left",
                "margin": "0.5rem 0",
                "padding": "0.75rem 1rem",
                "border-radius": "12px",
                "color": "#ecf0f1",
                "background-color": "rgba(255,255,255,0.1)",
                "backdrop-filter": "blur(10px)",
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                "color": "white",
                "box-shadow": "0 4px 15px rgba(102, 126, 234, 0.3)",
                "transform": "scale(1.02)",
            },
            "icon": {
                "color": "inherit", 
                "font-size": "1.2rem",
                "margin-right": "0.5rem",
            },
            "menu-title": {
                "color": "#ecf0f1",
                "font-weight": "700",
                "font-size": "1.3rem",
                "text-align": "center",
                "padding": "1rem 0",
                "border-bottom": "2px solid rgba(255,255,255,0.2)",
                "margin-bottom": "1rem",
            }
        }
    )

# Overview Page
if selected == '🏠 Overview':
    st.markdown('<h1 class="main-title">🤖 AI-Powered Disease Prediction System</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="ai-decoration">
        <p style="text-align: center; font-size: 1.2rem; color: #5a6c7d; margin-bottom: 2rem;">
            Harness the power of artificial intelligence to predict potential health conditions with advanced machine learning algorithms.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Disease info cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>🩺 Diabetes Prediction</h3>
            <p>Advanced ML model analyzing glucose levels, BMI, age, and other metabolic factors to predict diabetes risk with high accuracy.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>❤️ Heart Disease Prediction</h3>
            <p>Comprehensive cardiovascular risk assessment using multiple biomarkers and clinical parameters for early detection.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <h3>🧠 Parkinson's Prediction</h3>
            <p>Sophisticated voice analysis and motor function evaluation to identify early signs of Parkinson's disease.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 2rem; padding: 2rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); border-radius: 16px; text-align: center;">
        <h3 style="color: #2c3e50; margin-bottom: 1rem;">🚀 How It Works</h3>
        <p style="color: #5a6c7d; font-size: 1.1rem; line-height: 1.6;">
            Select a prediction module from the sidebar, input your health parameters, and our AI models will provide instant, 
            accurate predictions based on trained data from thousands of medical cases.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Diabetes Prediction Page
elif selected == '🩺 Diabetes Prediction':
    st.markdown('<h1 class="section-header">🩺 Diabetes Risk Assessment</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="prediction-card ai-decoration">
        <p style="color: #5a6c7d; font-size: 1.1rem; margin-bottom: 1.5rem; text-align: center;">
            Enter your health metrics below for AI-powered diabetes risk analysis
        </p>
    """, unsafe_allow_html=True)
    
    # Input fields with better organization
    col1, col2, col3 = st.columns(3)
    with col1:
        pregnancies = st.number_input('👶 Number of Pregnancies', min_value=0, format="%d", help="Total number of pregnancies")
        skin_thickness = st.number_input('📏 Skin Thickness (mm)', min_value=0.0, help="Triceps skin fold thickness")
        diabetes_pedigree = st.number_input('🧬 Diabetes Pedigree Function', min_value=0.0, help="Genetic diabetes likelihood")
    
    with col2:
        glucose = st.number_input('🍯 Glucose Level (mg/dL)', min_value=0.0, help="Plasma glucose concentration")
        insulin = st.number_input('💉 Insulin Level (μU/mL)', min_value=0.0, help="2-Hour serum insulin")
        age = st.number_input('📅 Age (years)', min_value=0, format="%d", help="Age in years")
    
    with col3:
        blood_pressure = st.number_input('🩸 Blood Pressure (mmHg)', min_value=0.0, help="Diastolic blood pressure")
        bmi = st.number_input('⚖️ BMI (kg/m²)', min_value=0.0, help="Body mass index")

    # Prediction
    if st.button('🔬 Analyze Diabetes Risk', help="Click to get AI prediction"):
        try:
            features = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]]
            prediction = diabetes_model.predict(features)
            
            if prediction[0] == 1:
                st.error('⚠️ **HIGH RISK**: The AI model indicates a high probability of diabetes. Please consult a healthcare professional for proper diagnosis and treatment.')
            else:
                st.success('✅ **LOW RISK**: The AI model indicates a low probability of diabetes. Continue maintaining a healthy lifestyle!')
                
        except Exception as e:
            st.error(f"🚨 Prediction Error: {e}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Heart Disease Prediction Page
elif selected == '❤️ Heart Disease Prediction':
    st.markdown('<h1 class="section-header">❤️ Cardiovascular Risk Assessment</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="prediction-card ai-decoration">
        <p style="color: #5a6c7d; font-size: 1.1rem; margin-bottom: 1.5rem; text-align: center;">
            Comprehensive cardiac health evaluation using advanced AI algorithms
        </p>
    """, unsafe_allow_html=True)

    # Input fields with better organization
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        age = st.number_input('📅 Age (years)', min_value=0, format="%d")
        cp = st.number_input('💔 Chest Pain Type (0-3)', min_value=0, max_value=3, format="%d", 
                           help="0: Typical angina, 1: Atypical angina, 2: Non-anginal pain, 3: Asymptomatic")
        fbs = st.selectbox('🍬 Fasting Blood Sugar > 120 mg/dl', [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        exang = st.selectbox('🏃 Exercise-Induced Angina', [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    
    with col2:
        sex = st.selectbox('👤 Gender', [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
        trestbps = st.number_input('🩸 Resting Blood Pressure (mmHg)', min_value=0.0)
        restecg = st.number_input('📈 Resting ECG (0-2)', min_value=0, max_value=2, format="%d",
                                help="0: Normal, 1: ST-T abnormality, 2: LV hypertrophy")
        oldpeak = st.number_input('📉 ST Depression', min_value=0.0, help="Exercise-induced ST depression")
    
    with col3:
        chol = st.number_input('🧪 Serum Cholesterol (mg/dl)', min_value=0.0)
        thalach = st.number_input('💓 Max Heart Rate Achieved', min_value=0.0)
        slope = st.number_input('📊 Slope of ST Segment (0-2)', min_value=0, max_value=2, format="%d",
                              help="0: Upsloping, 1: Flat, 2: Downsloping")
    
    with col4:
        ca = st.number_input('🔬 Major Vessels (0-3)', min_value=0, max_value=3, format="%d", 
                           help="Number of major vessels colored by fluoroscopy")
        thal = st.number_input('🫀 Thalassemia (0-3)', min_value=0, max_value=3, format="%d",
                             help="3: Normal, 6: Fixed defect, 7: Reversible defect")

    # Prediction
    if st.button('🔬 Analyze Heart Disease Risk', help="Click to get AI prediction"):
        try:
            features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            prediction = heart_disease_model.predict(features)
            
            if prediction[0] == 1:
                st.error('⚠️ **HIGH RISK**: The AI model indicates a high probability of heart disease. Please consult a cardiologist immediately for proper evaluation.')
            else:
                st.success('✅ **LOW RISK**: The AI model indicates a low probability of heart disease. Continue maintaining good cardiovascular health!')
                
        except Exception as e:
            st.error(f"🚨 Prediction Error: {e}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Parkinson's Prediction Page
elif selected == "🧠 Parkinson's Prediction":
    st.markdown('<h1 class="section-header">🧠 Parkinson\'s Disease Assessment</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="prediction-card ai-decoration">
        <p style="color: #5a6c7d; font-size: 1.1rem; margin-bottom: 1.5rem; text-align: center;">
            Advanced voice biomarker analysis for early Parkinson's detection
        </p>
    """, unsafe_allow_html=True)

    # Input fields organized by categories
    st.markdown("### 🎵 **Fundamental Frequency Measures**")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        fo = st.number_input('📊 MDVP:Fo(Hz)', min_value=0.0, help="Average vocal fundamental frequency")
    with col2:
        fhi = st.number_input('📈 MDVP:Fhi(Hz)', min_value=0.0, help="Maximum vocal fundamental frequency")
    with col3:
        flo = st.number_input('📉 MDVP:Flo(Hz)', min_value=0.0, help="Minimum vocal fundamental frequency")
    
    st.markdown("### 🎯 **Jitter Measures (Frequency Variation)**")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        jitter_percent = st.number_input('📊 MDVP:Jitter(%)', min_value=0.0, help="Jitter as percentage")
    with col2:
        jitter_abs = st.number_input('📏 MDVP:Jitter(Abs)', min_value=0.0, help="Absolute jitter")
    with col3:
        rap = st.number_input('🎵 MDVP:RAP', min_value=0.0, help="Relative average perturbation")
    with col4:
        ppq = st.number_input('🎶 MDVP:PPQ', min_value=0.0, help="Five-point period perturbation quotient")
    
    col1, col2 = st.columns(2)
    with col1:
        ddp = st.number_input('🎼 Jitter:DDP', min_value=0.0, help="Average absolute difference of differences between jitter cycles")
    
    st.markdown("### 🔊 **Shimmer Measures (Amplitude Variation)**")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        shimmer = st.number_input('📊 MDVP:Shimmer', min_value=0.0, help="Local shimmer")
    with col2:
        shimmer_db = st.number_input('📈 MDVP:Shimmer(dB)', min_value=0.0, help="Shimmer in decibels")
    with col3:
        apq3 = st.number_input('🎵 Shimmer:APQ3', min_value=0.0, help="Three-point amplitude perturbation quotient")
    with col4:
        apq5 = st.number_input('🎶 Shimmer:APQ5', min_value=0.0, help="Five-point amplitude perturbation quotient")
    
    col1, col2 = st.columns(2)
    with col1:
        apq = st.number_input('🎼 MDVP:APQ', min_value=0.0, help="Amplitude perturbation quotient")
    with col2:
        dda = st.number_input('📊 Shimmer:DDA', min_value=0.0, help="Average absolute differences between amplitudes")
    
    st.markdown("### 🎚️ **Harmonic-to-Noise Ratio**")
    col1, col2 = st.columns(2)
    with col1:
        nhr = st.number_input('📈 NHR', min_value=0.0, help="Noise-to-harmonic ratio")
    with col2:
        hnr = st.number_input('📊 HNR', min_value=0.0, help="Harmonic-to-noise ratio")
    
    st.markdown("### 🔬 **Nonlinear Dynamics Measures**")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        rpde = st.number_input('🌀 RPDE', min_value=0.0, help="Recurrence period density entropy")
    with col2:
        dfa = st.number_input('📊 DFA', min_value=0.0, help="Detrended fluctuation analysis")
    with col3:
        spread1 = st.number_input('📈 Spread1', min_value=-10.0, help="Nonlinear measure of fundamental frequency variation")
    with col4:
        spread2 = st.number_input('📉 Spread2', min_value=0.0, help="Nonlinear measure of fundamental frequency variation")
    
    col1, col2 = st.columns(2)
    with col1:
        d2 = st.number_input('🎯 D2', min_value=0.0, help="Correlation dimension")
    with col2:
        ppe = st.number_input('🔊 PPE', min_value=0.0, help="Pitch period entropy")

    # Prediction
    if st.button("🔬 Analyze Parkinson's Risk", help="Click to get AI prediction"):
        try:
            features = [[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, 
                        apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]]
            prediction = parkinsons_model.predict(features)
            
            if prediction[0] == 1:
                st.error('⚠️ **POSITIVE INDICATION**: The AI model indicates potential signs of Parkinson\'s disease based on voice analysis. Please consult a neurologist for comprehensive evaluation.')
            else:
                st.success('✅ **NEGATIVE INDICATION**: The AI model shows no significant indicators of Parkinson\'s disease in the voice patterns analyzed.')
                
        except Exception as e:
            st.error(f"🚨 Prediction Error: {e}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="margin-top: 3rem; padding: 2rem; text-align: center; border-top: 2px solid rgba(102, 126, 234, 0.2);">
    <p style="color: #5a6c7d; font-size: 0.9rem;">
        ⚠️ <strong>Medical Disclaimer:</strong> This AI system is for educational and screening purposes only. 
        Always consult qualified healthcare professionals for proper medical diagnosis and treatment.
    </p>
    <p style="color: #95a5a6; font-size: 0.8rem; margin-top: 1rem;">
        🤖 Powered by Advanced Machine Learning Algorithms | Built with Streamlit
    </p>
</div>
""", unsafe_allow_html=True)
