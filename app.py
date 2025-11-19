import streamlit as st
import pandas as pd
import pickle

# ---------------------------
# Load Model and Data
# ---------------------------
@st.cache_resource
def load_model():
    with open("Student_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

@st.cache_resource
def load_data():
    df = pd.read_csv("Clean_Data.csv")
    return df

model = load_model()
df = load_data()

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("Student Performance Prediction App")

st.write("Provide the input values to predict the student's performance score.")

# Assume dataset columns for input
# Change fields below based on your actual dataset features
features = df.columns.drop("Target")  # Replace 'Target' with actu
