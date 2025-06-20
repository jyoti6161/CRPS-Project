from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Load model and selected features
model = joblib.load("catboost_model.pkl")
features = joblib.load("selected_features.pkl")

# FastAPI instance
app = FastAPI(title="CPRS | Churn Prediction API")

# Request schema
class ChurnInput(BaseModel):
    data: list

# Churn reason explanation
def churn_reason(row):
    reasons = []
    if row["Loans Accessed"] == 0:
        reasons.append("the customer hasn't used loan features recently")
    if row["Sentiment Score"] < 0.3:
        reasons.append("they have shown low sentiment in support chats")
    if row["Monthly Avg Balance"] < 1000:
        reasons.append("their account balance is consistently low")
    if row["Declined Txns"] > 3:
        reasons.append("they’ve had multiple declined transaction attempts")
    if row["Overdraft Events"] > 2:
        reasons.append("they experience frequent overdraft events")
    if row["App Logins"] < 5:
        reasons.append("mobile app usage is very low")
    if row["Tickets Raised"] > 3:
        reasons.append("they’ve raised frequent support tickets")
    if row["Web Logins"] < 2:
        reasons.append("web portal usage is minimal")
    return (
        "The customer is likely to churn because " + "; ".join(reasons) + "."
        if reasons else
        "No strong churn signals detected based on recent behavior."
    )

# Probability-based risk segment
def final_risk_segment(prob):
    if prob > 0.80:
        return "🔴 High Risk"
    elif prob >= 0.40:
        return "🟠 Medium Risk"
    else:
        return "🟢 Low Risk"

# Strategy from probability
def recommended_action(prob):
    if prob > 0.80:
        return (
            "🚨 High priority: Assign a customer success agent within 24 hours. "
            "Offer personalized retention benefits and begin 30-day watch with alerts."
        )
    elif prob >= 0.40:
        return (
            "⚠️ Moderate priority: Send retention email with feature suggestions and bonus. "
            "Follow up if inactive for 7–14 days."
        )
    else:
        return (
            "✅ Low priority: Send loyalty appreciation message and invite to referral program. "
            "Monitor sentiment and usage monthly."
        )

# Churn message for business users
def churn_message(pred):
    return (
        "Churn risk detected – customer requires retention intervention."
        if pred == 1 else
        "Customer appears stable – no immediate churn indicators."
    )

@app.get("/")
def home():
    return {"message": "Welcome to the CRPS Churn Prediction API!"}

@app.post("/predict")
def predict_churn(input_data: ChurnInput):
    try:
        if len(input_data.data) != len(features):
            raise HTTPException(status_code=400, detail=f"Expected {len(features)} features.")

        X = np.array(input_data.data).reshape(1, -1)
        pred = model.predict(X)[0]
        proba = model.predict_proba(X)[0][1]

        row = dict(zip(features, input_data.data))
        risk_label = final_risk_segment(proba)
        reason = churn_reason(row) if pred == 1 else "No strong churn signals detected. Customer appears healthy based on current usage behavior."
        action = recommended_action(proba)
        message = churn_message(pred)

        return {
            "prediction": int(pred),
            "churn_probability": round(float(proba), 4),
            "risk_segment": risk_label,
            "message": message,
            "churn_reason": reason,
            "recommended_strategy": action,
            "final_action": f"{risk_label} → {action}"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
