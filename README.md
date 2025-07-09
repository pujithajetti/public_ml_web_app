# 🩺 Multiple Disease Prediction Web App

A Streamlit-based web application to predict the likelihood of **Diabetes**, **Heart Disease**, and **Parkinson’s Disease** using pre-trained machine learning models.

---

## 🚀 Features

- **Self-contained prediction modules**:
  - **Diabetes Prediction** using SVC
  - **Heart Disease Prediction** using Logistic Regression
  - **Parkinson’s Disease Prediction** (likely via voice/vocal features)
- Fast, interactive UI built with Streamlit for live inputs and instant results

---

## 📋 Getting Started

### Prerequisites

- Python 3.7+
- pip (package manager)

### Installation

```bash
git clone https://github.com/pujithajetti/public_ml_web_app.git
cd public_ml_web_app
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run app.py
```

This launches the app at `http://localhost:8501`.

---

## 🧠 Usage

Once loaded, you'll see separate sections for each disease:

- Fill in the requested input fields (e.g., age, blood pressure)
- Click **Predict**
- View results instantly displayed on the page

---

## 📁 Project Structure

```
public_ml_web_app/
├── app.py                         # Main Streamlit application
├── requirements.txt              # Python dependencies
├── templates/index.html          # (possibly unused in Streamlit flow)
├── heart_disease_model.sav       # Serialized Logistic Regression model
├── parkinsons_model.sav          # Serialized Parkinson’s model
├── trained_model.sav             # Likely Diabetes or general model
└── Multiple Disease pred.py      # Alternate script version
```

---

## 🛠️ Technologies Used

- **Python** – App logic & ML inference
- **Streamlit** – Web interface
- **Pickle/Joblib** – Model serialization
- **Scikit-learn** – Model training backend

---

## ✅ Model Details

- Diabetes: SVC classifier trained on relevant health data  
- Heart Disease: Logistic Regression on Cleveland/UCI dataset  
- Parkinson’s: Model trained using vocal audio features  

---

## ✅ Next Steps (To-Do)

- Add detailed docstrings & inline comments in `app.py`
- Build UI visualization (e.g., charts showing feature importance)
- Containerize with Docker for production deployment
- Add CI/CD and tests
- Create `requirements-dev.txt` and GitHub Actions CI pipeline

---

## 📄 License

Add your license here (e.g. MIT License).  
*(Currently not specified in the repository.)*

---

## 🙋‍♂️ Contribution

Contributions are welcome! Feel free to open issues, suggest features, or submit PRs.