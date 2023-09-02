import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')


st.title('California Housing Data (1990) by Yuxin Ou')
path = 'C:/Users/HP/Documents/housing.csv/housing.csv'
df = pd.read_csv(path)

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Median House Price (Millions):', 0, 200000, 500001)  # min, max, default

# create a multi select
capital_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a input form
income_filter = st.sidebar.radio('Choose income level',
                                  ('Low','Media','High'))

df = df[df.median_house_value<= price_filter]

if income_filter == 'Low':
    df = df[df.median_income<=2.5]
if income_filter == 'Medium':
    df = df[(df.median_income>2.5)&(df.median_income<4.5)]
if income_filter == 'High':
    df = df[df.median_income>=4.5]


# show on map
st.subheader('See more filers in the sidebar:')
st.map(df)


# show the plot
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(20, 10))
df.median_house_value.plot.hist(ax=ax,bins=30)
st.pyplot(fig)