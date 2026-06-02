import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Mobile Price Prediction",
    page_icon="📱",
    layout="wide"
)

# Load model files
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

# Title
st.title("📱 Mobile Phone Price Prediction")
st.markdown("Enter mobile specifications below to predict its price category.")

# Sidebar
st.sidebar.title("📲 Mobile Specifications")

battery_power = st.sidebar.selectbox(
    "Battery Capacity (mAh)",
    [500, 800, 1000, 1200, 1500, 1800, 2000]
)

blue = st.sidebar.selectbox(
    "Bluetooth Support",
    ["No", "Yes"]
)

clock_speed = st.sidebar.selectbox(
    "Processor Speed (GHz)",
    [0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0]
)

dual_sim = st.sidebar.selectbox(
    "Dual SIM",
    ["No", "Yes"]
)

fc = st.sidebar.selectbox(
    "Front Camera (MP)",
    [0, 1, 2, 3, 5, 8, 10, 12]
)

four_g = st.sidebar.selectbox(
    "4G Support",
    ["No", "Yes"]
)

int_memory = st.sidebar.selectbox(
    "Internal Storage (GB)",
    [2, 4, 8, 16, 32, 64]
)

m_dep = st.sidebar.slider(
    "Mobile Thickness",
    0.1,
    1.0,
    0.5
)

mobile_wt = st.sidebar.selectbox(
    "Mobile Weight (g)",
    [80, 100, 120, 140, 160, 180, 200]
)

n_cores = st.sidebar.selectbox(
    "CPU Cores",
    [1, 2, 3, 4, 5, 6, 7, 8]
)

pc = st.sidebar.selectbox(
    "Rear Camera (MP)",
    [2, 5, 8, 10, 12, 16, 20]
)

px_height = st.sidebar.selectbox(
    "Screen Resolution Height",
    [0, 240, 480, 720, 1080, 1440, 1920]
)

px_width = st.sidebar.selectbox(
    "Screen Resolution Width",
    [240, 480, 720, 1080, 1440, 1920]
)

ram = st.sidebar.selectbox(
    "RAM (MB)",
    [256, 512, 1024, 1536, 2048, 3072, 4096]
)

sc_h = st.sidebar.slider(
    "Screen Height (cm)",
    5,
    20,
    10
)

sc_w = st.sidebar.slider(
    "Screen Width (cm)",
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
    "WiFi Support",
    ["No", "Yes"]
)

# Convert Yes/No to 1/0
blue = 1 if blue == "Yes" else 0
dual_sim = 1 if dual_sim == "Yes" else 0
four_g = 1 if four_g == "Yes" else 0
three_g = 1 if three_g == "Yes" else 0
touch_screen = 1 if touch_screen == "Yes" else 0
wifi = 1 if wifi == "Yes" else 0

# Arrange input exactly like training features
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

# Prediction
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
