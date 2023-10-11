#import packages
import streamlit as st
import pandas as pd
import plotly.express as px

#import data
vehicles = pd.read_csv('vehicles_us.csv')

#split model into two new columns
vehicles[['car_make', 'car_model']] = vehicles['model'].str.split(' ', n=1, expand=True)


## create filtered data sets

#top types filter
vehicles['type'] = vehicles['type'].replace('pickup','truck')
type_counts = vehicles['type'].value_counts().nlargest(5).index
filtered_types = vehicles[vehicles["type"].isin(type_counts)]

#top makes filter
make_counts = vehicles['car_make'].value_counts().nlargest(5).index
filtered_makes = vehicles[vehicles["car_make"].isin(make_counts)]

st.header('Days Listed from Car Advertisement for TOP 5 Car Makes and Types')

checkbox_chart = st.checkbox('Chart Toggle')

if checkbox_chart:
#type charts
    days_hist = px.histogram(filtered_types,x='days_listed',title='Days Listed Histogram',template='plotly',color='type').update_yaxes(title_text = 'frequency of listing length').update_xaxes(title_text = "days listed")
    st.plotly_chart(days_hist)

    price_scatter = px.scatter(filtered_types,x='price',y='days_listed',title='Price vs Days Listed Scatter',template='plotly',color='type').update_yaxes(title_text = "days listed")
    st.plotly_chart(price_scatter)
else: 
    #make charts
    days_hist = px.histogram(filtered_makes,x='days_listed',title='Days Listed Histogram',template='plotly',color='car_make').update_yaxes(title_text = 'frequency of listing length').update_xaxes(title_text = "days listed")
    st.plotly_chart(days_hist)
    price_scatter = px.scatter(filtered_makes,x='price',y='days_listed',title='Price vs Days Listed Scatter',template='plotly',color='car_make').update_yaxes(title_text = "days listed")
    st.plotly_chart(price_scatter)





