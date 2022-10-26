import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

st.title('California Housing Data')
st.subheader('Luoxuehua')
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
    df.income_level.unique()
    )

df = df[df.median_house_value >= price_filter]

df = df[df.ocean_proximity.isin(ocean_filter)]

df = df[df.income_level == income_filter]

st.map(df)

st.subheader('Price Details:')
st.write(df[['median_income','median_house_value','ocean_proximity','income_level']])

st.subheader('The Median House Value:')
fig,ax = plt.subplots(figsize=(20,5))
df.median_house_value.plot.hist(bins=30,ax=ax)
st.pyplot(fig)