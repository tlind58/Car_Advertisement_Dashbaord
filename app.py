#import packages
import streamlit as st
import pandas as pd
import plotly.express as px

#import data
vehicles = pd.read_csv('vehicles_us.csv')

#split model into two new columns
vehicles[['car_make', 'car_model']] = vehicles['model'].str.split(' ', n=1, expand=True)

st.header('Days Listed from Car Advertisement')

#histogram
days_hist = px.histogram(vehicles,x='days_listed',title='Days Listed Histogram')
st.plotly_chart(days_hist)

 #scatter

checkbox_scatter = st.checkbox('Chart Toggle')

if checkbox_scatter:
    price_scatter = px.scatter(vehicles,x='price',y='days_listed',title='Price vs Days Listed Scatter',color='type')
    st.plotly_chart(price_scatter)
else: 
    price_scatter = px.scatter(vehicles,x='price',y='days_listed',title='Price vs Days Listed Scatter',color='car_model')
    st.plotly_chart(price_scatter)





