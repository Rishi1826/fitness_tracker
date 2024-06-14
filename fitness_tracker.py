import streamlit as st
import pandas as pd
import datetime

# Initialize session state
if 'activities' not in st.session_state:
    st.session_state['activities'] = []
if 'diet' not in st.session_state:
    st.session_state['diet'] = []
if 'metrics' not in st.session_state:
    st.session_state['metrics'] = []

st.title("Fitness Tracker")

# Section for physical activities
st.header("Log Physical Activities")
activity = st.text_input("Activity")
duration = st.number_input("Duration (minutes)", min_value=0)
calories_burned = st.number_input("Calories Burned", min_value=0)
activity_date = st.date_input("Date", datetime.date.today())

if st.button("Add Activity"):
    if activity and duration and calories_burned:
        st.session_state['activities'].append({
            'Activity': activity,
            'Duration (minutes)': duration,
            'Calories Burned': calories_burned,
            'Date': activity_date
        })
        st.success("Activity added!")
    else:
        st.error("Please fill in all fields.")

# Section for diet
st.header("Log Diet")
food = st.text_input("Food")
calories = st.number_input("Calories", min_value=0)
diet_date = st.date_input("Date", datetime.date.today(), key="diet_date")

if st.button("Add Diet"):
    if food and calories:
        st.session_state['diet'].append({
            'Food': food,
            'Calories': calories,
            'Date': diet_date
        })
        st.success("Diet entry added!")
    else:
        st.error("Please fill in all fields.")

# Section for health metrics
st.header("Log Health Metrics")
weight = st.number_input("Weight (kg)", min_value=0.0)
height = st.number_input("Height (cm)", min_value=0.0)
bmi = weight / ((height / 100) ** 2) if height > 0 else 0
metrics_date = st.date_input("Date", datetime.date.today(), key="metrics_date")

if st.button("Add Health Metrics"):
    if weight and height:
        st.session_state['metrics'].append({
            'Weight (kg)': weight,
            'Height (cm)': height,
            'BMI': bmi,
            'Date': metrics_date
        })
        st.success("Health metrics added!")
    else:
        st.error("Please fill in all fields.")

# Display logs
st.header("Activity Log")
if st.session_state['activities']:
    st.dataframe(pd.DataFrame(st.session_state['activities']))

st.header("Diet Log")
if st.session_state['diet']:
    st.dataframe(pd.DataFrame(st.session_state['diet']))

st.header("Health Metrics Log")
if st.session_state['metrics']:
    st.dataframe(pd.DataFrame(st.session_state['metrics']))