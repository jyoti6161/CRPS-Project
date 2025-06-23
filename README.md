

# 🧠Customer Churn Prediction and Proactive Retention System

An end-to-end AI-powered solution to proactively identify customers at risk of churn and recommend tailored retention strategies. Built using **CatBoost**, **SHAP**, **FastAPI**, and **Streamlit**, and fully containerized for deployment.

---

## 🔍 Overview

CRPS predicts customer churn **30–45 days in advance**, segments customers into **risk tiers**, explains why they might churn using **explainable AI**, and recommends **actionable retention strategies** in real time.

---

## 🎯 Objectives

1. Predict customer churn with high accuracy.
2. Segment customers into **Low**, **Medium**, and **High Risk** tiers.
3. Generate **explainable business reasons** behind churn.
4. Suggest **rule-based + ML-informed** retention actions.
5. Enable real-time prediction through a user-friendly dashboard.
6. Integrate API-first design for CRM or Campaign tools.
7. Allow continuous learning through session feedback.

---

## 🛠️ Tech Stack

| Layer           | Tools & Libraries                                     |
| --------------- | ----------------------------------------------------- |
| 🧠 Model        | CatBoost, SHAP, Scikit-learn                    |
| 🧪 Backend API  | FastAPI, Uvicorn                                      |
| 🖥️ Frontend UI | Streamlit                     |
| 📦 Deployment   | Docker, Render (Free Cloud Hosting), requirements.txt |
| 📂 DevOps       | GitHub, Dockerfile, render.yaml                       |

---

## 🗂️ Project Structure

```bash
CRPS_Final/
├── model/
│   ├── catboost_model.pkl              # Trained model
│   └── selected_features.pkl           # SHAP-selected features
├── assets/
│   ├── 1.png                           # Dashboard visual
│   └── download.png                    # Company logo
├── churn_api.py                        # FastAPI backend
├── streamlit_app.py                    # Interactive frontend
├── requirements.txt                    # Python dependencies
├── Dockerfile                          # Container config
├── render.yaml                         # Cloud deployment config
├── README.md                           # Project overview
├── README_FINAL.pdf                    # Final formatted report

```

---

## 🚀 Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/jyoti6161/CRPS-Project.git
cd CRPS-Project
```

### ⚙️ 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ 4. Run FastAPI Backend

```bash
uvicorn churn_api:app --reload
```

### 🌐 5. Launch Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

---

## 📈 Live Demo

🚀 [Churn Dashboard - Hosted on Render](https://crps-dashboard.onrender.com)

🧪 [API Endpoint - Hosted on Render](https://crps-api.onrender.com/predict)

---

## 📊 Features

* 🔮 Real-time churn prediction and confidence score
* 📊 Risk segmentation with color-coded tiers
* 🧾 Business-style churn reasoning
* 🎯 Retention strategy generator
* 📉 SHAP explainability used in model training
* 📂 Prediction session history + export

