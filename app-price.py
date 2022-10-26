import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

st.title('California Housing Data')
df = pd.read_csv('housing.csv')

price_filter = st.slider('Minimal Median House Pricing:',0,500001,200000)

ocean_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique()
)

df['income_level'] = pd.cut(df['median_income'],[0,2.5,4.5,15.2],labels=['low','median','high'])

income_filter = st.sidebar.selectbox(
    'income_level',
    df['income_level']
    )

df = df[df.median_house_value >= price_filter]

df = df[df.ocean_proximity.isin(ocean_filter)]

df = df[df.income_level == income_filter]

st.map(df)

st.subheader('Price Details:')
st.write(df['ocean_proximity','median_house_price','median_income','housing_median_age'])

st.subheader('The Median House Value:')
fig,ax = plt.subplots(figsize=(20,5))
median_value = df.median_house_value
median_value.plot.hist(bins=30)
st.pyplot(fig)
