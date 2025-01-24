import streamlit as st
import numpy as np
import pandas as pd
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. First, select the parameters of the ride
'''
n_passengers = range(1, 9)
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)
col6, col7 = st.columns(2)
with col1:
    st.selectbox('Number of passengers', n_passengers)
with col2:
    d = st.date_input("Date")
with col3:
    t = st.time_input("Time")
with col4:
    pickup_longitude = st.number_input('Pickup Longitude')
with col5:
    pickup_latitude = st.number_input('Pickup Latitude')
with col6:
    dropoff_longitude = st.number_input('Dropoff Longitude')
with col7:
    dropoff_latitude = st.number_input('Dropoff Latitude')


df = pd.DataFrame(
            [[pickup_latitude, pickup_longitude], [dropoff_latitude, dropoff_longitude]],
            columns=['lat', 'lon']
)

st.map(df)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...
'''
params = {"pickup_datetime" : f"{d} {t}", "pickup_longitude" : pickup_longitude,
          "pickup_latitude": pickup_latitude, "dropoff_longitude" : dropoff_longitude,
          "dropoff_latitude" : dropoff_latitude, "passenger_count" : n_passengers}

'''
3. Let's call our API using the `requests` package...
'''
response = requests.get(url, params=params)

'''
4. Let's retrieve the prediction from the **JSON** returned by the API...
'''
prediction = response.json()
'''
## Finally, we can display the prediction to the user
'''
st.text(f"Fare = {prediction['fare']}")
