# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
# show the title
st.title('Titanic app by Xuehua Luo')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.dataframe(df)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

fig, ax = plt.subplots(1,3,figsize = (15,5))
ax[0].boxplot(
        df[df.Pclass == 1].Fare
)
ax[0].set_xlabel('Fare')
ax[0].set_ylabel('Fare')
ax[0].set_title('Pclass=1')

ax[1].boxplot(
        df[df.Pclass == 2].Fare
)
ax[1].set_xlabel('Fare')
ax[1].set_title('Pclass=2')

ax[2].boxplot(
        df[df.Pclass == 3].Fare
)
ax[2].set_xlabel('Fare')
ax[2].set_title('Pclass=3')
st.pyplot(fig)