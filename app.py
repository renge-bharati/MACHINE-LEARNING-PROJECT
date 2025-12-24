import streamlit as st
import numpy as np
import pickle
import os

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Water Quality Prediction",
    page_icon="💧",
    layout="centered"
)

st.title("💧 Water Quality Prediction App")
st.write("Predict whether water is **Safe (1)** or **Not Safe (0)**")

# --------------------------------------------------
# Load model safely
# --------------------------------------------------
MODEL_PATH = "water_quality_model.pkl"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        st.error("❌ Model file not found: water_quality_model.pkl")
        st.stop()
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# --------------------------------------------------
# User Inputs (MATCH TRAINING FEATURES)
# --------------------------------------------------
st.subheader("🧪 Enter Water Parameters")

ph = st.number_input("pH", 0.0, 14.0, 7.0)
hardness = st.number_input("Hardness", 0.0, 500.0, 150.0)
s
