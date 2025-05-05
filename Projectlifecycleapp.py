import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
df = pd.read_csv('Walking-Cycling.csv')

# Display the first few rows of the dataset
#print(df.head())

# Streamlit app
st.title("Walking and Cycling Data Analysis")
st.header("This app analyzes the Walking and Cycling dataset.")
#sidebar
st.sidebar.title("This app allows you to visualize the Walking and Cycling dataset.")
st.sidebar.image("https://www.oxford.gov.uk/download/downloads/id/1030/walking_and_cycling_strategy_2015-2031.pdf", caption="Walking and Cycling Strategy 2015-2031")
st.sidebar.write("This dataset contains information about walking and cycling in different areas.")

import plotly.express as px
#Bar chart of the dataset
#Histogram of walking data
df['Walking']=df['Walking_%']
walking_hist = px.histogram(df, x='Walking', title='Walking Percentage',color_discrete_sequence=['blue'])
walking_hist.update_layout(yaxis_title_text='Number of areas') 
st.plotly_chart(walking_hist)
#Histogram of cycling data
df['Cycling']=df['Cycling_%']
Cycling__hist = px.histogram(df, x='Cycling', title='Cycling Percentage',color_discrete_sequence=['blue'])
Cycling__hist.update_layout(yaxis_title_text='Number of areas') 
#Cycling__hist.show()
st.plotly_chart(Cycling__hist)


# Line chart: Walking and Cycling percentages over time
df['Cycling'] = pd.to_numeric(df['Cycling_%'], errors='coerce').fillna(0).astype(int)
# User input: Select an area
userarea = st.selectbox('Choose an area', df['Local Authority'].unique())
userfreq = st.selectbox('Choose a Frequency', df['Frequency'].unique())
st.caption('Frequency of the data collection during each year.')

# Filter data based on the selected area
filtered_data = df[(df['Local Authority'] == userarea) & (df['Frequency'] ==userfreq)]

# Line chart: Walking and Cycling percentages over time
st.subheader(f"Line Chart for {userarea}")
line_chart = px.line(
    filtered_data,
    x='Year',
    y=['Walking', 'Cycling'],
    title=f"Walking and Cycling Percentages in {userarea} frequency of {userfreq}",
    labels={'value': 'Percentage', 'variable': 'Mode of Transport'},
    color_discrete_sequence=['blue', 'orange']
)
st.plotly_chart(line_chart)

