
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("water_quality_model.pkl")

st.title("💧 Water Quality Predictor")
st.markdown("Enter water sample data to check if it's potable:")

# Input fields
ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.number_input("Hardness", min_value=0.0, value=150.0)
solids = st.number_input("Solids (ppm)", min_value=0.0, value=10000.0)
chloramines = st.number_input("Chloramines (ppm)", min_value=0.0, value=8.0)
sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, value=300.0)
conductivity = st.number_input("Conductivity (μS/cm)", min_value=0.0, value=400.0)
organic_carbon = st.number_input("Organic Carbon (ppm)", min_value=0.0, value=10.0)
trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0.0, value=60.0)
turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, value=4.0)

if st.button("Predict Potability"):
    sample = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity,
                        organic_carbon, trihalomethanes, turbidity]])
    prediction = model.predict(sample)
    result = "✅ Safe to Drink" if prediction[0] == 1 else "❌ Not Safe to Drink"
    st.success(f"Prediction: {result}")

st.title("💧 Water Quality Predictor")

with st.expander("ℹ️ About this App", expanded=True):
    st.markdown("""
    This AI-powered app predicts whether water is **safe to drink (potable)** based on its chemical characteristics.

    ### 📌 What it Does
    - Uses a trained machine learning model to classify water as **potable** or **not potable**
    - Accepts user inputs for pH, turbidity, solids, etc.
    - Returns an easy-to-read result (✅ or ❌)

    ### 🌍 SDG Alignment
    - **SDG 3: Good Health and Well-being**
    - **SDG 6: Clean Water and Sanitation**

    ### 🤖 Powered By
    - Python & Streamlit
    - scikit-learn Random Forest Classifier
    - Public dataset from [Kaggle](https://www.kaggle.com/datasets/adityakadiwal/water-potability)

    > 📣 *Note: This is a predictive tool and does not replace certified lab testing.*
    """)

