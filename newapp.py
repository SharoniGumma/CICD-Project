import streamlit as st
import requests
st.set_page_config(page_title=" :mortar_board: Pass/Fail Predictor")
st.title(" :mortar_board: Student Pass/Fail Predictor")
st.write("Enter marks for 3 subjects to predict whether the student will Pass or Fail")

# Input field
m1=st.number_input("Maths marks ",min_value=0.00,max_value=100.00, value=50.00)
m2=st.number_input("Science marks ",min_value=0.00,max_value=100.00, value=50.00)
m3=st.number_input("English marks ",min_value=0.00,max_value=100.00, value=50.00)
features = [m1, m2, m3]

#Button event to check the predicted result
if st.button("Predict Result"):
    response = requests.post('http://127.0.0.1:8000/predict', json={'features': features})
    if response.status_code == 200:
        prediction = response.json().get('prediction')
        st.write(f"The model prediction",{'Pass' if prediction == 1 else 'Fail'})