import pandas as pd
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import json
from geopy.geocoders import Nominatim
import requests
import datetime
import streamlit as st
import folium
import streamlit as st
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
# Read data
def take_data():
    all_data = pd.read_csv('https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv?raw=true').reset_index()

    all_data = all_data[['continent', 'location', 'date','new_cases','new_deaths','total_cases_per_million','total_deaths_per_million','total_vaccinations_per_hundred']].copy()
    return all_data

df_confirm = pd.read_csv('CovidData/df_confirm.csv')
df_deaths = pd.read_csv('CovidData/df_death.csv')


df_confirm['date'] =pd.to_datetime(df_confirm.date)
df_deaths['date'] = pd.to_datetime(df_deaths.date)

df_confirm = df_confirm.sort_values(by=['date'], ascending = False)
df_deaths = df_deaths.sort_values(by=['date'], ascending = False)

# Some data wrangling

country_list =list(all_data.location.unique())
country_list.sort()

# Creating streamlit Interface

# setting title
st.markdown("# Welcome to Interactive Covid-19 Analysis DashBoard ")

st.markdown("This project is performed by the CRI team at Paris.  "
            "As vaccinations increase and covid-19 approaches towards the end, "
            "we would like analyze current situation of Covid on the world. "
            "This page is created to analyze Covid-19 confirmed cases and deaths data from Jan 2020 to 2021.   ")

st.markdown("(Data is taken from open-source: https://github.com/owid/covid-19-data) ")

st.image('CovidData/covid.jpg')
st.sidebar.title("Selector")
st.sidebar.write("-----------")
st.sidebar.write("**Usage of Sidebar** ")
st.sidebar.write(" If you want to use updated data you need to click button and it will take little time....")
get_data =st.sidebar.button('Extract New Data')
st.sidebar.write("You can select new cases, new_death, total confirmed cases per million("
                 "normalized), total death cases per million(normalized), vaccination per hundred and country by "
                 "date. Feel free "
                 "to play see the graph. ")

if get_data:
    all_data = take_data()
else:
    all_data = pd.read_csv('CovidData/all_data.csv')

all_data['date'] =pd.to_datetime(all_data.date)

cd = st.sidebar.checkbox('New Cases and Death')
total = st.sidebar.checkbox('Total Confirmed Cases and Deaths(normalized)')
vac = st.sidebar.checkbox('Vaccination')

select_country = st.sidebar.multiselect("Select Countries",country_list,default=["France"])
start_date = st.sidebar.date_input('Select Start Date', datetime.date(2020,1,24))
end_date = st.sidebar.date_input('Select End Date', datetime.datetime.now().date())
st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)

new_confirmed = df_confirm[df_confirm['country'].isin(select_country)]
new_confirmed = new_confirmed.sort_values(by=['date'], ascending = False)

confirmed_plot = px.line(new_confirmed, x = 'date', y = 'value', color='country')

confirmed_plot.update_layout(title="Cumulative Number Of Covid confirmed Cases",
                 xaxis = dict(title = 'Date'),
                 yaxis = dict(title = 'Number of People'),
                 legend_title=dict(text='<b>Countries</b>'),
                  )

new_death =  df_deaths[df_deaths['country'].isin(select_country)]
new_death = new_death.sort_values(by=['date'], ascending = False)

death_plot = px.line(new_death, x = 'date', y = 'value',color='country')
death_plot.update_layout(title="Cumulative Number Of Covid Death Cases",
                 xaxis = dict(title = 'Date'),
                 yaxis = dict(title = 'Number of People'),
                 legend_title=dict(text='<b>Countries</b>'),
                  )

if case_death  == 'Confirmed cases':
    # st.write('<span style="color:%s">%s</span>' % ('red', " **Total Confirmed Cases : and Total Deaths : ** "), unsafe_allow_html=True)
    st.plotly_chart(confirmed_plot,use_container_width=True)
elif case_death == 'Death cases':
    # st.write('<span style="color:%s">%s</span>' % ('red', " **Total Confirmed Cases : and Total Deaths : ** "), unsafe_allow_html=True)
    st.plotly_chart(death_plot, use_container_width=True)