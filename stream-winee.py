import pickle
import streamlit as st

model = pickle.load(open('wine-quality.sav', 'rb'))

st.title('Prediksi Kualitas Anggur Merah')

fixed_acidity = st.text_input ('fixed acidity')

volatile_acidity = st.text_input ('volatile acidity')

citric_acid = st.text_input ('citric acid')

residual_sugar = st.text_input ('residual sugar')

chlorides = st.text_input ('chlorides')

free_sulfur_dioxide = st.text_input ('free sulfur dioxide')

total_sulfur_dioxide = st.text_input ('total sulfur dioxide')

density = st.text_input ('density') 

pH = st.text_input ('pH')

sulphates = st.text_input ('sulphates')

alcohol = st.text_input ('alcohol')

wine_diagnosis =''

if st.button('Prediksi Kualitas Anggur Merah'):
    wine_prediction = model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])

    if(wine_prediction[0]==0):
        wine_diagnosis = 'Buruk'
    elif(wine_prediction[0]==1):
        wine_diagnosis = 'Baik'
    else:
        wine_diagnosis = 'Sangat Baik'
st.success(wine_diagnosis)