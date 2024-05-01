import streamlit as st
import pandas as pd
from joblib import load
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the logistic regression model
model = load('best_logistic_regression_model.joblib')

# Setup Streamlit UI
st.title('PredictVote')

# Create a dictionary to hold user inputs
user_input = {}

# Create sliders for numerical features
for feature, range_vals in data_structure.items():
    if isinstance(range_vals, list):  # Assuming it's a numerical range
        user_input[feature] = st.slider(f'Select {feature}', min_value=range_vals[0], max_value=range_vals[1], value=(range_vals[0] + range_vals[1]) // 2)
    else:  # It's a categorical feature
        user_input[feature] = st.selectbox(f'Select {feature}', range_vals)

# Convert user inputs to DataFrame for prediction
input_df = pd.DataFrame([user_input])

# Preprocessing and predictions
categorical_cols = ['statut_commune_uu2020']
numerical_cols = input_df.columns.drop('statut_commune_uu2020')

categorical_transformer = OneHotEncoder(handle_unknown='ignore')
numerical_transformer = StandardScaler()

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

pipeline = Pipeline(steps=[('preprocessor', preprocessor)])

# Transform the input data
X_transformed = pipeline.fit_transform(input_df)

# Use the model to make a prediction
prediction = model.predict(X_transformed)

# Display the prediction
st.write(f'The predicted category is: {prediction[0]}')
