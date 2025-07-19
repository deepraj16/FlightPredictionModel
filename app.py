import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

model = joblib.load("model.joblib")

st.set_page_config(page_title="Flight Price Predictor", layout="centered")

st.title("Flight Price Predictor")

with st.form("prediction_form"):
    st.subheader("Enter Flight Details")

    airline = st.selectbox("Airline", ["IndiGo", "Air India", "Jet Airways", "SpiceJet", "GoAir"])
    date_of_journey = st.date_input("Date of Journey")
    source = st.selectbox("Source", ["Delhi", "Kolkata", "Mumbai", "Chennai", "Banglore"])
    destination = st.selectbox("Destination", ["Cochin", "Delhi", "New Delhi", "Hyderabad", "Kolkata"])
    dep_time = st.time_input("Departure Time")
    arrival_time = st.time_input("Arrival Time")
    duration = st.text_input("Duration (e.g., 2h 50m)")
    total_stops = 1
    additional_info = st.selectbox("Additional Info", ["No info", "In-flight meal not included", "No check-in baggage included"])

    submit_btn = st.form_submit_button("Predict Price")


if submit_btn:
    try:
        input_data = pd.DataFrame({
            "airline": [airline],
            "date_of_journey": [date_of_journey.strftime("%Y-%m-%d")],
            "source": [source],
            "destination": [destination],
            "dep_time": [dep_time.strftime("%H:%M:%S")],
            "arrival_time": [arrival_time.strftime("%H:%M:%S")],
            "duration": [duration],
            "total_stops": [total_stops],
            "additional_info": [additional_info]
        })
        prediction = model.predict(input_data)[0] - 1000
        st.success(f"Estimated Price: ₹{int(prediction)} INR")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
