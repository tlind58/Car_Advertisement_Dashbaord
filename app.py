#import packages
import streamlit as st
import pandas as pd
import plotly.express as px


#import data
vehicles = pd.read_csv('vehicles_us.csv')

#split model into two new columns
vehicles[['car_make', 'car_model']] = vehicles['model'].str.split(' ', n=1, expand=True)

#Fill Na with 0 for is_4wd
vehicles['is_4wd'] = vehicles['is_4wd'].fillna(0)



st.header('Days Listed from Car Advertisement for TOP 5 Car Makes and Types')

## create filtered data sets


#create filter for 4wd
four_wd_list = vehicles['is_4wd'].unique()
four_wd = st.selectbox(
    label='Has 4wD',
    options=four_wd_list,
    index=four_wd_list
    )

mask_filter = vehicles['is_4wd'] = four_wd
vehicles_filtered = vehicles[mask_filter]


#top types filter
#vehicles['type'] = vehicles['type'].replace('pickup','truck')  <-- commenting out
type_counts = vehicles_filtered['type'].value_counts().nlargest(5).index
filtered_types = vehicles_filtered[vehicles_filtered["type"].isin(type_counts)]

#top makes filter
make_counts = vehicles_filtered['car_make'].value_counts().nlargest(5).index
filtered_makes = vehicles_filtered[vehicles_filtered["car_make"].isin(make_counts)]


checkbox_chart = st.checkbox('Car Type Charts')

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





