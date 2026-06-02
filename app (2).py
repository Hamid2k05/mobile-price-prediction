import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Mobile Price Prediction",
    page_icon="📱",
    layout="wide"
)

model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

st.title("📱 Mobile Phone Price Prediction")

st.markdown("Predict the price category of a mobile phone based on its specifications.")

st.sidebar.header("Enter Mobile Specifications")

inputs = []

for feature in feature_names:
    value = st.sidebar.number_input(
        feature,
        min_value=0.0,
        value=0.0
    )
    inputs.append(value)

if st.button("Predict Price Category"):
    data = pd.DataFrame([inputs], columns=feature_names)
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)[0]

    labels = {
        0: "Low Cost",
        1: "Medium Cost",
        2: "High Cost",
        3: "Very High Cost"
    }

    st.success(f"Predicted Category: {labels[prediction]}")

st.markdown("---")
st.write("Best Model: Logistic Regression")
st.write("Accuracy: 97.5%")
