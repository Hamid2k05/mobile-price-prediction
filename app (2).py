
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Mobile Price Prediction",
    page_icon="📱",
    layout="wide"
)

# Load Files
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

# Title
st.title("📱 Mobile Phone Price Prediction")
st.markdown(
    "Predict the price category of a mobile phone based on its specifications."
)

# Sidebar
st.sidebar.title("📲 Mobile Specifications")

battery_power = st.sidebar.selectbox(
    "Battery Capacity (mAh)",
    [1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000]
)

blue = st.sidebar.selectbox("Bluetooth", ["No", "Yes"])

clock_speed = st.sidebar.slider(
    "Processor Speed (GHz)",
    0.5,
    3.5,
    2.0
)

dual_sim = st.sidebar.selectbox("Dual SIM", ["No", "Yes"])

fc = st.sidebar.selectbox(
    "Front Camera (MP)",
    [2, 5, 8, 12, 16, 32]
)

four_g = st.sidebar.selectbox(
    "4G Support",
    ["No", "Yes"]
)

int_memory = st.sidebar.selectbox(
    "Internal Storage (GB)",
    [8, 16, 32, 64, 128, 256]
)

m_dep = st.sidebar.slider(
    "Mobile Thickness",
    0.1,
    1.0,
    0.5
)

mobile_wt = st.sidebar.slider(
    "Mobile Weight (g)",
    80,
    250,
    150
)

n_cores = st.sidebar.selectbox(
    "CPU Cores",
    [1, 2, 4, 6, 8]
)

pc = st.sidebar.selectbox(
    "Rear Camera (MP)",
    [8, 12, 16, 32, 48, 64, 108]
)

px_height = st.sidebar.number_input(
    "Screen Resolution Height",
    value=1280
)

px_width = st.sidebar.number_input(
    "Screen Resolution Width",
    value=720
)

ram = st.sidebar.selectbox(
    "RAM (MB)",
    [512, 1024, 2048, 3072, 4096, 6144, 8192]
)

sc_h = st.sidebar.slider(
    "Screen Height",
    5,
    20,
    10
)

sc_w = st.sidebar.slider(
    "Screen Width",
    3,
    15,
    5
)

talk_time = st.sidebar.slider(
    "Talk Time (Hours)",
    2,
    30,
    15
)

three_g = st.sidebar.selectbox(
    "3G Support",
    ["No", "Yes"]
)

touch_screen = st.sidebar.selectbox(
    "Touch Screen",
    ["No", "Yes"]
)

wifi = st.sidebar.selectbox(
    "WiFi",
    ["No", "Yes"]
)

# Convert Yes/No to 1/0
blue = 1 if blue == "Yes" else 0
dual_sim = 1 if dual_sim == "Yes" else 0
four_g = 1 if four_g == "Yes" else 0
three_g = 1 if three_g == "Yes" else 0
touch_screen = 1 if touch_screen == "Yes" else 0
wifi = 1 if wifi == "Yes" else 0

# Input Data
input_data = [[
    battery_power,
    blue,
    clock_speed,
    dual_sim,
    fc,
    four_g,
    int_memory,
    m_dep,
    mobile_wt,
    n_cores,
    pc,
    px_height,
    px_width,
    ram,
    sc_h,
    sc_w,
    talk_time,
    three_g,
    touch_screen,
    wifi
]]

if st.button("🔮 Predict Price Category"):

    data = pd.DataFrame(
        input_data,
        columns=feature_names
    )

    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)[0]

    labels = {
        0: "💰 Low Cost",
        1: "💵 Medium Cost",
        2: "💎 High Cost",
        3: "👑 Very High Cost"
    }

    st.success(
        f"Predicted Category: {labels[prediction]}"
    )

st.markdown("---")
st.write("✅ Best Model: Logistic Regression")
st.write("✅ Accuracy: 97.5%")

