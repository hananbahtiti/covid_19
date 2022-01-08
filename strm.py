import streamlit as st
import  numpy as np
import pandas as pd
from PIL import Image
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go


st.title('Covid_19 Cases')
st.write('It show ***CoronaVirue Cases***')
st.sidebar.title('Selector')
#image = Image.open('CoronaVirue.jpg')
#st.image(image ,use_column_width = True)
st.markdown('<style>body{background-color : lightblue;}</style>' , unsafe_allow_html = True) 



@st.cache
def load_data():
	df = pd.read_csv('owid-covid-data.csv')
	return df

df = load_data()


visualization = st.sidebar.selectbox('Select a Chart type' , ('Bar Chart', 'Pie Chart' , 'Line Chart'))
state_select = st.sidebar.selectbox('Select a state' , df['location'].unique())
status_select = st.sidebar.radio('Covid-19 patient status' , ('total_cases' , 'new_cases' , 'new_cases_smoothed' , 'total_deaths' , 'new_deaths' , 'reproduction_rate' , 'icu_patients' , 'total_tests' , 'total_vaccinations'))
selected_state = df[df['location'] == state_select]
st.markdown('## **State Level Analsis**')


def get_total_dataframe(df):
	total_dataframe = pd.DataFrame({
		'location':['total_cases' ,'new_cases' ,'new_cases_smoothed', 'total_deaths' , 'new_deaths' ,'reproduction_rate', 'icu_patients' , 'total_tests' , 'total_vaccinations'], 
		'Number of cases':(df.iloc[0]['total_cases'],
		df.iloc[0]['new_cases'],
		df.iloc[0]['new_cases_smoothed'] ,
		df.iloc[0]['total_deaths'],
		df.iloc[0]['new_deaths'],
		df.iloc[0]['reproduction_rate'] ,
		df.iloc[0]['icu_patients'],
		df.iloc[0]['total_tests'],
		df.iloc[0]['total_vaccinations'])})
	return total_dataframe

state_total = get_total_dataframe(selected_state)

if visualization=='Bar Chart':
	state_total_graph = px.bar(state_total , x ='location' , y ='Number of cases' ,
		labels ={'Number of cases':'Number of cases in%s'% (state_select)} ,color = 'location')
	st.plotly_chart(state_total_graph)

elif visualization=='Pie Chart':
	if status_select=='total_cases':
		st.title('Total Cases')
		fig = px.pie(df ,values=df['total_cases'] , names=df['location'])
		st.plotly_chart(fig)

	if status_select=='new_cases':
		st.title('Total New Cases')
		fig = px.pie(df ,values=df['new_cases'] , names=df['location'])
		st.plotly_chart(fig)

	if status_select=='new_cases_smoothed':
		st.title('Total New Cases Smoothed')
		fig = px.pie(df ,values=df['new_cases_smoothed'] , names=df['location'])
		st.plotly_chart(fig)

	if status_select=='total_deaths':
		st.title('Total Deaths Cases')
		fig = px.pie(df ,values=df['total_deaths'] , names=df['location'])
		st.plotly_chart(fig)

	if status_select=='new_deaths':
		st.title('Total New Deaths Cases')
		fig = px.pie(df ,values=df['new_deaths'] , names=df['location'])
		st.plotly_chart(fig)

	if status_select=='reproduction_rate':
		st.title('Total Reproduction Rate Cases')
		fig = px.pie(df ,values=df['reproduction_rate'] , names=df['location'])
		st.plotly_chart(fig)

	if status_select=='icu_patients':
		st.title('Total Icu Patients Cases')
		fig = px.pie(df ,values=df['icu_patients'] , names=df['location'])
		st.plotly_chart(fig)

	if status_select=='total_tests':
		st.title('Total Tests Cases')
		fig = px.pie(df ,values=df['total_tests'] , names=df['location'])
		st.plotly_chart(fig)

	if status_select=='total_vaccinations':
		st.title('Total Vaccinations Cases')
		fig = px.pie(df ,values=df['total_vaccinations'] , names=df['location'] )
		st.plotly_chart(fig)

elif visualization=='Line Chart':
	if status_select == 'total_deaths':
		st.title('Total Death Cases Among states')


def get_table():
	datatable = df[['location' , 'total_cases' , 'new_cases' ,'new_cases_smoothed',
	'total_deaths' , 'reproduction_rate' , 'icu_patients' , 'total_tests',
	'total_vaccinations']].sort_values(by=['total_cases'] , ascending = False)
	return datatable

datatable =get_table()
st.dataframe(datatable)

