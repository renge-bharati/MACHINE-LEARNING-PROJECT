import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Insurance Cost Prediction",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Insurance Cost Prediction App")

# --------------------------------------------------
# Load trained model (.pkl)
# --------------------------------------------------
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# --------------------------------------------------
# User Input Section
# --------------------------------------------------
st.subheader("🧮 Enter Customer Details")

age = st.number_input("Age", min_value=18, max_value=100, value=25)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=5, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox(
    "Region",
    ["southwest", "southeast", "northwest", "northeast"]
)

# --------------------------------------------------
# Manual Encoding (must match training)
# --------------------------------------------------
sex_val = 1 if sex == "male" else 0
smoker_val = 1 if smoker == "yes" else 0

region_map = {
    "southwest": 0,
    "southeast": 1,
    "northwest": 2,
    "northeast": 3
}
region_val = region_map[region]

# Create input array
input_data = np.array([[
    age,
    sex_val,
    bmi,
    children,
    smoker_val,
    region_val
]])

# --------------------------------------------------
# Prediction
# --------------------------------------------------
if st.button("🔮 Predict Insurance Cost"):
    prediction = model.predict(input_data)
    st.success(f"💵 Estimated Insurance Cost: ₹ {prediction[0]:,.2f}")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.markdown("📊 **Machine Learning Model Deployment using Streamlit**")
