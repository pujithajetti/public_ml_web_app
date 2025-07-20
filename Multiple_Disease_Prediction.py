

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Page configuration
st.set_page_config(
    page_title="AI Disease Prediction System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional design
st.markdown("""
<style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main app styling */
    .stApp {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .main .block-container {
        padding: 2rem;
        max-width: 1400px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 1rem auto;
    }
    
    /* Title styling */
    .main-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
        font-family: 'Poppins', sans-serif;
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    /* Section headers */
    .section-title {
        color: #2d3748;
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Card styling */
    .feature-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        border: 1px solid #e2e8f0;
        margin-bottom: 1rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    }
    
    .card-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 0.5rem;
    }
    
    .card-description {
        color: #4a5568;
        line-height: 1.6;
        font-size: 0.95rem;
    }
    
    /* Input styling */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        border: 2px solid #e2e8f0;
        border-radius: 8px;
        padding: 0.5rem 0.75rem;
        font-size: 0.9rem;
        transition: border-color 0.2s ease;
        background: white;
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-size: 1rem;
        font-weight: 600;
        transition: all 0.2s ease;
        width: 100%;
        margin-top: 1rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    /* Success and error messages */
    .stSuccess {
        background: #f0fff4;
        border: 1px solid #9ae6b4;
        border-radius: 8px;
        color: #2f855a;
    }
    
    .stError {
        background: #fff5f5;
        border: 1px solid #feb2b2;
        border-radius: 8px;
        color: #c53030;
    }
    
    /* Input labels */
    .stNumberInput label, .stSelectbox label {
        color: #2d3748;
        font-weight: 500;
        font-size: 0.9rem;
        margin-bottom: 0.25rem;
    }
    
    /* How it works section */
    .how-it-works {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        margin-top: 2rem;
        border: 1px solid rgba(102, 126, 234, 0.1);
    }
    
    .how-it-works h3 {
        color: #2d3748;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .how-it-works p {
        color: #4a5568;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Footer */
    .footer {
        margin-top: 3rem;
        padding: 2rem;
        text-align: center;
        border-top: 2px solid #e2e8f0;
    }
    
    .disclaimer {
        color: #4a5568;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    .credits {
        color: #718096;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Load the saved models
try:
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
except FileNotFoundError as e:
    st.error(f"Error loading models: {e}")

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        'Disease Prediction System',
        ['Overview', 'Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"],
        icons=['house', 'activity', 'heart', 'brain'], 
        default_index=0,
        styles={
            "container": {"padding": "1rem", "background-color": "#f8f9fa"},
            "nav-link": {
                "font-size": "1rem",
                "text-align": "left",
                "margin": "0.2rem 0",
                "padding": "0.75rem 1rem",
                "border-radius": "8px",
                "color": "#495057",
            },
            "nav-link-selected": {
                "background-color": "#667eea",
                "color": "white",
                "font-weight": "600",
            },
            "icon": {"color": "inherit", "font-size": "1rem"},
        }
    )

# Overview Page
if selected == 'Overview':
    st.markdown('<h1 class="main-title">AI-Powered Disease Prediction System</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Harness the power of artificial intelligence to predict potential health conditions with advanced machine learning algorithms.</p>', unsafe_allow_html=True)
    
    # Feature cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="card-title">🩺 Diabetes Prediction</div>
            <div class="card-description">Advanced ML model analyzing glucose levels, BMI, age, and other metabolic factors to predict diabetes risk with high accuracy.</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="card-title">❤️ Heart Disease Prediction</div>
            <div class="card-description">Comprehensive cardiovascular risk assessment using multiple biomarkers and clinical parameters for early detection.</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="card-title">🧠 Parkinson's Prediction</div>
            <div class="card-description">Sophisticated voice analysis and motor function evaluation to identify early signs of Parkinson's disease.</div>
        </div>
        """, unsafe_allow_html=True)
    
    # How it works section
    st.markdown("""
    <div class="how-it-works">
        <h3>🚀 How It Works</h3>
        <p>Select a prediction module from the sidebar, input your health parameters, and our AI models will provide instant, accurate predictions based on trained data from thousands of medical cases.</p>
    </div>
    """, unsafe_allow_html=True)

# Diabetes Prediction Page
elif selected == 'Diabetes Prediction':
    st.markdown('<h1 class="section-title">🩺 Diabetes Prediction</h1>', unsafe_allow_html=True)
    
    # Input fields - keeping exact original parameters
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
elif selected == 'Heart Disease Prediction':
    st.markdown('<h1 class="section-title">❤️ Heart Disease Prediction</h1>', unsafe_allow_html=True)

    # Input fields - keeping exact original parameters
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
elif selected == "Parkinson's Prediction":
    st.markdown('<h1 class="section-title">🧠 Parkinson\'s Disease Prediction</h1>', unsafe_allow_html=True)

    # Input fields - keeping exact original parameters
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

# Footer
st.markdown("""
<div class="footer">
    <div class="disclaimer">
        ⚠️ <strong>Medical Disclaimer:</strong> This AI system is for educational and screening purposes only. 
        Always consult qualified healthcare professionals for proper medical diagnosis and treatment.
    </div>
    <div class="credits">
        🤖 Powered by Advanced Machine Learning Algorithms | Built with Streamlit
    </div>
</div>
""", unsafe_allow_html=True)
