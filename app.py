import streamlit as st
import pandas as pd
import pickle

# Saving the Random Forest model using pickle
#with open('random_forest_model.pkl', 'wb') as f:
 #   pickle.dump(rf_clf, f)
# Load the trained Random Forest model
file_path ='random_forest_model.pkl'
with open(file_path, 'rb') as f:
    loaded_model = pickle.load(f)


# Streamlit UI
st.title('Disease Prediction')

# User input features
feature1 = st.slider('Feature 1', min_value=0.0, max_value=100.0)
feature2 = st.slider('Feature 2', min_value=0.0, max_value=100.0)
feature3 = st.slider('Feature 3', min_value=0.0, max_value=100.0)

# Predict function using the loaded model
def predict_disease(feature1, feature2, feature3):
    features = [[feature1, feature2, feature3]]
    prediction = loaded_model.predict(features)
    return prediction

if st.button('Predict'):
    prediction_result = predict_disease(feature1, feature2, feature3)
    st.write(f"Predicted Disease: {prediction_result[0]}")
