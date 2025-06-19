import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
import time
import matplotlib.pyplot as plt
import plotly.express as px

# API URL
API_URL = "http://127.0.0.1:8000/predict"

# Feature list used in prediction
features = [
    "Loans Accessed", "Sentiment Score", "Monthly Avg Balance",
    "Declined Txns", "Overdraft Events", "App Logins",
    "Tickets Raised", "Web Logins"
]

# Slider bounds
bounds = {
    "Loans Accessed": (0, 10),
    "Sentiment Score": (0.0, 1.0),
    "Monthly Avg Balance": (0, 100000),
    "Declined Txns": (0, 20),
    "Overdraft Events": (0, 10),
    "App Logins": (0, 100),
    "Tickets Raised": (0, 15),
    "Web Logins": (0, 100)
}

# --- Page Setup ---
st.set_page_config(page_title="CPRS | Advanced Churn Dashboard", layout="wide")
st.markdown("""
    <style>
    .stButton button {
        background-color: #004080;
        color: white;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        font-size: 0.8rem;
        margin-top: 50px;
        color: gray;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("download.png", width=500)

st.markdown("<h1 style='text-align: center; color: #0a58ca;'>Customer Retention Proactive System</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: gray;'>AI-powered insights with tailored retention strategies</h5>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("1.png", width=750)
st.markdown("---")

# --- Initialize Session Tracker ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Sidebar Inputs ---
st.sidebar.header("📋 Input Customer Profile")
inputs = {}
for feature in features:
    min_val, max_val = bounds[feature]
    step = 0.01 if isinstance(min_val, float) else 1
    inputs[feature] = st.sidebar.slider(feature, min_val, max_val, step=step)

# --- Predict Button ---
if st.sidebar.button("🚀 Predict Churn Risk"):
    with st.spinner("Processing prediction..."):
        payload = {"data": [inputs[f] for f in features]}
        try:
            response = requests.post(API_URL, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
            if response.status_code == 200:
                result = response.json()

                # Save session log
                log = {
                    "Prediction": "CHURN" if result["prediction"] == 1 else "NO CHURN",
                    "Churn Probability": round(result["churn_probability"], 4),
                    "Risk Level": result["risk_segment"],
                    "Timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state.history.append(log)

                # Animate results
                time.sleep(1)
                st.success("✅ Prediction received... displaying insights")
                time.sleep(1)

                col1, col2, col3 = st.columns(3)
                col1.metric("🧠 Prediction", "Likely to Churn" if result["prediction"] == 1 else "No churn")
                time.sleep(0.5)
                col2.metric("📈 Churn Probability", f"{result['churn_probability'] * 100:.2f}%")
                time.sleep(0.5)
                col3.metric("🚨 Risk Segment", result["risk_segment"])
                time.sleep(0.5)

                st.markdown("### 📝 Executive Summary")
                st.success(result["message"])
                time.sleep(0.5)

                st.markdown("### 🧾  Explanation of Prediction")
                st.info(result["churn_reason"])
                time.sleep(0.5)

                st.markdown("### 🛠️ Recommended Retention Strategy")
                st.warning(result["recommended_strategy"])
                st.progress(result["churn_probability"])

                
            else:
                st.error(f"❌ API Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"❌ Failed to connect to API: {e}")

# --- Session Viewer ---
if st.sidebar.checkbox("📂 Show Prediction History"):
    st.markdown("### 🧾 Session Prediction History")
    history_df = pd.DataFrame(st.session_state.history)
    st.dataframe(history_df)
    st.download_button("📥 Download Session History", data=history_df.to_csv(index=False),
                       file_name="churn_session_log.csv", mime="text/csv")

# --- Footer ---
st.markdown("<div class='footer'>CRPS Dashboard © 2025 • Powered by Quantumsoft Technolgies Pvt Ltd.</div>", unsafe_allow_html=True)
