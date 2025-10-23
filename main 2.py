import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
@st.cache
def load_data():
    data = pd.read_csv('sales_data.csv')  # Replace 'sales_data.csv' with your dataset
    return data

# Sidebar for user input
st.sidebar.header("User Input")
data = load_data()
feature_cols = st.sidebar.multiselect("Select Features", data.columns.tolist())
target_col = st.sidebar.selectbox("Select Target", data.columns.tolist())

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data[feature_cols], data[target_col], test_size=0.2, random_state=42)

# XGBoost model training
model = xgb.XGBRegressor()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)



# Streamlit app
st.title("Sales Prediction App")

# Display dataset
st.write("## Sales Data")
st.write(data.head())



# User input form
st.sidebar.header("Make a Prediction")
input_features = {}

for feature in feature_cols:
    input_features[feature] = st.sidebar.number_input(f"Enter {feature}", min_value=data[feature].min(), max_value=data[feature].max())

# Make a prediction
input_data = pd.DataFrame([input_features])
prediction = model.predict(input_data[feature_cols])

# Display prediction
st.sidebar.header("Prediction")
st.sidebar.write(f"The predicted value is: {prediction[0]:,.2f}")
