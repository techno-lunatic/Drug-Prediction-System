import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Drug Prediction App")

st.title("💊 Drug Prediction System")

st.write("Enter patient details to predict the suitable drug.")

# ---------------- INPUT FIELDS ---------------- #

age = st.number_input("Age", min_value=1, step=1)

sex = st.selectbox("Sex", ["M", "F"])

bp = st.selectbox("Blood Pressure", ["LOW", "NORMAL", "HIGH"])

cholesterol = st.selectbox("Cholesterol", ["NORMAL", "HIGH"])

na_to_k = st.number_input("Na_to_K Ratio", min_value=0.0, step=0.1)

# ---------------- BUTTON ---------------- #

if st.button("Predict Drug"):

    # Create payload
    payload = {
        "Age": age,
        "Sex": sex,
        "BP": bp,
        "Cholesterol": cholesterol,
        "Na_to_K": na_to_k
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            drug = result["predicted_drug"]

            st.success(f"Predicted Drug: {drug}")

        else:
            st.error(f"Error: {response.text}")

    except Exception:
        st.error("Could not connect to FastAPI server. Make sure it is running.")