import os
import streamlit as st
import matplotlib.pyplot as plt
import joblib
from sklearn.svm import SVR
from PIL import Image

model = joblib.load('SVR_classifier_bf%.joblib')

st.title('Body Fat% Calculator :weight_lifter:')

user_weight = st.number_input('Input Weight (lb)', min_value=0.0, step=0.1)
user_height = st.number_input('Input Height (inches)', min_value=0.0, step=0.1)
user_neck = st.number_input('Input Neck Circumference (inches)', min_value=0.0, step=0.1)
user_chest = st.number_input('Input Chest Circumference (inches)', min_value=0.0, step=0.1)
user_waist = st.number_input('Input Waist Circumference (inches)', min_value=0.0, step=0.1)
user_hip = st.number_input('Input Hip Circumference (inches)', min_value=0.0, step=0.1)

def convert_in_to_cm(val):
    return val*2.54

def predict():
    weight_by_height = user_weight/user_height
    waist_by_neck = convert_in_to_cm(user_waist) / convert_in_to_cm(user_neck)
    waist_by_chest = convert_in_to_cm(user_waist) / convert_in_to_cm(user_chest)
    waist_by_hip = convert_in_to_cm(user_waist) / convert_in_to_cm(user_hip)
    user_X = [weight_by_height, waist_by_neck, waist_by_chest, waist_by_hip]

    prediction = model.predict([user_X])[0]

    # print(prediction)

    st.success(round(prediction, 1))
    img = Image.open('bf_chart.png')
    st.image(img)



st.button('Calculate', on_click=predict)


# Lochan info inches:
# Height = 68.5
# Weight = 165
# Chest = 38.5
# Neck = 14.5
# Waist = 33
# Hip = 39