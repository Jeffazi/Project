# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 18:57:55 2023

@author: hp
"""

import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


loaded_model = pickle.load(open('breast_cancer_model', 'rb'))

#creating a function for Classification

def breast_cancer_prediction(input_data):
    

    # changing the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    # standardize the input data
    std_data =  scaler.transform(input_data_reshaped)
    print(std_data)
    
    prediction = loaded_model.predict(std_data)
    print(prediction)
    
    if (prediction[0] == 0):
        print('The Breast Cancer is BENIGN')
    else:
        print ('The Breast Cancer is MALIGNANT')
    
    
    
def main():
    
    
    # giving a title
    st.title('Breast Cancer Classification Web App')
    
    
    # getting the input data from user
   
    
    Radius = st.text_input('Radius Mean')
    Texture = st.text_input('Texture Mean')
    Perimeter = st.text_input('Perimeter Mean')
    Area = st.text_input('Area Mean')
    Smoothness = st.text_input('Smoothness Mean')
    Compactness = st.text_input('Compactness Mean')
    Concavity = st.text_input('Concavity Mean')
    Concave = st.text_input('Concave Points Mean')
    Symmetry = st.text_input('Symmetry Mean')
    Fractal = st.text_input('Fractal Dimension Mean')
    Radiuus = st.text_input('Radius Standard Error')
    Textuure = st.text_input('Texture Standard Error')
    Perimeteer = st.text_input('Perimeter Standard Error')
    Areaa = st.text_input('Area Standard Error')
    Smoothnesss = st.text_input('Smoothness Standard Error')
    Compactnesss = st.text_input('Compactness Standard Error')
    Concavityy = st.text_input('Concavity Standard Error')
    Concavee = st.text_input('Concave Points Standard Error')
    Symmetryy = st.text_input('Symmetry Standard Error')
    Fractall = st.text_input('Fractal Dimension Standard Error')
    Radiusss = st.text_input('Radius Worst')
    Texturee = st.text_input('Texture Worst')
    Perimeterr = st.text_input('Perimeter Worst')
    Areea = st.text_input('Area Worst')
    Smouthness = st.text_input('Smoothness Worst')
    Compacctness = st.text_input('Compactness Worst')
    Concaavity = st.text_input('Concavity Worst')
    Concaave = st.text_input('Concave Points Worst')
    Syymetry = st.text_input('Symmetry Worst')
    Fructall = st.text_input('Fractal Dimension Worst')
    
    # code for prediction
    diagnosis = ''
    
    #creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        diagnosis = breast_cancer_prediction([Radius, Texture, Perimeter, Area, Smoothness, Compactness, Concavity, Concave, Symmetry, Fractal, Radiuus, Textuure, Perimeteer, Areaa, Smoothnesss, Compactnesss, Concavityy, Concavee, Symmetryy, Fractall, Radiusss, Texturee, Perimeterr, Areea, Smouthness, Compacctness, Concaavity, Concaave, Syymetry, Fructall])
        
        
    st.success(diagnosis)
    
    
    
    

if __name__ == '__main__':
    main()
