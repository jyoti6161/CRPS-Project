# 🧠 Customer Retention Proactive System (CRPS)

CPRS is an AI-powered solution that predicts the likelihood of customer churn and recommends proactive retention strategies. It uses advanced machine learning models (e.g., CatBoost), explainable AI (SHAP, LIME), and an interactive Streamlit dashboard for real-time decision support.

---

## 📦 Project Structure
CPRS_Final/
├── model/
│ ├── catboost_model.pkl # Trained CatBoost model
│ └── selected_features.pkl # SHAP-selected features
├── assets/
│ ├── 1.png # Dashboard header visual
│ └── download.png # Company logo
├── churn_api.py # FastAPI backend for predictions
├── streamlit_app.py # Streamlit UI dashboard
├── requirements.txt # All Python dependencies
├── README.md # This file
