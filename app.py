
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('/content/drive/MyDrive/Voyage-Analytics-MLops/models/flight_model.pkl')

st.title("✈️ Flight Price Prediction App")

st.write("Enter flight details to predict price")

# Inputs
from_loc = st.number_input("From (encoded)", min_value=0)
to_loc = st.number_input("To (encoded)", min_value=0)
flight_type = st.number_input("Flight Type (encoded)", min_value=0)
distance = st.number_input("Distance")
agency = st.number_input("Agency (encoded)", min_value=0)
year = st.number_input("Year", value=2023)
month = st.number_input("Month", min_value=1, max_value=12)
day = st.number_input("Day", min_value=1, max_value=31)

if st.button("Predict Price"):
    features = np.array([[from_loc, to_loc, flight_type, distance, agency, year, month, day]])
    prediction = model.predict(features)

    st.success(f"Predicted Flight Price: {prediction[0]:.2f}")
