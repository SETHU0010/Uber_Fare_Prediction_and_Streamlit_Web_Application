
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn



# title

st.title('Uber Fares Prediction')

# image
# st.image('Uber.png',width = 550)

# Load data
df = pd.read_csv('Clean_data.csv')
scale = pd.read_pickle('scale.pkl')
model = pd.read_pickle('model.pkl')

# input
passenger_count = st.number_input('Passenger Count',df['passenger_count'].min(),df['passenger_count'].max())
Distance = st.number_input('distance in km',df['distance(km)'].min(),df['distance(km)'].max())
Day = st.number_input('Day',df['Day'].min(),df['Day'].max())
year = st.number_input('year',df['year'].min(),df['year'].max())
month = st.number_input('month',df['month'].min(),df['month'].max())
hour = st.number_input('hour',df['hour'].min(),df['hour'].max())

new_data = {'passenger_count':passenger_count , 'distance(km)':Distance , 'Day':Day,'year':year,'month':month,'hour':hour}

new_data = pd.DataFrame(new_data ,index=[0])
#scale
new_data_scaled = scale.transform(new_data)
#model
fare_amount = model.predict(new_data_scaled)

#output
if st.button('Predict'):
    st.markdown('# Fare Amount: ')
    st.markdown(fare_amount.round(2))