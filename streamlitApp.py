# Importing the dependencies
import numpy as np
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Loading the model
loaded_model = pickle.load(open('C:/Users/User/Desktop/Github ML projects/Diabetes Prediction/trained_model.sav', 'rb'))

# Creating a function for prediction
def diabetes_prediction(input_data):
    input_data_reshaped = np.array(input_data).reshape(1,-1)

    # Converting the reshaped data to as_numpy_array
    input_data_as_numpy_array = np.asarray(input_data_reshaped)

    # standardizing the input_data_as_numpy_array
    model_scale = StandardScaler()
    scaled_input_data = model_scale.fit_transform(input_data_as_numpy_array)

    # Predicting the new data
    predicted_value = loaded_model.predict(scaled_input_data)
    print(predicted_value)

    if predicted_value[0] == 1:
        return 'The person is Diabetic'
    else:
        return 'The person is Not Diabetic'
    

def main():
    # Giving a title
    st.title('Diabetes Prediction System')
    
    # getting the input_data from the user
    # Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('BloodPressure Value')
    SkinThickness = st.text_input('SkinThickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Level')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
    Age = st.text_input('Patient Age')
    
    # code for prediction
    diagnoses = ''
    
    # creating a button for prediction
    
    if st.button('Daibetes Test Result'):
        diagnoses = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnoses)
    

if __name__ == '__main__':
    main()