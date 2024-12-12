import streamlit as st
import pickle
import numpy as np

# Load the pickle file
file_path = "/workspaces/diabetes_pickl/dataframe/diab.pkl"
with open(file_path, 'rb') as file:
    model1 = pickle.load(file)
st.write("Welcome to Diabetic prediction Analysis")


user = np.array([[0,80,0,1,4,25.19,6.6,140]])
st.write(model1.predict(user))
if model1.predict(user) == 0:
    st.write("you have no diabeties")
else:
     st.write("you have diabeties")













st.write("***Disclaimer: This prediction page is for analysis purpose only kindly consult your Doctor***")