import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
df = pd.read_csv('Walking-Cycling.csv')

#Streamlit app
st.title("Walking and Cycling Data Analysis", anchor='top')
st.header("This app analyzes the Walking and Cycling dataset.")

st.sidebar.header("About the Project")
st.sidebar.subheader("This app is created by Mohammad Baratnezhad")
st.sidebar.write("This dataset contains information about walking and cycling scheme in different areas of UK from 2010 to 2017.\n 'https://data.london.gov.uk/dataset/walking-and-cycling-borough'")

#Bar chart of the dataset
#Histogram of walking data
st.markdown("Histograms for distribution and basic sight")
df['Walking']=df['Walking_%']
walking_hist = px.histogram(df, x='Walking', title='Walking Percentage',color_discrete_sequence=['blue'])
walking_hist.update_layout(yaxis_title_text='Number of areas', xaxis_title_text='Walking Percentage') 
st.plotly_chart(walking_hist)
#Histogram of cycling data
df['Cycling']=df['Cycling_%']
Cycling__hist = px.histogram(df, x='Cycling', title='Cycling Percentage',color_discrete_sequence=['blue'])
Cycling__hist.update_layout(yaxis_title_text='Number of areas', xaxis_title_text='Cycling Percentage')   
#Cycling__hist.show()
st.plotly_chart(Cycling__hist)

# Tree map: Walking and Cycling percentages by Local Authority
df['Cycling'] = pd.to_numeric(df['Cycling'], errors='coerce')
st.subheader("Tree Map of Walking OR Cycling Percentages by Area")
st.caption('Cycling as value and Walking as color OR walking as value and cycling as color.')
usertreechoice = st.radio('Pick your preference',['Walking as color','Cycling as color'])
if usertreechoice == 'Cycling as color':
    st.subheader("Tree Map of Walking Percentages by Area")
    tree_map = px.treemap(df, path=['Local Authority'], values='Walking', color='Cycling',color_continuous_scale=px.colors.sequential.RdBu)
    st.plotly_chart(tree_map)
else:
    st.subheader("Tree Map of Cycling Percentages by Area")
    tree_map = px.treemap(df, path=['Local Authority'], values='Cycling', color='Walking', color_continuous_scale=px.colors.sequential.RdBu)
    st.plotly_chart(tree_map)

# Pie chart of the dataset
# Pie chart: Walking and Cycling percentages
userpie=st.selectbox('Choose a pie chart', ['Walking', 'Cycling'])
st.subheader("Pie Chart of Walking and Cycling Percentages")
userareapie = st.multiselect('Choose a Area', df['Local Authority'].unique())
st.caption('Choose a Area to see the pie chart of walking and cycling percentages.')
st.markdown('You can select multiple Areas And see the pie chart of walking and cycling percentages.\n for comparing the Areas with each other.')
st.caption('If you select no Area, the pie chart will be shown for all Areas.')
if userareapie == []:
    piedf = df
else:
    piedf= df[df['Local Authority'].isin(userareapie)][['Local Authority', 'Walking', 'Cycling']]
    
if userpie == 'Walking':
    st.subheader("Pie Chart of Walking Percentages")
    walking_pie = px.pie(piedf, values='Walking', names='Local Authority', color_discrete_sequence=px.colors.sequential.RdBu)
    walking_pie.update_traces(textinfo='percent+label')
    st.plotly_chart(walking_pie)
elif userpie == 'Cycling':
    st.subheader("Pie Chart of Cycling Percentages")
    cycling_pie = px.pie(piedf, values='Cycling', names='Local Authority', color_discrete_sequence=px.colors.sequential.RdBu)
    cycling_pie.update_traces(textinfo='percent+label')
    st.plotly_chart(cycling_pie)


# Line chart: Walking and Cycling percentages over time
#df['Walking'] = pd.to_numeric(df['Walking'], errors='coerce')
df['Cycling'] = pd.to_numeric(df['Cycling'], errors='coerce')
# User input: Select an area
st.markdown('You can select an area and frequency to see the line chart of walking and cycling percentages.\n change frequency to less periods would consider more accurate data and shows the data was consistent during the periods.')
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

